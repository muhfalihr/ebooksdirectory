from bs4 import BeautifulSoup
import requests
from .utility import idDownload, charSpecial, idLink, soup as s


def download(url, title=''):
    user_agent = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

    if 'smashwords' in url:
        resp = requests.get(url, headers=user_agent)

        soup = BeautifulSoup(resp.text, 'lxml')

        judul = charSpecial(title.lower())
        id = idLink(url)
        link_download = 'https://www.smashwords.com/books/download/{0}/1/latest/0/0/{1}.pdf'.format(
            id, judul)
        return link_download

    elif 'archive' in url:

        resp = requests.get(url, headers=user_agent)

        soup = BeautifulSoup(resp.text, 'lxml')

        items = soup.find_all(
            'div', 'col-sm-4 thats-right item-details-archive-info')

        link_download = ''.join(['https://archive.org' + a['href'] for item in items for section in item.find_all('section', 'boxy item-download-options') for div in section.find_all(
            'div', 'format-group') for a in div.find_all('a', 'format-summary download-pill') if a.text.replace('download', '').strip() == 'PDF'])
        return url if link_download == '' else link_download

    elif 'manybooks.net' in url:

        resp = requests.get(url, headers=user_agent)

        soup = BeautifulSoup(resp.text, 'lxml')

        href = ''.join([a['href'] for item in soup.find_all(
            'section', 'block block-mnybks-book-files block-book-file-links clearfix') for bc in item.find_all('div', 'block-content') for fg in bc.find_all('div', 'form-group') for a in fg.find_all('a', 'mb-link-files use-ajax mb-login-ajax-link')])

        link_download = f'https://manybooks.net/books/get/{idDownload(href)}/6'
        return url if link_download == '' else link_download

    elif 'shatteredcrystals.net' in url:

        resp = requests.get(url, headers=user_agent)

        soup = BeautifulSoup(resp.text, 'lxml')

        link_download = ''.join(['http://www.shatteredcrystals.net/'+a['href']
                                 for strong in soup.find_all('strong') for a in strong.find_all('a')])
        return url if link_download == '' else link_download

    elif 'bookrix' in url:

        resp = requests.get(url, headers=user_agent)

        soup = BeautifulSoup(resp.text, 'lxml')

        items = soup.find_all('div', id='bookfree')

        link = ''.join(['https://www.bookrix.com'+a['data-download']
                       for item in items for a in item.find_all('a', href='#')])

        link_download = ''.join(['https://www.bookrix.com'+a['href']
                                 for item in s(link) for a in item.find_all('a')])

        return url if link_download == '' else link_download

    elif 'mises.org' in url:

        resp = requests.get(url, headers=user_agent)

        soup = BeautifulSoup(resp.text, 'lxml')

        items = soup.find_all('div', 'list-group-item')

        link_download = [a['href'].replace(' ', '%20') for item in items for content in item.find_all(
            'div', 'content') for a in content.find_all('a') for img in content.find_all('img') if img['title'] == 'application/pdf']
        return url if ''.join(link_download) == '' else ''.join(link_download)

    elif 'wikibooks.org' in url:

        page = url.split('/')[4]

        link_download = f'https://en.wikibooks.org/w/index.php?title=Special:DownloadAsPdf&page={page}&action=show-download-screen'

        return url if page == '' else link_download

    elif 'aerospaceengineering' in url:

        resp = requests.get(url, headers=user_agent)

        soup = BeautifulSoup(resp.text, 'lxml')

        items = soup.find_all('div', 'book-columns')

        link_download = ''.join([a['href'] for item in items for td in item.find_all(
            'td', style='text-align: left;') for a in td.find_all('a')])
        return url if link_download == '' else link_download

    elif 'hdl.handle.net' in url:
        resp = requests.get(url, headers=user_agent)

        soup = BeautifulSoup(resp.text, 'lxml')

        items = soup.find_all('div', 'col-xs-6 col-sm-12')

        link_download = ''.join(['https://vtechworks.lib.vt.edu'+a['href']
                                 for item in items for div in item.find_all('div', 'filename-word-break') for a in div.find_all('a')])
        return url if link_download == '' else link_download

    elif 'www.faa.gov' in url:
        resp = requests.get(url, headers=user_agent)

        soup = BeautifulSoup(resp.text, 'lxml')

        items = soup.find_all('article', 'content')

        link_download = ''.join([a['href'] for item in items for ul in item.find_all(
            'ul', 'join') for a in ul.find_all('a')])

        return url if link_download == '' else link_download

    elif 'www.rand.org' in url:
        resp = requests.get(url, headers=user_agent)

        soup = BeautifulSoup(resp.text, 'lxml')

        items = soup.find_all('table', 'ebook')

        link_download = ['https://www.rand.org'+span.a['href']
                         for item in items for span in item.find_all('span', 'format-pdf')][0]
        return url if link_download == '' else link_download

    else:
        return url
