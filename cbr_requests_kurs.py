import requests
from datetime import datetime
from xml.etree import ElementTree

'''
Например, для получения котировок на заданный день
http://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002
    date_req= Date of query (dd/mm/yyyy)
 если параметр(date_req) отсутствует, то Вы получите документ на последнюю зарегистрированную дату.
'''

def data_install_kurs():
    try:
        r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        root = ElementTree.fromstring(r.text)
        data_install_kurs = root.attrib['Date']

        answer_data_to_tlg = ('Курсы ЦБ на дату: {}'.format(data_install_kurs))
        return answer_data_to_tlg
    except ValueError:
        print('Выходим.')


def cbr_requests_kurs(valuta):
    try:
        requests_to_tlg = ''
        now_data = datetime.now()
        now_data = now_data.strftime('%d/%m/%Y')
        cbr_params_kurs = {'date_req': now_data}
        r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp?', params=cbr_params_kurs)

        root = ElementTree.fromstring(r.text)
        #print('root = ', root)
        #print('root.tag = ', root.tag)
        #print('root.attrib = ', root.attrib)

        #bank_info.append(root[0][0].text)  # Bank Name

        for child in root:
            #if valuta == 'ALL':
            #    print('1 {} ({}) = {}' .format(child[3].text, child[1].text, child[4].text))

            if child[1].text == valuta:
                #print('1 {} ({}) = {}' .format(child[3].text, child[1].text, child[4].text))
                answer_to_tlg = ('1 {} ({}) = {} руб.'.format(child[3].text, child[1].text, child[4].text))

                #print(requests_to_tlg)
                return answer_to_tlg

            #    print(child[0].text, child[3].text, child[4].text)
#       #Valute ID = "R01235"


        print(r.url)
        print('Ответ xml:', r.text)
        print('------------------------#-----------------------')

    except ValueError:
        print('Это не число. Выходим.')
