# stock-news
This Stock Price Monitor tracks Tesla's stock price (TSLA) and alerts you to significant price changes (5%+), fetching related news via the NewsAPI.

# Stock Price Monitor

## Description
The Stock Price Monitor tracks the daily price of a specified stock, in this case, **Tesla Inc (TSLA)**. It uses the **Alpha Vantage API** to fetch real-time stock data and checks if the price changes by 5% or more compared to the previous day. If a significant change is detected, it fetches the latest news articles about the company using the **NewsAPI**.

## Features
- Fetches daily stock data from Alpha Vantage API.
- Monitors the price change of the stock and identifies significant changes (5% or more).
- Retrieves the latest news articles related to the company using the NewsAPI.
- Displays the latest headlines if a significant price change is detected.

## Requirements
- Python 3.x
- **requests** library
- **python-dotenv** library for environment variables

## Setup
1. Install the required dependencies:
   ```bash
   pip install requests python-dotenv
