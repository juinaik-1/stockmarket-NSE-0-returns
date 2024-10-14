
# Daily Stock Scanner
This project implements a daily stock scanner that identifies stocks listed on the National Stock Exchange of India (NSE) which have delivered approximately 0% returns over the last 7 years. The scanner is dynamic, allowing users to adjust the return and timeframe parameters.

## Dataset
The stock data is sourced from the National Stock Exchange of India (NSE). The CSV file containing the list of stocks can be downloaded from ![NSE Equity Archive](https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv)

## Features

- Analyzes stocks listed in the provided NSElist.csv file.
- Identifies stocks that have delivered returns close to 0% over the last 7 years.
- Allows for dynamic adjustment of return and timeframe parameters.



## Requirements

    Python 3.x
    pandas
    yfinance
## Run Locally

Clone the project

```bash
  git clone https://github.com/juinaik-1/stockmarket-NSE-0-returns
```

Go to the project directory

```bash
  cd stockmarket-NSE-0-returns
```

Install dependencies

```bash
  pip install pandas yfinance
```

Execute the script in python environment

```bash
  python stockscanner.py

```

