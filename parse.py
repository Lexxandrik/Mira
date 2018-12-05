import requests
from bs4 import BeautifulSoup
import shutil

count = 1

while count <=3:
    url = 'http://www.lostfilm.tv/new/page_' + str(count)
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    rows = soup.findAll('div', {'class': 'row'})

    def find_content():

        for div in rows:
            name = div.find('div' , {'class' : 'name-ru'}).text
            print (name)
            img = div.find('div', {'class' : 'picture-box'})
            pic = img.find ('img').get('src')
            pic1 = 'http:' + pic

            response =  requests.get(pic1, stream=True)

            with open (name.replace(':','') + '.jpg' , 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response

        return
    count+=1
    find_content()