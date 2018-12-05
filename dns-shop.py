from selenium import webdriver
from lxml import html

page_num = 1
url = 'https://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/?p=%s&i=1&mode=list&brand=brand-apple' % page_num

driver = webdriver.Firefox()
driver.get(url)
content = driver.page_source

tree = html.fromstring(content)

last_page = tree.xpath('//span[@class=" item edge"]')[0].attrib.get('data-page-number')
last_page = int(last_page)
d=[]

while page_num <= last_page:
    url = 'https://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/?p=%s&i=1&mode=list&brand=brand-apple' % page_num

    driver.get(url)

    print('Страница: ', page_num)

    names = driver.find_elements_by_tag_name('h3')
    prices = driver.find_elements_by_class_name('price_g')
    links = driver.find_elements_by_xpath("//div[@class='title']/a")

    for name, price, link in zip(names, prices, links):
        name = name.text
        price = price.text
        link = link.get_attribute("href")

        d.append((name, price, link))
        print(d)

    with open('dns.csv', 'w') as out_f:
        for i in d:
            i = str(i)
            out_f.write(i + '\n')

    page_num += 1

driver.close()