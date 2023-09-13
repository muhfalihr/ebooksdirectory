from .utility import wov, soup
from .kategori import Categories
import requests
from bs4 import BeautifulSoup
import json


def takeHref(links):
    try:
        linkhref = ['http://www.e-booksdirectory.com/' + a['href'] for item in soup(
            links) for article in item.find_all('article', 'img_list') for a in article.find_all('a')]
    except:
        linkhref = ['http://www.e-booksdirectory.com/' + a['href'] for link in links if link != '' for item in soup(
            link) for article in item.find_all('article', 'img_list') for a in article.find_all('a')]
    return linkhref


def takeLinkCategories():
    link = 'http://www.e-booksdirectory.com/'
    items = soup(link)

    kategori = Categories(items)

    clText = kategori.cat_largeText()
    clLink = kategori.cat_largeLink()
    csLink = kategori.cat_smallLink()

    all_categories = []
    for i in range(len(clText)):
        data = takeHref(clLink[i]) + takeHref(csLink[i])
        all_categories.append(data)

        dumps = json.dumps(all_categories, indent=4)

        try:
            with open('links.json', 'w') as file:
                file.write(dumps)
        except:
            with open('links.json', 'r+') as file:
                file.write(dumps)


def takeNTP(page: int, option: str):
    '''page = Berapa page yang akan anda ambil linknya, option = (new, top, popular) pilihan page yang akan anda ambil linknya. (Defaultnya New)'''
    user_agent = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

    url = 'http://www.e-booksdirectory.com/new.php' if option.lower() == 'new' else ('http://www.e-booksdirectory.com/top20.php' if option.lower()
                                                                                     == 'top' else ('http://www.e-booksdirectory.com/popular.php' if option.lower() == 'popular' else 'http://www.e-booksdirectory.com/new.php'))
    resp = requests.get(url, headers=user_agent)

    soup = BeautifulSoup(resp.text, 'lxml')

    items = soup.find_all('article', 'img_list')

    hrefLinks = []
    [hrefLinks.append('http://www.e-booksdirectory.com/'+a['href'])
     for item in items for a in item.find_all('a')]

    if page < 1:
        return ['']

    num = 0
    for i in range(page-1):
        data = {
            'submit': 'Next',
            'startid': f'{0+num}'
        }

        response = requests.post(url, data=data)

        soup = BeautifulSoup(response.text, 'html.parser')

        items = soup.find_all('article', 'img_list')

        [hrefLinks.append('http://www.e-booksdirectory.com/'+a['href'])
         for item in items for a in item.find_all('a')]
        num += 20

    return hrefLinks
