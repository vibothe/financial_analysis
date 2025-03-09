import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from data_handling.yahoo_finance import YahooFinanceDataSource

def calculate_returns(data: pd.DataFrame, price_column: str = "Close") -> pd.Series:
    """Calculates returns from price data."""
    returns = data[price_column].pct_change().dropna()  # Percentage change from previous price
    return returns

def calculate_volatility(returns: pd.Series, window: int = 20) -> pd.Series:
    """Calculates rolling volatility from returns."""
    volatility = returns.rolling(window).std() * np.sqrt(252)  # Annualized volatility
    return volatility

def calculate_moving_average(data: pd.DataFrame, window: int = 20, price_column: str = "Close") -> pd.Series:
    """Calculates moving average from price data."""
    moving_average = data[price_column].rolling(window).mean()
    return moving_average

def calculate_sharpe_ratio(returns: pd.Series, risk_free_rate: float = 0.04, window: int = 252) -> float:
    """Calculates the Sharpe ratio from the returns."""
    # Subtract the risk-free rate from returns
    excess_returns = returns - risk_free_rate / 252  # Annualize the risk-free rate for daily returns
    sharpe_ratio = excess_returns.mean() / excess_returns.std() * np.sqrt(window)  # Annualized Sharpe ratio
    return sharpe_ratio

def analyze_stock(ticker: str, start_date: str, end_date: str):
    # Fetch the stock data
    data_source = YahooFinanceDataSource()
    stock_data = data_source.fetch_data(ticker, start_date, end_date)

    if stock_data.empty:
        print(f"No data found for {ticker} from {start_date} to {end_date}.")
        return

    # Calculate returns
    returns = calculate_returns(stock_data)

    # Calculate volatility
    volatility = calculate_volatility(returns)

    # Calculate moving average (20-day)
    moving_average = calculate_moving_average(stock_data, window=20)

    # Calculate Sharpe ratio
    sharpe_ratios = calculate_sharpe_ratio(returns)
    # Print Sharpe ratio

    #print(f"Sharpe Ratio for {ticker}: {sharpe_ratio:.4f}")
    
    for ticker, ratio in sharpe_ratios.items():
        print(f"Ticker: {ticker}, Sharpe Ratio: {ratio:.4f}")