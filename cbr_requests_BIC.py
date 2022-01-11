import requests
from xml.etree import ElementTree

def cbr_requests_BIC(bicc):
    bank_info = []
    bic_input = bicc

    name = ''

    try:
        cbr_params_bank = {'bic': bic_input} # , 'name': name}
        r = requests.get('http://www.cbr.ru/scripts/XML_bic.asp?', params=cbr_params_bank)

        root = ElementTree.fromstring(r.text)

        print(r.url)
        print(r.text)
        #print('root = ', root)
        #print('root.tag = ', root.tag)
        #print('root.attrib = ', root.attrib)

        bank_info.append(root[0][0].text) # Bank Name

        #for child in root:
        #    print(child.tag, child.attrib)
        #    bank_info.append(child.attrib['DU'])

        #for element in root.iter('Record'):
        #    for child in element:
        #        print(child.text)

        print('------------------------#-----------------------')
        return (bank_info)
    except ValueError:
        print('Это не число. Выходим.')
