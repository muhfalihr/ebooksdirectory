import re
import unicodedata
from bs4 import BeautifulSoup
import requests


def soup(link):

    user_agent = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

    req = requests.get(link, headers=user_agent)

    soup = BeautifulSoup(req.text, 'lxml')

    if 'listing.php' in link:
        return soup.find_all('section', 'main_content')
    elif 'bookrix' in link:
        return soup.find_all('div', 'modal-body')
    else:
        return soup.find_all('article', 'main_categories')


def wov(list):
    try:
        if list:
            return list[0] if len(list) == 1 else list
    except:
        return list


def clearLast(text):
    char = ",./;'[\=-`<>?:|{(*&^%$#@!~"
    return text.rstrip(char)


def clean(text):
    cleaned = re.sub(r'\n+', '\n', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned)
    normalized = unicodedata.normalize('NFKD', cleaned_text)
    ascii_text = normalized.encode('ascii', 'ignore').decode('ascii')
    replace_text = ascii_text.replace('\"', "'").replace('\r\n', ' - ')
    if replace_text[0] == ' ' and replace_text[-1] == ' ':
        return replace_text[1:-1]
    if replace_text[0] == ' ':
        return replace_text[1:]
    if replace_text[-1] == ' ':
        return replace_text[:-1]
    else:
        return replace_text


def wordCapitalize(text):
    words = text.split()
    capWord = [word.capitalize() for word in words]
    capsentence = ' '.join(capWord)
    return capsentence


def categories():
    category = [
        'Arts & Photography',
        'Biographies & Memoirs',
        'Business & Investing',
        "Children's Books",
        'Comics & Graphic Novels',
        'Computers & Internet',
        'Cooking, Food & Wine',
        'Engineering',
        'Entertainment',
        'Health, Mind & Body',
        'History',
        'Humanities',
        'Law',
        'Literature & Fiction',
        'Mathematics',
        'Medicine',
        'Nonfiction',
        'Outdoors & Nature',
        'Religion & Spirituality',
        'Science',
        'Science Fiction & Fantasy',
        'Travel'
    ]
    return category


def ebookNum(link: str):
    match = re.search(r'category=(\d+)', link)
    if match:
        return match.group(1)
    else:
        return ''


def namePage(link):
    match = re.search(r'www\.e-booksdirectory\.com/(.*?)\.php', link)
    if match:
        return match.group(1)
    else:
        return ''


def idDownload(link: str):
    match = re.search(r'download_nid=(\d+)', link)
    if match:
        return match.group(1)
    else:
        return ''


def idLink(link):
    match = re.search(r'/view/(\d+)', link)
    if match:
        return match.group(1)
    else:
        return ''


def charSpecial(teks):
    pattern = r'[,\./;\\=\-`<>?:|\]\[\{\}\+\_\)\(\*&\^%\$#@!\~]'

    result = re.sub(pattern, '', teks)

    return result.replace('  ', '-').replace(' ', '-')


def unique(inList):
    unique_list = []
    [unique_list.append(x) for x in inList if x not in unique_list]
    return unique_list
