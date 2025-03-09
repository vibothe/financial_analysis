import yfinance as yf
import pandas as pd
import mplfinance as mpf

def plot_stock_candlestick(ticker, period="12mo"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)
    
    # Plot the candlestick chart
    mpf.plot(hist, type='candle',title=f'{ticker} Candlestick Chart (Daily)', ylabel='Price', style='yahoo', figscale = 2.0, figratio = (1, 0.3))

# Example usage
ticker = 'RELIANCE.NS'
period = "50d"  #"4y", "12mo", "30d"
plot_stock_candlestick(ticker, period)
