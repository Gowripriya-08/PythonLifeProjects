import pandas as pd
import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com/")
print(response)

soup = BeautifulSoup(response.content,'html.parser')
print(soup)

names = soup.find_all('img')
print(names)

result = []
for i in names[0:10]:
    result.append(i['src'])
print(result)

df = pd.DataFrame()
df['images'] = result
print(df)

df .to_csv("sports.csv")