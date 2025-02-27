**Stock Portfolio Tracker**

A simple tool to track the value of a stock portfolio using Python and yfinance. This project fetches real-time stock prices, calculates key portfolio metrics, and visualizes performance trends with plots.

**Features:**
- Fetches live stock data using yfinance
- Calculates portfolio value dynamically based on holdings
- Computes key portfolio metrics:
   > Expected Annual Return,
   > Portfolio Volatility,
   > Sharpe Ratio
- Plots portfolio value trends over time
  
**Installation & Usage**

1. Install Dependencies
   
First, install the required Python libraries:

pip install pandas yfinance matplotlib numpy

2. Run the Script
   
Run the script to fetch stock prices, calculate metrics, and generate reports:

python portfolio_tracker.py

3. View the Report
   
Once the script runs, you will be able to view:

- Portfolio Value & Holdings
- Performance Metrics
- Stock Price & Portfolio Trends (Graph)

**Example Stocks Used**

This project works with stocks from multiple exchanges. You can track:

USA Stocks: AAPL, TSLA, MSFT

Indian Stocks: RELIANCE.NS, INFY.NS, DECNGOLD.BO
(Use .NS for NSE and .BO for BSE stocks in India)

**Simply modify the stock symbols in the Python script to track your custom portfolio!** 
