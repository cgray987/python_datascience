import os
import pandas


def load(path: str) -> pandas.DataFrame:
    """
    takes path to csv dataset, prints size
    returns data
    """
    try:
        if (os.path.exists(path)):
            df = pandas.read_csv(path)
            print(f"loading dataset of dimensions: {df.shape}")
        return (df)

    except Exception as e:
        print(f"Exception: {e}")
