import requests
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCKAPI_KEY = 'X5O8OWUHLP45ZFSL'
NEWSAPI_KEY = 'f0f38211cbf54d2eaa0c5923533c701d'
TWILIO_ACC_SID = 'AC73579c48594404ba2eb6e494efa9a8f2'
TWILIO_AUTH_TOKEN = 'b6e91a5635c18243f0d7229757042bb3'
TWILIO_PHONE_NUM = '+15673339814'
MY_NUM = '+358468909804'

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    'function': 'TIME_SERIES_MONTHLY',
    'symbol': STOCK_NAME,
    'apikey': STOCKAPI_KEY
}

r = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = r.json()['Monthly Time Series']
data_list = [value for (key, value) in stock_data.items()]

last_month = data_list[0]
last_month_closing_prise = last_month['4. close']

previous_month = data_list[1]
previous_mount_closing_prise = previous_month['4. close']

difference = abs(float(last_month_closing_prise) - float(previous_mount_closing_prise))

dif_percent = (difference/float(last_month_closing_prise)) * 100
print(dif_percent)

if dif_percent > 4:
    news_params = {
        'qInTitle': COMPANY_NAME,
        'apiKey': NEWSAPI_KEY
    }
    
    news_data = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_data.json()['articles']
    three_articles = articles[:3]
    print(three_articles)
    articles_list = [f'Headline: {article["title"]}. \nBrief: {article["description"]}' for article in three_articles]
    print(articles_list)
    
    client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)
    for article in articles_list:
        message = client.messages.create(
            body=article,
            from_=TWILIO_PHONE_NUM,
            to=MY_NUM
        )



#TODO 9. - Send each article as a separate message via Twilio.



#Optional TODO: Format the message like this:
"""
TSLA: 🔺🔻2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

