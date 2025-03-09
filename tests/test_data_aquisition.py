# data_handling/test_data_aquisition.py
import sys
import os

print("Current Working Directory:", os.getcwd())  # print current directory.
print("Python Path:")
for path in sys.path:
    print(path)

from data_handling.yahoo_finance import YahooFinanceDataSource  # changed line.
import pandas as pd

def test_yahoo_finance_data_acquisition():
    """Tests data acquisition from Yahoo Finance."""
    datasource = YahooFinanceDataSource()
    ticker = "RELIANCE.NS"  # Example: Reliance Industries (NSE)
    data = datasource.fetch_data(ticker, start_date="2023-01-01", end_date="2023-01-31")

    if not isinstance(data, pd.DataFrame):
        print("Error: Data is not a Pandas DataFrame.")
        return

    if data.empty:
        print("Error: No data fetched.")
        return

    print(f"Data fetched successfully for {ticker}:")
    print(data.head())

if __name__ == "__main__":
    test_yahoo_finance_data_acquisition()