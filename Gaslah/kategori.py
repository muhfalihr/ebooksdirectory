class Categories:
    def __init__(self, items):
        self.items = items
        self.headlink = 'http://www.e-booksdirectory.com/'

    def cat_smallText(self, cat_large):
        result = [[] for _ in range(len(cat_large))]

        for i in range(len(cat_large)):
            for item in self.items:
                for table in item.find_all('table'):
                    cs = [cs.text for cs in table.find_all('td', 'cat_small')[
                        i] if cs.text.strip() != '']
                    result[i].extend(cs)
        hasil = [[''] if not sublist else sublist for sublist in result]
        return hasil

    def cat_smallLink(self):
        result = [[self.headlink+a['href'] for a in cs.find_all('a')] for item in self.items for table in item.find_all(
            'table') for cs in table.find_all('td', 'cat_small')]
        hasil = [[''] if not sublist else sublist for sublist in result]
        return hasil

    def cat_largeText(self):
        return [cl.text for item in self.items for table in item.find_all(
            'table') for cl in table.find_all('td', 'cat_large')]

    def cat_largeLink(self):
        return [self.headlink+a['href'] for item in self.items for table in item.find_all(
            'table') for cl in table.find_all('td', 'cat_large') for a in cl.find_all('a')]
