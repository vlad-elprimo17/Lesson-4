import requests
import sqlite3
from bs4 import BeautifulSoup


connection = sqlite3.connect('itstep.db', 5) # Під'єднує базу даних
cur = connection.cursor() # Під'єднує курсор
cur.execute("CREATE TABLE IF NOT EXISTS books (name TEXT, price TEXT)") # Створюємо таблицю якщо немає

r = requests.get("https://books.toscrape.com/")
text = r.text

print(text)

soup = BeautifulSoup(text, "html.parser")
books = soup.find_all("p", class_="price_color")
stock = soup.find_all(<p class="instock availability">)
name = soup.find_all(<a href="../../../full-moon-over-noahs-ark-an-odyssey-to-mount-ararat-and-beyond_811/index.html" title="Full Moon over Noah’s Ark: An Odyssey to Mount Ararat and Beyond">Full Moon over Noah’s ...</a>
star-rating = soup.find_all(<p class="star-rating Four">



for b in books:
    print(b.text)