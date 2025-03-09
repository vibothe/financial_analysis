# scripts/stock_scanner.py
from data_handling.yahoo_finance import YahooFinanceDataSource
from data_handling.data_processing import calculate_returns, calculate_volatility
from modules.analysis import calculate_sharpe_ratio
from data_handling.utils import load_stock_tickers
import pandas as pd

def scan_stocks(filenames):
    datasource = YahooFinanceDataSource()
    tickers = load_stock_tickers(filenames)  # Pass the filenames
    results_df = pd.DataFrame(columns=["ticker", "returns", "volatility", "sharpe_ratio"])

    for ticker in tickers:
        data = datasource.fetch_data(ticker, start_date="2023-01-01")
        if not data.empty:
            returns = calculate_returns(data)
            volatility = calculate_volatility(returns)
            sharpe_ratio = calculate_sharpe_ratio(returns)
            results_df.loc[len(results_df)] = {"ticker": ticker, "returns": returns.mean(), "volatility": volatility.mean(), "sharpe_ratio": sharpe_ratio}

    print(results_df["volatility"])
    top_10 = results_df.nlargest(10, "sharpe_ratio")
    print("Top 10 Stocks:")
    print(top_10)

if __name__ == "__main__":
    filenames = ["nifty50.csv"]
    scan_stocks(filenames)