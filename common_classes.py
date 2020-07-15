from loguru import logger
import colorama


class Episode:
    e_id = None
    num = None
    air_date = None
    link = None

    def __init__(self, e_id, num, air_date, link):
        logger.debug(f"Creating episode obj (id: {e_id}, num: {num})")
        self.e_id = e_id
        self.num = num
        self.air_date = air_date
        self.link = link

    def __repr__(self):
        return f"{self.e_id}-{self.num}"

    def __str__(self):
        return self.link


class Related:
    a_id = None
    type = None
    title = None
    slug = None

    def __init__(self, a_id, type, title, slug):
        self.a_id = a_id
        self.type = type
        self.title = title
        self.slug = slug

    def __repr__(self):
        return f"{self.a_id}-{self.title}"

    def get_anime_url(self):
        return f"https://animeunity.it/anime/{self.a_id}-{self.slug}"


class Anime:
    a_id = None
    title = None
    title_eng = None
    thumbnail = None
    cover_image = None
    status = None
    type = None
    slug = None
    year = None
    episodes = []
    episodes_length = None
    related = []

    def __init__(self, a_id, title, type, episodes_length):
        logger.debug(f"Creating Anime obj (id: {a_id}, num: {title})")
        self.a_id = a_id
        self.title = title
        self.episodes_length = episodes_length
        # Se è OVA o ONA e dura più di 50 min lo converto in film
        if int(self.episodes_length) > 50 and (type == 'OVA' or type == 'ONA'):
            self.type = 'Movie'
        else:
            self.type = type

    def __repr__(self):
        return f"{self.a_id}-{self.title}"

    def __str__(self):
        title = f"{colorama.Fore.BLUE} {str(self.a_id)}"
        if self.type != 'TV':
            title = f"{title} {colorama.Fore.CYAN} {self.type}"
        return f"{title} {colorama.Fore.GREEN} {self.title}{('{} ({})'.format(colorama.Fore.CYAN, self.title_eng), '')[self.title_eng is None]} {colorama.Style.RESET_ALL}"

    def get_anime_url(self):
        return f"https://animeunity.it/anime/{self.a_id}-{self.slug}"
