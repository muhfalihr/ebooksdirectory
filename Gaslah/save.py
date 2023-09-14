from .takeLink import takeHref
from .crawl import CrawlDetail
import json


def returnSuccess(urls):

    results = []
    datas = {
        'status': 200,
        'data': results
    }

    for link in urls:
        crawl = CrawlDetail(link)
        image = crawl.img()
        title = crawl.title()
        author = crawl.author()
        publisher = crawl.publisher()
        dp = crawl.datePublished()
        numpage = crawl.numPage()
        isbn = crawl.isbn()
        desc = crawl.desc()
        origin_site = crawl.download_link(title)

        data = {
            'title': title,
            'thumbnail_url': image,
            'author': author,
            'publisher': publisher,
            'date_published': dp,
            'number_of_page': numpage,
            'isbn/asin': isbn,
            'description': desc,
            'original_site': origin_site
        }
        results.append(data)

        dumps = json.dumps(datas, indent=4)

    return dumps


def returnError():
    datas = {
        'status': 400,
        'data': []
    }
    dumps = json.dumps(datas, indent=4)
    return dumps
