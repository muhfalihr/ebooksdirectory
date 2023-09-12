from Gaslah import categories, soup, Categories, saveResult, takeNTP, saveError
import os


while True:
    os.system('clear')
    print('Crawling Web http://www.e-booksdirectory.com/')

    print('Note : Cat = Categories, new = Halaman New, top = Halaman Top, popular = Halaman Popular')
    searchBy = input('Search data by Cat, new, top or popular:\n> ')

    fixOpsi = searchBy.lower()

    match fixOpsi:
        case 'cat':
            os.system('clear')
            for i, cat in enumerate(categories()):
                print(f"{i+1}. {cat}")

            select1 = int(input('Search data by number:\n> '))

            link = 'http://www.e-booksdirectory.com/'
            items = soup(link)

            kategori = Categories(items)

            clText = kategori.cat_largeText()
            clLink = kategori.cat_largeLink()
            scText = kategori.cat_smallText(clText)
            scLink = kategori.cat_smallLink()

            os.system('clear')
            print('Sub-Category'.center(50, '-'))
            for i, sc in enumerate(scText[select1-1]):
                print(f'{i+1}. {sc}')

            yn = input('Crawling Categori ini aja (y/n):\n> ')
            match yn.lower():
                case 'y':
                    try:
                        saveResult(clLink[select1-1])
                    except IndexError:
                        saveError()
                case 'n':
                    select2 = int(input('Crawling data by number:\n> '))
                    try:
                        saveResult(scLink[select1-1][select2-1])
                    except IndexError:
                        saveError()
                case _:
                    print('Nggak ada bang')

            break

        case 'new' | 'top' | 'popular':
            os.system('clear')
            print(
                f'Crawling {fixOpsi} Page http://www.e-booksdirectory.com/\n')

            page = input('Tentukan banyak page(1 page terdapat 20 data) :\n> ')
            links = takeNTP(int(page), fixOpsi)
            saveResult(links, fixOpsi)
            break
        case _:
            print('Nggak ada bang')
            break
