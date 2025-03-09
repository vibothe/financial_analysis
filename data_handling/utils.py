# data_handling/utils.py
import pandas as pd
import os

def load_stock_tickers(filenames: list, data_dir: str = "data_handling/data") -> list:
    """
    Loads stock tickers from the specified CSV files.

    Args:
        filenames (list): A list of CSV filenames to load.
        data_dir (str): The directory containing the CSV files.

    Returns:
        list: A list of stock tickers.
    """
    tickers = []
    for filename in filenames:
        filepath = os.path.join(data_dir, filename)
        try:
            df = pd.read_csv(filepath)
            # Extract tickers from the "Symbol" column and add .NS
            tickers.extend([f"{ticker}.NS" for ticker in df['Symbol'].tolist()])
            print(f"Loaded {len(df)} tickers from {filename}")
        except Exception as e:
            print(f"Error reading {filename}: {e}")
    return tickers