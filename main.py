import scraper
import json_parser
import res_obj_manipulator
import printer


def main():
    keyword = input("Keyword: ")
    anime_json = scraper.search(title=keyword)
    search_res = res_obj_manipulator.get_formatted_search_results(json_parser.decode_json(anime_json))
    # search_res = json_parser.encode_json(search_res)
    if not search_res:
        print("No Anime Found")
        exit(1)
    printer.print_search_results(search_res)
    anime_id = input("ID: ")
    selected = res_obj_manipulator.get_selected_anime_obj_by_id(search_res, anime_id)
    printer.print_selected_anime_episodes(selected)


if __name__ == "__main__":
    main()
