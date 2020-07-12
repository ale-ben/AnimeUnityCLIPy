import colorama

import logging_aux

"""
Print mode levels:
1) Print only anime info
2) Print 1 and episode list
"""


@logging_aux.logger_wraps()
def print_anime_list(search_res, config, print_mode):
    colorama.init()
    if not isinstance(search_res, type([])):
        search_res = [search_res]
    for res in search_res:
        if print_mode >= 1 and config['print_level'] >= 1:
            title = f"{colorama.Fore.BLUE} {str(res['id'])}"
            if res['type'] != 'TV':
                title = f"{title} {colorama.Fore.CYAN} {res['type']}"
                if int(res['episodes_length']) > 50 and res['type'] != 'Movie':
                    title = f"{title}(Movie)"
            title = f"{title} {colorama.Fore.GREEN} {res['title']}{('{} ({})'.format(colorama.Fore.CYAN, res['title_eng']), '')[res['title_eng'] is None]} {colorama.Style.RESET_ALL}"
            print(title)
            print(
                f"year: {res['date']}\t Episodes: {res['episodes_count']}\t Episode length: {res['episodes_length']} minutes")
        if print_mode >= 2 and config['print_level'] >= 2:
            print("Episodes: ")
            for episode in res['episodes']:
                print(episode['link'])
