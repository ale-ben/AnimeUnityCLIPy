import cloudscraper
from bs4 import BeautifulSoup
from pathlib import Path

from AnimeUnityEngine import logging_aux, res_obj_manipulator, json_parser, common_classes

file_log = False
base_path = Path('./doc/templates')
defined_anime_types = ['TV', 'OVA', 'ONA', 'Movie', 'Special']


@logging_aux.logger_wraps()
def search(title="false", type="false", year="false", order="false", status="false", genres="false", offset=0):
    scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
    payload = {"title": title, "type": type, "year": year, "order": order, "status": status, "genres": genres,
               "offset": offset}

    page = scraper.get("https://animeunity.it/archivio", params=payload)
    if file_log:
        with open(f'{base_path / "search_scraped"}.html', 'w') as f:
            f.write(page.text)
            f.close()

    soup = BeautifulSoup(page.content, 'html.parser')

    if file_log:
        with open(f'{base_path / "search_souped"}.html', 'w') as f:
            f.write(soup.prettify())
            f.close()

    anime_json = soup.find('archivio')['records']

    if file_log:
        with open(f'{base_path / "search_result"}.json', 'w') as f:
            f.write(anime_json)
            f.close()

    # Passo da json a dizionario e da dizionario a oggetto
    search_obj = res_obj_manipulator.get_formatted_search_results(json_parser.decode_json(anime_json))

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
    # JSON contenente tutto il necessario
    anime_json = anime_info['anime']

    if file_log:
        with open(f'{base_path / "anime_page_results"}.json', 'w') as f:
            f.write(anime_json)
            f.close()

    # Passo da json a dizionario e da dizionario a oggetto
    anime_obj = res_obj_manipulator.get_formatted_search_results(json_parser.decode_json(anime_json))

    if file_log:
        with open(f'{base_path / "anime_page_final"}.json', 'w') as f:
            f.write(json_parser.encode_json(anime_obj))
            f.close()

    return anime_obj[0]


def season_scraper(anime, config=None):
    if config['season'] is not None:
        # Per comodità converto l'array in elemento
        if not isinstance(anime, common_classes.Anime):
            anime = anime[0]

        anime = anime_page_scraper(anime.get_anime_url())

        print(config['season'])
        anime_list = []
        # Se l'anime è del tipo specificato lo appendo
        if ('ALL' in config['season']) or (anime.type in config['season']):
            anime_list.append(anime)

        for rel in anime.related:
            # Tra i related c'è spesso anche l'anime di partenza
            if rel.a_id == anime.a_id:
                continue
            # Se l'anime è del tipo specificato lo appendo
            if ('ALL' in config['season']) or (rel.type in config['season']):
                anime_elem = anime_page_scraper(rel.get_anime_url())
                anime_list.append(anime_elem)
        print(anime_list)
        return anime_list
