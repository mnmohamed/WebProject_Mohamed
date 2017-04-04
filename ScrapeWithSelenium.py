from selenium import webdriver
import datetime

today = str(datetime.datetime.now().date())

sites = {'Bestbuy': 'https://bestbuy.com/',
         'Gamestop': 'http://www.gamestop.com/browse/games?nav=28-xu0,13ffff2418',
         'Amazon' : 'https://www.amazon.com'
         }

browser = webdriver.Chrome()

for name, link in sites.items():
    response = browser.get(link)
    html = browser.page_source

    fileName = today + '.' + name + '.html'
    outfile = open(fileName, 'w')
    outfile.write(html)
    outfile.close()

browser.quit()