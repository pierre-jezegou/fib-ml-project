"""Extract petrics from `y_pred` and `y_test` for a given model, and save in csv file."""
import os
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error, median_absolute_error, mean_absolute_error
from sklearn.inspection import permutation_importance
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt

def write_metrics_in_csv(y_pred: pd.Series,
                         y_real: pd.Series,
                         model_name: str,
                         hyperparameters: dict = None,
                         file_name: str ='metrics.csv'
                         ) -> pd.DataFrame:
    """Write metrics in csv file."""

    # Calculating metrics
    result = compute_metrics(y_pred, y_real)

    # Saving metrics in a DataFrame
    metrics = pd.DataFrame({
        'Model': [model_name],
        'Hyperparameters': [str(hyperparameters)],
        'Mean Squared Error': [result['mse']],
        'Mean Absolute Error': [result['mean_abs_e']],
        'Median Absolute Error': [result['median_abs_e']],
        'R2 Score': [result['r2']]
        })

    # Add this new row to the existing csv file
    metrics.to_csv(file_name,
                   mode='a',
                   header=not os.path.exists(file_name),
                   index=False)

    return metrics


def compute_metrics(y_pred: pd.Series,
                    y_real: pd.Series,
                    ) -> dict:

    """Compute metrics and save in csv file."""
    r2 = r2_score(y_real, y_pred)
    mse = mean_squared_error(y_real, y_pred)
    median_abs_e = median_absolute_error(y_real, y_pred)
    mean_abs_e = mean_absolute_error(y_real, y_pred)

    result = {
        'r2': r2,
        'mse': mse,
        'median_abs_e': median_abs_e,
        'mean_abs_e': mean_abs_e
    }

    return result


def plot_variable_importance(model, x: pd.DataFrame, y: pd.Series, number_of_features: int = -1):
    """Plot variable importance for a given model."""
    perm_importance = permutation_importance(model, x, y, n_repeats=30, random_state=42)
    feature_importance = perm_importance.importances_mean
    sorted_idx = np.argsort(feature_importance)

    if number_of_features > len(sorted_idx) or number_of_features < 0:
        number_of_features = len(sorted_idx)

    pos = np.arange(sorted_idx.shape[0]) + .5
    plt.figure(figsize=(10,10))
    plt.barh(pos[-number_of_features:],
             feature_importance[sorted_idx][-number_of_features:],
             align='center')
    plt.yticks(pos[-number_of_features:],
               x.columns[sorted_idx][-number_of_features:])
    plt.xlabel('Relative Importance')
    plt.title('Variable Importance')
    plt.show()


def plot_ypred_vs_yreal(y_pred: pd.Series,
                        y_real: pd.Series,
                        model_name: str = None,
                        log_scale: bool = False,
                        identity_line: bool = False
                        ) -> None:
    """Plot y_pred vs y_real."""
    if log_scale:
        y_pred = np.log(y_pred)
        y_real = np.log(y_real)

    # Add labels
    plt.xlabel('Real values')
    plt.ylabel('Predicted values')

    # If model name is provided, add it to the title
    if model_name:
        plt.title(f'{model_name} - Predicted vs Real values')
    else:
        plt.title('Predicted vs Real values')

    # Plot
    sns.scatterplot(x=y_real, y=y_pred)
    if identity_line:
        plt.plot([np.min(y_real), np.max(y_real)],
                 [np.min(y_real), np.max(y_real)],
                 '--',
                 color='red')


def learning_curve_plot(model,
                        model_name: str,
                        X: pd.DataFrame,
                        y: pd.Series,
                        train_sizes: int = 10
                        ) -> None:
    """Plot learning curve for a given model."""
    train_sizes, train_scores, val_scores = learning_curve(model,
                                                           X,
                                                           y,
                                                           cv=5,
                                                           scoring='neg_mean_squared_error',
                                                           train_sizes=np.linspace(0.1, 1.0, train_sizes))

    train_scores_mean = -train_scores.mean(axis=1)
    val_scores_mean = -val_scores.mean(axis=1)

    plt.plot(train_sizes, train_scores_mean, label='Training error')
    plt.plot(train_sizes, val_scores_mean, label='Validation error')
    plt.ylabel('MSE')
    plt.xlabel('Training size')
    plt.title(f'{model_name} - Learning curves')
    plt.legend()
    plt.show()
