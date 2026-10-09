import pandas as pd
import requests
from bs4 import BeautifulSoup
response = requests.get("https://books.toscrape.com/")
print(response)

soup = BeautifulSoup(response.content,'html.parser')
print(soup)

names = soup.find_all('p',class_ = "price_color")
print(names)

image = soup.find_all('img')
print(image)

images = []
for i in image[0:10]:
  result = i['src']
  images.append(result)
print(images)
result =[]
for i in names[0:10]:
  result.append(i.get_text(strip=True))
print(result)

price = [result.replace('£','') for result in result]
print(price)

df = pd.DataFrame()
df['Price']= price
df['images']= images

print(df)

df.to_csv("booksinfo.csv")