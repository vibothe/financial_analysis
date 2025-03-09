# data_handling/base_datasource.py
from abc import ABC, abstractmethod
import pandas as pd

class BaseDataSource(ABC):
    @abstractmethod
    def fetch_data(self, ticker, start_date=None, end_date=None, **kwargs) -> pd.DataFrame:
        """
        Fetches data from the data source.

        Args:
            ticker (str): The ticker symbol.
            start_date (str, optional): The start date (YYYY-MM-DD).
            end_date (str, optional): The end date (YYYY-MM-DD).
            **kwargs: Additional keyword arguments.

        Returns:
            pd.DataFrame: The fetched data.
        """
        pass
