from .takeLink import takeHref
from .crawl import CrawlDetail
import json
from .utility import ebookNum


def saveResult(urls, opsi=''):
    try:
        take = takeHref(urls)
    except:
        take = urls

    results = []
    count = 1
    for link in take:
        crawl = CrawlDetail(link)
        image = crawl.img()
        title = crawl.title()
        author = crawl.author()
        publisher = crawl.publisher()
        dp = crawl.datePublished()
        numpage = crawl.numPage()
        isbn = crawl.isbn()
        download_link = crawl.download_link(title)

        data = {
            'title': title,
            'thumbnail_url': image,
            'author': author,
            'publisher': publisher,
            'date_published': dp,
            'number_of_page': numpage,
            'isbn/asin': isbn,
            'download_link': download_link
        }
        results.append(data)

        dumps = json.dumps(results, indent=4)
        try:
            category = ebookNum(urls)
        except:
            category = opsi

        try:
            with open(f'Results/detail_category{category}.json', 'w') as file:
                file.write(dumps)
        except:
            with open(f'Results/detail_category{category}.json', 'r+') as file:
                file.write(dumps)

        print(f'\rData {count} berhasil', end="")
        count += 1
    print()
