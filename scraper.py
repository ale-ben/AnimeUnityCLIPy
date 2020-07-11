import cloudscraper
from bs4 import BeautifulSoup

import logging_aux
import res_obj_manipulator
import json_parser


@logging_aux.logger_wraps()
def search(title="false", type="false", year="false", order="false", status="false", genres="false", offset=0):
    scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
    payload = {"title": title, "type": type, "year": year, "order": order, "status": status, "genres": genres,
               "offset": offset}

    page = scraper.get("https://animeunity.it/archivio", params=payload)
    soup = BeautifulSoup(page.content, 'html.parser')
    anime_json = soup.find('archivio')['records']
    return res_obj_manipulator.order_search_res(
        res_obj_manipulator.get_formatted_search_results(json_parser.decode_json(anime_json)))


def anime_page_scraper(url):
    scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
    page = scraper.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    anime_info = soup.find('video-player')
    anime_json = anime_info['anime']
    anime_obj = res_obj_manipulator.order_search_res(
        res_obj_manipulator.get_formatted_search_results([json_parser.decode_json(anime_json)]))
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
            if ('ALL' in season) or ('OVA' in season and anime_elem['type'] == 'OVA') or (
                    'ONA' in season and anime_elem['type'] == 'ONA') or (
                    'Movie' in season and anime_elem['type'] == 'Movie') or (
                    'Special' in season and anime_elem['type'] == 'Special'):
                anime_list.append(anime_elem)
        return anime_list
