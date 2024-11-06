import os
import pandas as pd

def load_example(dataset_name):
    """Loads an example dataset included in the package."""
    module_path = os.path.dirname(__file__)

    if dataset_name == "gefcom2014-wind":
        df = pd.read_csv(os.path.join(module_path, 'data', 'gefcom2014', 'gefcom2014-wind.csv'),
                        index_col=[0, 1], parse_dates=True, header=[0, 1])
        df_scores = pd.read_csv(os.path.join(module_path, 'data', 'gefcom2014', 'gefcom2014-wind-scores.csv'),
                                index_col=0)
    elif dataset_name == "solar":
        data_path = os.path.join(module_path, 'data', 'solar.csv')
    else:
        raise ValueError(f"Dataset '{dataset_name}' is not available.")

    return df, df_scores
