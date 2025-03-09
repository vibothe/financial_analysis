import matplotlib.pyplot as plt
from data_handling.yahoo_finance import YahooFinanceDataSource

def plot_stock_price(ticker: str, start_date: str, end_date: str):
    """
    Fetches stock data using YahooFinanceDataSource and plots the price chart for the specified range.

    Args:
        ticker (str): The stock ticker symbol (e.g., 'AAPL').
        start_date (str): The start date (dd.mm.yyyy).
        end_date (str): The end date (dd.mm.yyyy).
    """
    # Create instance of YahooFinanceDataSource
    data_source = YahooFinanceDataSource()

    # Fetch stock data using the existing method from YahooFinanceDataSource
    stock_data = data_source.fetch_data(ticker, start_date, end_date)

    if stock_data.empty:
        print(f"No data available for {ticker} from {start_date} to {end_date}.")
        return

    # Plot the closing price
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label=f'{ticker} Close Price')
    plt.title(f'{ticker} Stock Price from {start_date} to {end_date}')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.xticks(rotation=45)
    plt.legend(loc='best')
    plt.grid(True)
    plt.tight_layout()

    # Show the plot
    plt.show()

# Example usage:
ticker = "RELIANCE.NS"  # Apple Inc. ticker for NSE
start_date = "01.01.2023"  # in dd.mm.yyyy format
end_date = "31.12.2024"    # in dd.mm.yyyy format

plot_stock_price(ticker, start_date, end_date)
