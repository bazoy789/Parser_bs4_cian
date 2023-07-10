from bs4 import BeautifulSoup
import requests
from random import randint
import time


def parser():
    html_doc = requests.get("https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/")

    soup = BeautifulSoup(html_doc.text, "html.parser")

    title = soup.find_all("a", "_93444fe79c--media--9P6wN")

    for i in title:
        with open("cian_href.html", "a", encoding="UTF-8") as file:
            file.write(i.get("href") + " 1" + "\n")

    for t in range(2, 6):
        url = requests.get(f"https://www.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&p={t}&region=1&room1=1&room2=1&type=4")
        soup_2 = BeautifulSoup(url.text, "html.parser")
        title_2 = soup_2.find_all("a", "_93444fe79c--media--9P6wN")

        for list_2 in title_2:
            with open("cian_href.html", "a", encoding="UTF-8") as file:
                file.write(list_2.get("href") + f" {t}" + "\n")
        time.sleep(randint(1, 3))


def get_data():
    with open("cian_href.html", encoding="UTF-8") as file:
        w = file.readlines()
    data_cian = {}
    for r in w[:10]:
        href = r.split(' ')[0]
        req = requests.get(href)
        soup = BeautifulSoup(req.text, "html.parser")

        name_flat = soup.find("h1", "a10a3f92e9--title--vlZwT").text
        price = soup.find("div", "a10a3f92e9--amount--ON6i1").text
        title = soup.find_all("li", "a10a3f92e9--underground--pjGNr")
        metro = []
        for t in title:
            metro.append(f"{t.find('a').text} - {t.find('span').text}")

        data_cian[f"{name_flat}"] = {
            "Цена": price,
            "Метро": metro
        }
    for k in data_cian.items():
        print(k)


def main():
    parser()
    get_data()


if __name__ == "__main__":
    main()

