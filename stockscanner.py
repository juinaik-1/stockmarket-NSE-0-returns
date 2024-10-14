#Develop a scanner that will run daily after market close to identify stocks that have delivered 0% returns in the last 7 years. The scanner should be dynamic, allowing for the adjustment of return and timeframe parameters.

#dataset downloaded from https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv

import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# Function to read CSV file and return a DataFrame
def read_csv(file_path):
    return pd.read_csv(file_path)

# Function to fetch historical data for multiple stock symbols
def fetch_historical_data(stock_symbols, start_date, end_date):
    try:
        # Download data and handle potential errors
        historical_data = yf.download(stock_symbols, start=start_date, end=end_date)['Close']
        return historical_data
    except Exception as e:
        print(f"Error fetching data for {stock_symbols}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

# Function to calculate returns for multiple stocks
def calculate_returns(prices):
    returns = {}
    for symbol in prices.columns:
        initial_price = prices[symbol].iloc[0]
        current_price = prices[symbol].iloc[-1]

        # Check if initial_price or current_price is NaN
        if pd.isna(initial_price) or pd.isna(current_price):
            returns[symbol] = float('nan')  # Mark as NaN if data is missing
            continue

        returns[symbol] = (current_price - initial_price) / initial_price * 100
    return returns

# Main scanning function
def scan_stocks(file_path, return_threshold=0, years=7):
    df = read_csv(file_path)

    if 'SYMBOL' not in df.columns:
        raise ValueError("CSV must contain a 'SYMBOL' column.")

    stock_symbols = df['SYMBOL'].tolist()
    
    start_date = (datetime.now() - pd.DateOffset(years=years)).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')

    # Fetch historical data for all stocks at once
    historical_prices = fetch_historical_data([f"{symbol}.NS" for symbol in stock_symbols], start_date, end_date)

    # Calculate returns
    stock_returns = calculate_returns(historical_prices)

    # Filter stocks based on return threshold
    results = {symbol: ret for symbol, ret in stock_returns.items() if pd.notna(ret) and abs(ret) < return_threshold + 0.9}

    return results

# Example usage
if __name__ == "__main__":
    file_path = 'NSElist.csv'  # Path to your CSV file
    print("Scanning for NSE stocks with approximately 0% returns over the last 7 years...")
    
    stocks_with_zero_return = scan_stocks(file_path)
    
    if stocks_with_zero_return:
        print("Stocks with approximately 0% returns:")
        for stock, ret in stocks_with_zero_return.items():
            print(f"{stock}: {ret:.2f}%")
    else:
        print("No stocks found with approximately 0% returns.")

#output:
# Scanning for NSE stocks with approximately 0% returns over the last 7 years...
# [*********************100%***********************]  2022 of 2022 completed

# 2 Failed downloads:
# ['KALYANI.NS', 'MITTAL-RE1.NS']: YFPricesMissingError('$%ticker%: possibly delisted; no price data found  (1d 2017-10-14 -> 2024-10-14)')
# Stocks with approximately 0% returns:
# FLEXITUFF.NS: -0.41%
# SIL.NS: -0.53%
# WHEELS.NS: 0.77%