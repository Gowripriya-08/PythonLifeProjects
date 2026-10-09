import pandas as pd
import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com/?utm_source")
print(response)

soup = BeautifulSoup(response.content,'html.parser')
print(soup)

names = soup.find_all('small', class_ = "author")
print(names)

result = []
for i in names[0:10]:
    result.append(i.get_text(strip=True))
print(result)

df = pd.DataFrame()
df['Author'] = result

print(df)

df.to_csv("authors.csv")
