from bs4 import BeautifulSoup

import re
import urllib.request as ul
import wget
import os


def get_themes():
    """ Scraps data.gouv.fr to retrieve only most recent json data (not CSV)
    There is a little formatting at the end so the user can select which data
    she or he wants to download

    Returns
    -------
    themes: {theme: url}
        URL to data
    """

    url = 'https://www.data.gouv.fr/fr/datasets/donnees-ouvertes-du-grand-debat-national/'
    response = ul.urlopen(url,timeout=5)
    soup = BeautifulSoup(response, features="lxml")

    themes = {}
    i = 0
    for article in soup.find_all('article'):

        spans = article.find_all('li', attrs={'title':'Information du fichier'})
        json = False
        for span in spans:
            json = True if 'json' in str(span) else False

        if json:
            for a in article.find_all('h4', attrs={'class': 'ellipsis'}):
                if 'Contributions déposées' in a.text:
                    theme = re.sub('"', '', re.findall('".*"', a.text)[0])
                else:
                    break
            for a in article.find_all('a', href=True):
                link = a['href']

            if theme not in themes.keys(): # Keep only most recent files
                themes[theme] = link

    themes_clean = {}
    i = 1
    for theme, link in themes.items():
        themes_clean[str(i) + ' ' + theme] = link
        i += 1

    return themes_clean


def download_data(themes, selected_theme):
    """ Downloads data in `data` dir

    Parameters
    ----------
    themes: {theme: url}
        URL to data
    which_themes= [int]
        Themes to download
    """
    for theme, link in themes.items():
        if int(theme[0]) == selected_theme:
            if os.path.isfile('data/' + theme[2:] + '.json'):
                os.remove('data/' + theme[2:] + '.json')
            wget.download(link, 'data/' + theme[2:] + '.json')
            print('Données les plus récentes associées au thème ' + str(selected_theme) + ' sauvegardée à ' + 'data/' + theme[2:] + '.json')
