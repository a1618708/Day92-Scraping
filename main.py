from bs4 import BeautifulSoup
import requests
from datetime import date
import csv

para = {
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}


response = requests.get("https://icook.tw/categories/634", headers=para)

soup = BeautifulSoup(response.text, "html.parser")
recipe_name = soup.find_all(class_="browse-recipe-name")
recipe_ingredient = soup.find_all(class_="browse-recipe-content-ingredient")
recipe_link = soup.find_all(class_="browse-recipe-link")

recipe_name = [name.string.strip() for name in recipe_name]
recipe_ingredient = [ingredient.string.strip().split("食材：")[1] for ingredient in recipe_ingredient]
recipe_link = [f'https://icook.tw{link.get("href")}' for link in recipe_link]
print(recipe_name)
print(recipe_ingredient)
print(recipe_link)


today = date.today()
today = today.strftime('%Y%m%d')
print(today)
with open(f"recipe_{today}.csv","w",encoding='utf-8-sig',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["料理名", "食材", "料理連結"])
    for i in range(len(recipe_name)):
        writer.writerow([recipe_name[i].replace("\n",""),recipe_ingredient[i].replace("\n",""),recipe_link[i]])
    file.close()