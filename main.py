import scraper
import json_parser

def main():
    anime_json = scraper.search(title="dxd")
    search_res = json_parser.get_formatted_search_results(json_parser.decode_json(anime_json))
    print(json_parser.encode_json(search_res))


if __name__ == "__main__":
    main()
