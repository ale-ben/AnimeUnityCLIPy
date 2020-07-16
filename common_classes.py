"""Common classes."""

from loguru import logger
import colorama


class Episode:
    """Episode class."""

    e_id = None
    num = None
    air_date = None
    link = None

    def __init__(self, e_id, num, air_date, link):
        """
        Episode class initializer.

        Keyword arguments:
        e_id -- episode id
        num -- numero dell'episodio
        air_date -- -.- data di uscita
        link -- url dell'episodio
        """
        logger.debug(f"Creating episode obj (id: {e_id}, num: {num})")
        self.e_id = e_id
        self.num = num
        self.air_date = air_date
        self.link = link

    def __repr__(self):
        """Rappresentazione di un episodio: episode id-episode number-air date."""
        return f"{self.e_id}-{self.num}-{self.air_date}"

    def __str__(self):
        """To string di un episodio: url."""
        return self.link


class Related:
    """Anime related class."""

    a_id = None
    a_type = None
    title = None
    slug = None

    def __init__(self, a_id, a_type, title, slug):
        """
        Anime related class initializer.

        Keyword arguments:
        a_id -- Anime id
        a_type -- v
        title -- Titolo
        slug -- Titolo formattato
        """
        self.a_id = a_id
        self.a_type = a_type
        self.title = title
        self.slug = slug

    def __repr__(self):
        """Rappresentazione di un anime collegato: anime id-anime title."""
        return f"{self.a_id}-{self.title}"

    def get_anime_url(self):
        """Combine the anime id and the slug to get the URL."""
        return f"https://animeunity.it/anime/{self.a_id}-{self.slug}"


class Anime:
    """Anime class."""

    a_id = None
    title = None
    title_eng = None
    thumbnail = None
    cover_image = None
    status = None
    a_type = None
    slug = None
    year = None
    episodes = None
    episodes_length = None
    related = None

    def __init__(self, a_id, title, a_type, episodes_length):
        """
        Anime class initializer.

        Keyword arguments:
        a_id -- Anime id
        title -- Titolo
        a_type -- Tipo anime (TV,OVA,ONA,Movie,Special)
        episode_length -- Lunghezza media di un episodio
        """
        logger.debug(f"Creating Anime obj (id: {a_id}, num: {title})")
        self.a_id = a_id
        self.title = title
        self.episodes_length = episodes_length
        # Se è OVA o ONA e dura più di 50 min lo converto in film
        if int(self.episodes_length) > 50 and (a_type == 'OVA' or a_type == 'ONA'):
            self.a_type = 'Movie'
        else:
            self.a_type = a_type

    def __repr__(self):
        """Rappresentazione di un anime: anime id-anime title."""
        return f"{self.a_id}-{self.title}"

    def __str__(self):
        """To String di un anime: Anime id [a_type] title."""
        title = f"{colorama.Fore.BLUE} {str(self.a_id)}"
        if self.a_type != 'TV':
            title = f"{title} {colorama.Fore.CYAN} {self.a_type}"
        return f"{title} {colorama.Fore.GREEN} {self.title}{('{} ({})'.format(colorama.Fore.CYAN, self.title_eng), '')[self.title_eng is None]} {colorama.Style.RESET_ALL}"

    def get_anime_url(self):
        """Combine the anime id and the slug to get the URL."""
        return f"https://animeunity.it/anime/{self.a_id}-{self.slug}"
