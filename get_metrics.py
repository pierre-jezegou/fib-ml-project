"""Extract petrics from `y_pred` and `y_test` for a given model, and save in csv file."""
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error, median_absolute_error, mean_absolute_error

def write_metrics_in_csv(y_pred: pd.Series,
                 y_test: pd.Series,
                 model_name: str,
                 file_name: str ='metrics.csv'
                 ) -> None:
    """Write metrics in csv file."""

    # Calculating metrics
    result = compute_metrics(y_pred, y_test, model_name)

    # Saving metrics in a DataFrame
    metrics = pd.DataFrame({
        'Model': [model_name],
        'Hyperparameters': [result['hyperparameters']],
        'Mean Squared Error': [result['mse']],
        'Mean Absolute Error': [result['mean_abs_e']],
        'Median Absolute Error': [result['median_abs_e']],
        'R2 Score': [result['r2']]
        })

    # Add this new row to the existing csv file
    metrics.to_csv(file_name, mode='a', header=False, index=False)


def compute_metrics(y_pred: pd.Series,
                    y_real: pd.Series,
                    model_name: str,
                    hyperparameters: dict = None
                    ) -> dict:

    """Compute metrics and save in csv file."""
    r2 = r2_score(y_pred,y_real)
    mse = mean_squared_error(y_pred, y_real)
    median_abs_e = median_absolute_error(y_pred, y_real)
    mean_abs_e = mean_absolute_error(y_pred, y_real)

    result = {
        'model': model_name,
        'hyperparameters': hyperparameters,
        'r2': r2,
        'mse': mse,
        'median_abs_e': median_abs_e,
        'mean_abs_e': mean_abs_e
    }

    return result
