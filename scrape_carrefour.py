#
# command line:
# python -m venv venv_c4
# venv_c4/scripts/activate
# pip install requests
# pip install bs4

import requests
from bs4 import BeautifulSoup
import json

def scrape_carrefour():
    pages=10
    jsondata=[]

    for page in range(0,pages):
        url='https://www.carrefouruae.com/mafuae/en/frozen-food/c/F6000000?pg=%s' % (page,)     #-- set url 
        response = requests.get(url)                            #-- request connection to url
        soup = BeautifulSoup(response.text, 'html.parser')      #-- get data and parse 

        anchors=soup.find_all('a', class_='js-gtmProdData')
        if(len(anchors)>0):
            print('scraping data from %s"' % (url,))
            for a in anchors:
                item=a['data-gtm-prod-data']    #-- get json string from the anchor attribute name 'data-gtm-prod-data'
                jsonitem=json.loads(item)       #-- convert string to json object
                jsondata.append(jsonitem)       #-- append item to json

            with open('carrefour.json', 'w') as outfile:
                json.dump(jsondata, outfile)    #-- save jsondata to 'carrefour.json' file
        else:
            return      #-- exit loop since nothing to scrape

scrape_carrefour()      #-- call scraping function 