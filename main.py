import getopt
import sys
from loguru import logger
import colorama

import scraper
import json_parser
import res_obj_manipulator
import printer
import logging_aux
import jdownloader

crawl_path = None
download_path = None
no_print=False


@logging_aux.logger_wraps()
def main():
    logging_aux.init_logger(level="INFO", file_log=True)
    if len(sys.argv) == 1:
        keyword = interactive_mode()
    else:
        keyword = cli_mode()
    logger.debug("Keyword selected: {}".format(keyword))
    anime_json = scraper.search(title=keyword)
    logger.debug("search json: {}".format(anime_json))
    search_res = res_obj_manipulator.get_formatted_search_results(json_parser.decode_json(anime_json))
    logger.debug("search results: {}".format(search_res))
    if not search_res:
        print(f"{colorama.Fore.RED}No Anime Found{colorama.Style.RESET_ALL}")
        logger.debug("No anime found, keyword: {}".format(keyword))
        exit(1)
    logger.debug("Printing anime list")
    printer.print_search_results(res_obj_manipulator.order_search_res(search_res))
    anime_id = input("ID: ")
    logger.debug("ID selected: {}".format(anime_id))
    selected = res_obj_manipulator.get_selected_anime_obj_by_id(search_res, anime_id)
    logger.debug("Anime selected: {}".format(selected))
    logger.debug("Printing anime episodes")
    if not no_print:
        printer.print_selected_anime_episodes(selected)

    jdownloader.send_to_jdownloader([selected], crawl_path=crawl_path, jdownload_path=download_path)


@logging_aux.logger_wraps()
def cli_mode():
    keyword = None
    global crawl_path
    global download_path
    global no_print

    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, 'k:jdp:', ['no_print', 'keyword=', 'crawlpath=', 'jdownloadpath='])
    except getopt.GetoptError:
        # stampa l'informazione di aiuto ed esce:
        # usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ['-k', '--keyword']:
            keyword = arg
        if opt in ['-jdp', '--jdownloadpath']:
            download_path = arg
        if opt in ['--crawlpath']:
            crawl_path = arg
        if opt in ['--noprint']:
            no_print = True

    return keyword


@logging_aux.logger_wraps()
def interactive_mode():
    keyword = input("Keyword: ")
    return keyword


if __name__ == "__main__":
    main()
