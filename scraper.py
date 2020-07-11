import cloudscraper
from bs4 import BeautifulSoup

import logging_aux


@logging_aux.logger_wraps()
def search(title="false", type="false", year="false", order="false", status="false", genres="false", offset=0):
    scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
    payload = {"title": title, "type": type, "year": year, "order": order, "status": status, "genres": genres,
               "offset": offset}

    page = scraper.get("https://animeunity.it/archivio", params=payload)
    soup = BeautifulSoup(page.content, 'html.parser')
    anime_json = soup.find('archivio')['records']
    return anime_json
