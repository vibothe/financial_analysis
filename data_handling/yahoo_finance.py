# data_handling/yahoo_finance.py
import yfinance as yf
import pandas as pd
from .base_datasource import BaseDataSource
import logging
from tenacity import retry, stop_after_attempt, wait_fixed
import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class YahooFinanceDataSource(BaseDataSource):
    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))  # Retry 3 times, wait 2 seconds between retries
    def fetch_data(self, ticker, start_date=None, end_date=None, **kwargs) -> pd.DataFrame:
        """
        Fetches data from Yahoo Finance with shitload of error handling.
        """
        if not ticker:
            logging.error("Ticker cannot be empty.")
            return pd.DataFrame()

        if start_date and not isinstance(start_date, str):
            logging.error("start_date must be a string")
            return pd.DataFrame()

        if end_date and not isinstance(end_date, str):
            logging.error("end_date must be a string")
            return pd.DataFrame()
        
        # Convert dates from dd.mm.yyyy to yyyy-mm-dd
        if start_date:
            try:
                start_date = datetime.datetime.strptime(start_date, "%d.%m.%Y").strftime("%Y-%m-%d")
            except ValueError as e:
                logging.error(f"Invalid start date format: {e}")
                return pd.DataFrame()

        if end_date:
            try:
                end_date = datetime.datetime.strptime(end_date, "%d.%m.%Y").strftime("%Y-%m-%d")
            except ValueError as e:
                logging.error(f"Invalid end date format: {e}")
                return pd.DataFrame()

        try:
            data = yf.download(ticker, start=start_date, end=end_date, **kwargs)
            if data.empty:
                logging.warning(f"No data found for {ticker} between {start_date} and {end_date}.")
            return data
        except ValueError as e:  # Handles 'No data found for symbol' errors
            logging.error(f"No data found for symbol {ticker}: {e}")
            return pd.DataFrame()
        except Exception as e:
            logging.error(f"An unexpected error occurred for {ticker}: {e}")
            return pd.DataFrame()