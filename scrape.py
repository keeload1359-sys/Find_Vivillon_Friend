import requests
from bs4 import BeautifulSoup
import re
from filter import within_15minutes

def scrape_latest_codes():
    url = "https://www.pokemon-friends.eu/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text,"html.parser")
    title = soup.find(lambda tag: tag.name == "h2" and "LATEST CODES" in tag.text)
    table = title.find_next("table")
    row = table.find_all("tr")

    posts = []

    for i in row[1:]:
        tds = i.find_all("td")
        trainer_code = tds[0].contents[0].strip()
        time = tds[0].find("span").text.strip()
        country = tds[1].find("img").get("alt")
        vivillon = tds[2].find("img").get("alt")

        if within_15minutes(time):

            post = {
                "trainer_code": trainer_code,
                "time": time,
                "country": country,
                "vivillon": vivillon
            }

            posts.append(post)

    return posts

