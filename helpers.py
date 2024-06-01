"""Extract petrics from `y_pred` and `y_test` for a given model, and save in csv file."""
import os
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error, median_absolute_error, mean_absolute_error
from sklearn.inspection import permutation_importance
from matplotlib import pyplot as plt
import numpy as np

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
    r2 = r2_score(y_pred,y_real)
    mse = mean_squared_error(y_pred, y_real)
    median_abs_e = median_absolute_error(y_pred, y_real)
    mean_abs_e = mean_absolute_error(y_pred, y_real)

    result = {
        'r2': r2,
        'mse': mse,
        'median_abs_e': median_abs_e,
        'mean_abs_e': mean_abs_e
    }

    return result


def plot_variable_importance(model, X: pd.DataFrame, y: pd.Series):
    """Plot variable importance for a given model."""
    perm_importance = permutation_importance(model, X, y, n_repeats=30, random_state=42)
    feature_importance = perm_importance.importances_mean
    sorted_idx = np.argsort(feature_importance)

    pos = np.arange(sorted_idx.shape[0]) + .5
    plt.figure(figsize=(10,10))
    plt.barh(pos, feature_importance[sorted_idx], align='center')
    plt.yticks(pos, X.columns[sorted_idx])
    plt.xlabel('Relative Importance')
    plt.title('Variable Importance')
    plt.show()
