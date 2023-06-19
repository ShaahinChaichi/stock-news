import requests
import unicodedata

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ACCESS_KEY = "MO5LQIYP48RPIBR5"

NEWS_API_KEY = "c4bd24d75f7f431ca448b03ab4755bbc"
NEWS_PARAMS = {
    "qInTitle": "tesla",
    "apiKey": NEWS_API_KEY
}

# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo

params = {"function": "TIME_SERIES_DAILY_ADJUSTED",
          "symbol": "IBM",
          "apikey": ACCESS_KEY,
          }

response = requests.get(STOCK_ENDPOINT, params=params)
data = response.json()

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday
# then print("Get News").

# stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
time_series_price = data['Time Series (Daily)']
data_list = [item for (key, item) in time_series_price.items()]
yesterday_closing_price = data_list[0]["4. close"]
day_before_yesterday_closing_price = data_list[1]["4. close"]
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
diff_percent = (difference / float(yesterday_closing_price)) * 100

# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
# Use Python slice operator to create a list that contains the first 3 articles. Hint:
# https://stackoverflow.com/questions/509211/understanding-slice-notation


response = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMS)
articles = response.json()["articles"]
three_article = articles[:3]

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
three_article_headline = [article["title"] for article in three_article]


# TODO 9. - Send each article as a separate message via Twilio.
for article_headline in three_article_headline:
    print(article_headline)

# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
