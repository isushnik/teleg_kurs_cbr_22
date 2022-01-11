import requests
from xml.etree import ElementTree


def cbr_news():
    cbr_news = []

    try:
        r = requests.get('http://www.cbr.ru/rss/eventrss')
        root = ElementTree.fromstring(r.text)
        print(r.url)

        for child in root:
            print(child.tag, child.attrib)

        for element in root.iter('item'):
            cbr_news_one = ('{} \n{} \n{}'.format(element[0].text, element[1].text, element[4].text))
            #print(cbr_news_one)
            cbr_news.append(cbr_news_one)
        print('------------------------#-----------------------')
        return (cbr_news)

    except ValueError:
        print('Это не число. Выходим.')