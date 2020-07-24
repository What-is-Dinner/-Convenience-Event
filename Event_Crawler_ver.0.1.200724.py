from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import json

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_driver_path = 'C:/Users/color/Desktop/chromedriver.exe'

driver = webdriver.Chrome(options = chrome_options, executable_path = chrome_driver_path)
driver.implicitly_wait(3)

data = {'cu_plus' : [], 'cu_morning' : [], 'cu_present' : [], 'gs_plus' : [], }


def cu_crawler_plus(pageIndex = 1):
    global driver, data

    prev_name = []
    prev_price = []
    val = 1

    print("Start cu_plus crawling!")
    print("Progress : ", end = '')

    while True:
        driver.get('http://cu.bgfretail.com/event/plus.do;jsessionid=5xgWfZqWG26rSCX2xXychtKQdJG8FWMnQMrz5WngvZR8TKcysQ0y!1091641819?category=event&amp;depth2=1&amp;sf=N&pageIndex=' + str(pageIndex))

        time.sleep(val)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        product_name = soup.select('#contents > div.relCon > div.prodListWrap > ul > li > p.prodName > a')
        product_price = soup.select('#contents > div.relCon > div.prodListWrap > ul > li > p.prodPrice > span')

        if ((product_name == []) and (product_price == [])) or ((product_name == prev_name) and (product_price == prev_price)):
            break

        prev_name = product_name
        prev_price = product_price

        for i in range(len(product_name)):
            data['cu_plus'].append({'name' : product_name[i].get_text(), 'price' : product_price[i].get_text()})

        print("#", end = '')
        pageIndex += 1
        val += 0.55

    print("\nTotal page : " + str(pageIndex - 1))
    print("Success cu_plus crawling!")


def cu_crawler_morning(pageIndex = 1):
    global driver, data

    prev_name = []
    prev_price = []
    val = 1

    print("Start cu_morning crawling!")
    print("Progress : ", end = '')

    while True:
        driver.get('http://cu.bgfretail.com/event/morning.do;jsessionid=QlGsfZLPJxjy7Jr3NNXCYXTpwmwNTqnqjJ1n1J8yvh48t2x9yV3y!1091641819?category=event&amp;depth2=2&pageIndex=' + str(pageIndex))

        time.sleep(val)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        product_name = soup.select('#contents > div.relCon > div.prodListWrap > ul > li > p.prodName > a')
        product_price = soup.select('#contents > div.relCon > div.prodListWrap > ul > li > p.prodPrice > span')

        if ((product_name == []) and (product_price == [])) or ((product_name == prev_name) and (product_price == prev_price)):
            break

        prev_name = product_name
        prev_price = product_price

        for i in range(len(product_name)):
            data['cu_morning'].append({'name' : product_name[i].get_text(), 'price' : product_price[i].get_text()})

        print("#", end = '')
        pageIndex += 1
        val += 0.55

    print("\nTotal page : " + str(pageIndex - 1))
    print("Success cu_morning crawling!")


def cu_crawler_present(pageIndex = 1):
    global driver, data

    prev_name = []
    prev_price = []

    while True:
        driver.get('http://cu.bgfretail.com/event/present.do;jsessionid=kFGTfZKGJkLn1vNps1QT2kQh14pn41yXVbdF7GGLb6c3sZpL4Zbf!-1715295381?category=event&amp;depth2=5&amp;sf=N&pageIndex=' + str(pageIndex))

        time.sleep(10)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        product_name = soup.select('#contents > div.relCon > div.prodListWrap > ul > li > p.prodName > a')
        product_price = soup.select('#contents > div.relCon > div.prodListWrap > ul > li > p.prodPrice > span')

        if ((product_name == []) and (product_price == [])) or ((product_name == prev_name) and (product_price == prev_price)):
            break

        prev_name = product_name
        prev_price = product_price

        for i in range(len(product_name)):
            print(product_name[i].get_text(), "\t", product_price[i].get_text(), "원")

        pageIndex += 1


def start_crawling():
    global data

    print("Start crawling!")

    cu_crawler_plus()
    cu_crawler_morning()

    current = time.strftime('%y%m%d', time.localtime(time.time()))
    file_path = 'c:/Users/color/Desktop/EventList_' + str(current) + '.json'

    with open(file_path, 'w', encoding = 'utf-8') as outfile:
        json.dump(data, outfile, indent = 4, ensure_ascii = False)


if __name__ == '__main__':
    start_crawling()