from .takeLink import takeHref
from .crawl import CrawlDetail
import json


def saveResult(urls, opsi=''):

    results = []
    datas = {
        'status': 200,
        'data': results
    }
    # count = 1
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
        download_link = crawl.download_link(title)

        data = {
            'title': title,
            'thumbnail_url': image,
            'author': author,
            'publisher': publisher,
            'date_published': dp,
            'number_of_page': numpage,
            'isbn/asin': isbn,
            'description': desc,
            'download_link': download_link
        }
        results.append(data)

        dumps = json.dumps(datas, indent=4)

        try:
            with open(f'Results/detail_category_{opsi}.json', 'w') as file:
                file.write(dumps)
        except:
            with open(f'Results/detail_category_{opsi}.json', 'r+') as file:
                file.write(dumps)

    # print(f'\rData {count} berhasil', end="")
    # count += 1
    # print()


def saveError():
    datas = {
        'status': 400,
        'data': []
    }
    dumps = json.dumps(datas, indent=4)
    try:
        with open(f'Results/detail_ERROR.json', 'w') as file:
            file.write(dumps)
    except:
        with open(f'Results/detail_ERROR.json', 'r+') as file:
            file.write(dumps)
