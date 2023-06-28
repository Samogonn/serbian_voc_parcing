import requests
import csv
from bs4 import BeautifulSoup
from googletrans import Translator

# url = 'https://3000mostcommonwords.com/list-of-3000-most-common-serbian-words-in-english/'

# headers = {
#     'accept': '*/*',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
# }

# req = requests.get(url, headers=headers)

# src = req.text

# with open('serbian_vocabulary.html', 'w', encoding='utf-8') as file:
#     file.write(src)

with open("serbian_vocabulary.html", "r", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

# create headings

with open("serbian_vacabulary.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(("#", "English/Russian", "POS", "Level", "Serbian"))

all_row = soup.find(class_="row-hover").find_all("tr")

# fill the table

for row in all_row:
    params = row.find_all("td")

    number = params[0].text.strip('"')
    eng = params[1].text.strip('"')
    pos = params[2].text.strip('"')
    lev = params[3].text.strip('"')
    ser = params[4].text.strip('"')

    if ser == "":
        continue

    translator = Translator()
    rus = translator.translate(ser, src="sr", dest="ru").text

    with open("serbian_vacabulary.csv", "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow((number, f"{eng} / {rus}", pos, lev, ser))
