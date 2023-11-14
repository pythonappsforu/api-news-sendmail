from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("NEWS_API_Key")
url = f"https://newsapi.org/v2/everything?q=Ashok Leyland&from=2023-11-1&sortBy=popularity&apiKey={API_KEY}"

response = requests.get(url=url)
content = response.json()

articles = content['articles']
for article in articles:
    print(article['title'])

