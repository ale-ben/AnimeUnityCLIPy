import colorama


def print_search_results(search_res):
    colorama.init()
    for res in search_res:
        title = f"{colorama.Fore.BLUE} {str(res['id'])}"
        if res['type'] != 'TV':
            title = f"{title} {colorama.Fore.CYAN} {res['type']}"
            if int(res['episodes_length'])>50 and res['type'] != 'Movie':
                title = f"{title}(Movie)"
        title = f"{title} {colorama.Fore.GREEN} {res['title']} {colorama.Style.RESET_ALL}"
        print(title)
        print(f"year: {res['date']}\t Episodes: {res['episodes_count']}\t Episode length: {res['episodes_length']} minutes")


def print_selected_anime_episodes(selected_anime):
    colorama.init()
    title = f"{colorama.Fore.BLUE} {str(selected_anime['id'])}"
    if selected_anime['type'] != 'TV':
        title = f"{title} {colorama.Fore.CYAN} {selected_anime['type']}"
        if int(selected_anime['episodes_length']) > 50 and selected_anime['type'] != 'Movie':
            title = f"{title}(Movie)"
    title = f"{title} {colorama.Fore.GREEN} {selected_anime['title']} {colorama.Style.RESET_ALL}"
    print(title)
    print(f"year: {selected_anime['date']}\t Episodes: {selected_anime['episodes_count']}\t Episode length: {selected_anime['episodes_length']} minutes")
    print("Episodes: ")
    for episode in selected_anime['episodes']:
        print(episode['link'])