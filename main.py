from dotenv import load_dotenv
import os
import requests
from send_mail import send_mail

load_dotenv()

news_about = input("enter keyword to search :")
API_KEY = os.getenv("NEWS_API_Key")
url = (f"https://newsapi.org/v2/everything?q={news_about}&"
       f"from=2023-11-1&"
       f"sortBy=popularity&"
       f"apiKey={API_KEY}&language=en")

response = requests.get(url=url)
content = response.json()

articles = content['articles']
body = ''
for article in articles[:20]:
    body += (article['title'] + '\n' + article['description'] +
             '\n' + article['url'] + 2*'\n')

message = f"""Subject:{news_about} news articles\n
{body}
"""
send_mail(message.encode('utf-8'))