from selenium import webdriver
import datetime
from bs4 import BeautifulSoup
import json

# Create dict for JSON Object
response = []

# Prepare for parsing APNewsBriefs with BeautifulSoup after Scraping with Selenium

url = 'http://www.gamestop.com/browse/games?nav=28-xu0,13ffff2418'
i = 0
while i < 100:
    browser = webdriver.Chrome()
    urlGameStop = url
    pageGameStop = browser.get(urlGameStop)
    soupGameStop = BeautifulSoup(browser.page_source, 'lxml')
    i += 1

    browser.quit()


    # Parse GameStop urlbrowser.page_source
    today = str(datetime.datetime.now().date())

    for position in soupGameStop.find_all('div', class_='product new_product dyother dyMonitor'):
        gameTitle = position.find('a', class_='ats-product-title-lnk').string
        console = gameTitle.find_next('strong').string
        if(console and console.find_next('p')):
            publisher = console.find_next('p').string
        else:
            publisher = 'not included'
        condition = position.find('h4', class_='ats-product-condition').find_next('strong').string
        price = condition.find_next('p').string
        url = ''
        response.append(
            {'Game Title': gameTitle, 'Game System': console, 'Publisher': publisher, 'Condition': condition,
             'Price': price})
    for position in soupGameStop.find_all('div', class_='product digital_product dyother dyMonitor'):
        gameTitle = position.find('a', class_='ats-product-title-lnk').string
        console = gameTitle.find_next('strong').string
        if (console.find_next('p')):
            publisher = console.find_next('p').string
        else:
            publisher = 'not included'
        condition = position.find('h4', class_='ats-product-condition').find_next('strong').string
        price = condition.find_next('p').string
        url = ''
        response.append(
            {'Game Title': gameTitle, 'Game System': console, 'Publisher': publisher, 'Condition': condition,
             'Price': price})
    for position in soupGameStop.find_all('div', class_='product preowned_product dyother dyMonitor'):
        gameTitle = position.find('a', class_='ats-product-title-lnk').string
        console = gameTitle.find_next('strong').string
        if (console.find_next('p')):
            publisher = console.find_next('p').string
        else:
            publisher = 'not included'
        condition = position.find('h4', class_='ats-product-condition').find_next('strong').string
        price = condition.find_next('p').string
        url = ''
        response.append(
            {'Game Title': gameTitle, 'Game System': console, 'Publisher': publisher, 'Condition': condition,
             'Price': price})
    for href in soupGameStop.find_all('a'):
        if href.string == 'Next':
            print(href.get('href'))
            url = 'http://www.gamestop.com' + href.get('href')

    if url == '':
        i = 2
        # Make changes to response for GameStop
    print(i)

# Write response to JSON file
postingsFile = '/Users/laptop/Desktop/WebProject_Mohamed/GameStopJSONs/' + today + '.GameStop.json'

with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()
