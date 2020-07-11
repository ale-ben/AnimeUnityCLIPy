import colorama

import logging_aux


@logging_aux.logger_wraps()
def print_anime_list(search_res, lev=1):
    colorama.init()
    if not isinstance(search_res, type([])):
        search_res = [search_res]
    for res in search_res:
        if lev >= 1:
            title = f"{colorama.Fore.BLUE} {str(res['id'])}"
            if res['type'] != 'TV':
                title = f"{title} {colorama.Fore.CYAN} {res['type']}"
                if int(res['episodes_length']) > 50 and res['type'] != 'Movie':
                    title = f"{title}(Movie)"
            title = f"{title} {colorama.Fore.GREEN} {res['title']} {colorama.Style.RESET_ALL}"
            print(title)
            print(
                f"year: {res['date']}\t Episodes: {res['episodes_count']}\t Episode length: {res['episodes_length']} minutes")
        if lev >= 2:
            print("Episodes: ")
            for episode in res['episodes']:
                print(episode['link'])