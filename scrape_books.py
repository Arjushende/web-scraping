import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

data = []

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text

    # This must be INSIDE the loop
    data.append({
        "Title": title,
        "Price": price
    })

print(data)

df = pd.DataFrame(data)

print(df)

# Fixes the £ symbol in Excel
df.to_csv("books.csv", index=False, encoding="utf-8-sig")

print("CSV file created successfully!")