import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Alpha Vantage API configuration
AV_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": AV_API_KEY
}

# Fetch stock data
try:
    stocks_raw = requests.get("https://www.alphavantage.co/query", params=parameter)
    stocks_raw.raise_for_status()
    stock_data = stocks_raw.json()["Time Series (Daily)"]
    # Get yesterday and day before data
    dates = list(stock_data.keys())
    yesterday = float(stock_data[dates[0]]["2. high"])
    day_before = float(stock_data[dates[1]]["2. high"])
    change = ((yesterday - day_before) / day_before) * 100

    # Check for significant change
    if abs(change) >= 5:
        print("Get News")  # Placeholder
except KeyError:
    print("Error in retrieving stock data.")

# NewsAPI configuration
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
article_params = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
    "language": "en",
    "sortBy": "publishedAt",
    "pageSize": 3
}

# Fetch news
try:
    news_response = requests.get("https://newsapi.org/v2/everything", params=article_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"][:3]

    for article in articles:
        title = article["title"]
        print(f"Headline: {title}")

except KeyError:
    print("Error in retrieving news data.")
