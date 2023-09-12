from bs4 import BeautifulSoup
import requests
from .downloader import download


class CrawlDetail:
    def __init__(self, link) -> None:
        self.__user_agent = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

        self.__link = link

        self.__resp = requests.get(self.__link, headers=self.__user_agent)

        self.__soup = BeautifulSoup(self.__resp.text, 'lxml')

        self.__items = self.__soup.find_all('section', 'main_content')

    def articles(self):
        return [article for item in self.__items for article in item.find_all('article')]

    def img(self):
        article = self.articles()
        return ''.join(['http://www.e-booksdirectory.com/'+img['src']
                        for img in article[1].find_all('img')])

    def title(self):
        article = self.articles()
        return ''.join([strong.text for strong in article[1].find_all(
            'strong', itemprop='name')])

    def author(self):
        article = self.articles()
        return ''.join([span.text for p in article[1].find_all('p') for span in p.find_all(
            'span', itemprop='author')])

    def publisher(self):
        article = self.articles()
        return ''.join([span.text for p in article[1].find_all('p') for strong in p.find_all('strong') if strong.text == 'Publisher' for span in p.find_all(
            'span', itemprop='name')])

    def datePublished(self):
        article = self.articles()
        return ''.join([span.text for span in article[1].find_all(
            'span', itemprop='datePublished')])

    def numPage(self):
        article = self.articles()
        return ''.join([span.text for p in article[1].find_all('p') for strong in p.find_all('strong') if strong.text == 'Publisher' for span in p.find_all(
            'span', itemprop='numberOfPages')])

    def isbn(self):
        article = self.articles()

        return ''.join([span.text for p in article[1].find_all('p') for strong in p.find_all('strong') if strong.text == 'Publisher' for span in p.find_all(
            'span', itemprop='isbn')])

    def download_link(self, title):
        article = self.articles()
        url = ''.join([href['href'] for href in article[1].find_all(
            'a') if href.text == 'Download link'])
        link = download(url=url, title=title)
        return link
