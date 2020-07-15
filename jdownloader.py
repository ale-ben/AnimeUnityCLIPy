from pathlib import Path

from AnimeUnityEngine import logging_aux


@logging_aux.logger_wraps()
def format_title(old_title):
    # Formatting the string
    new_title = str.capitalize(str.lower(old_title))

    replace_chars = [{'old': ' ', 'new': '_'}, {'old': '!', 'new': ''}, {'old': '?', 'new': ''},
                     {'old': ':', 'new': ''}, {'old': ',', 'new': ''}, {'old': '\'', 'new': ''}]
    for char in replace_chars:
        new_title = str.replace(new_title, char['old'], char['new'])

    return new_title


@logging_aux.logger_wraps()
def create_crawl_file(anime_page=None, crawl_path="", jdownload_path="", season=1):
    file_content = ""

    # Formatting the string
    formatted_anime_title = format_title(anime_page['slug'])
    crawl_file = Path(crawl_path) / formatted_anime_title

    # Creating the AnimeDir
    jdownloader_anime_path = Path(jdownload_path) / "Season_" / str(season)

    for ep in anime_page['episodes']:
        file_content = file_content + "{\n"
        file_content = f"{file_content}\ttext= {ep['link']}\n"
        file_content = f"{file_content}\tdownloadFolder= {jdownloader_anime_path}\n"
        file_content = f"{file_content}\tenabled= true\n"
        file_content = f"{file_content}\tautoStart= true\n"
        file_content = f"{file_content}\tautoConfirm= true\n"
        file_content = file_content + "}\n"

    with open(f'{crawl_file}.crawljob', 'w') as f:
        f.write(file_content)
        f.close()


@logging_aux.logger_wraps()
def send_to_jdownloader(anime_page_list=None, crawl_path="", jdownload_path=""):
    formatted_title = format_title(anime_page_list[0]['slug'])
    jdownload_path = Path(jdownload_path) / formatted_title

    season_num = 0

    for anime in anime_page_list:
        if anime['type'] == 'TV':
            season_num = season_num + 1
            create_crawl_file(anime, crawl_path, jdownload_path, season_num)
        else:
            create_crawl_file(anime, crawl_path, jdownload_path, 0)
