import yfinance as yf
import pandas as pd
import requests
import logging

pd.options.display.float_format = "{:,.0f}".format
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



def get_financial_statements(ticker:str) -> pd.DataFrame:
    """
    Get income statement for a given ticker symbol.

    Args:
        ticker (str): Ticker symbol of the stock.
    Returns:    
        pd.DataFrame: Financial statements of the stock.
    """
    try:
        logging.info(f"Fetching financial statements for {ticker}" )
        stock = yf.Ticker(ticker)
        financials = {
            "income_statement": stock.financials,
            "balance_sheet": stock.balance_sheet,
            "cashflow_statement": stock.cashflow
        }
        if any(df.empty for df in financials.values()):
            logging.warning(f"Financial statements for {ticker} are empty.")
            return None
        
        logging.info(f"Successfully extracted financial statements for {ticker}.")
        return financials
    
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error occurred: {e}")
        return None




if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "FB"]  # List of popular ticker symbols

    companies = {}
    for ticker in tickers:
        fin_stmts = get_financial_statements(ticker)
        companies[ticker] = fin_stmts
        

        
