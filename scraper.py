import cloudscraper
from bs4 import BeautifulSoup
from pathlib import Path

import logging_aux
import res_obj_manipulator
import json_parser

file_log = False
base_path = Path('./doc/templates')
defined_anime_types = ['TV','OVA','ONA','Movie','Special']


@logging_aux.logger_wraps()
def search(title="false", type="false", year="false", order="false", status="false", genres="false", offset=0):

    scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
    payload = {"title": title, "type": type, "year": year, "order": order, "status": status, "genres": genres,
               "offset": offset}

    page = scraper.get("https://animeunity.it/archivio", params=payload)
    with open(f'{base_path / "search_scraped"}.html', 'w') as f:
        f.write(page.text)
        f.close()
    soup = BeautifulSoup(page.content, 'html.parser')
    with open(f'{base_path / "search_souped"}.html', 'w') as f:
        f.write(soup.prettify())
        f.close()
    anime_json = soup.find('archivio')['records']
    with open(f'{base_path / "search_result"}.json', 'w') as f:
        f.write(anime_json)
        f.close()
    search_obj = res_obj_manipulator.order_search_res(
        res_obj_manipulator.get_formatted_search_results(json_parser.decode_json(anime_json)))
    if file_log:
        with open(f'{base_path / "search_result_final"}.json', 'w') as f:
            f.write(json_parser.encode_json(search_obj))
            f.close()
    return search_obj

def anime_page_scraper(url):
    scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
    page = scraper.get(url)
    if file_log:
        with open(f'{base_path / "anime_page_scraped"}.html', 'w') as f:
            f.write(page.text)
            f.close()
    soup = BeautifulSoup(page.content, 'html.parser')
    if file_log:
        with open(f'{base_path / "anime_page_souped"}.html', 'w') as f:
            f.write(soup.prettify())
            f.close()
    anime_info = soup.find('video-player')
    anime_json = anime_info['anime']
    if file_log:
        with open(f'{base_path / "anime_page_results"}.json', 'w') as f:
            f.write(anime_json)
            f.close()
    anime_obj = res_obj_manipulator.order_search_res(
        res_obj_manipulator.get_formatted_search_results([json_parser.decode_json(anime_json)]))
    if file_log:
        with open(f'{base_path / "anime_page_final"}.json', 'w') as f:
            f.write(json_parser.encode_json(anime_obj))
            f.close()
    return anime_obj[0]


def season_scraper(anime, season=None):
    if season is not None:
        base_url = 'https://animeunity.it/anime/'
        anime_url = f"{base_url}{anime['id']}-{anime['slug']}"
        scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
        page = scraper.get(anime_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        related = soup.find_all('a', class_="unstile-a")
        anime_list = []
        anime_url = [anime_url]
        for el in related:
            anime_url.append(el['href'])
        for url in anime_url:
            anime_elem = anime_page_scraper(url)
            if ('ALL' in season) or (anime_elem['type'] in season):
                anime_list.append(anime_elem)
        return anime_list