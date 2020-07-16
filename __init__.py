"""Interazione con AnimeUnity e manipolazione dati

Modules:
common_classes -- classi usate per creare vari oggetti (Anime, Episodi, ...)
jdownloader -- funzioni usate per creare e formattare file crawljob (File usato da jdownloader per auto avviare download)
json_parser -- funzioni usate per manipolare e convertire json
logging_aux -- funzioni ausiliarie per il logging
res_obj_manipulator -- funzioni necessarie per convertire dizionari in classe Anime e formattare i risultati
scraper -- funzioni necessarie per ottenere i json richiesti dal sito
"""
__all__ = ["scraper", "logging_aux", "res_obj_manipulator", "jdownloader", "common_classes"]
