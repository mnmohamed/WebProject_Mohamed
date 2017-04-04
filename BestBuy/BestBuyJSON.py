from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get('http://www.gamestop.com/browse/games/playstation-4?nav=28-xu0,131dc-ffff2418')
html = browser.page_source

fileName = 'gamestop.html'
outfile = open(fileName, 'w')
outfile.write(html)
outfile.close()

browser.quit()
soup = BeautifulSoup(html, 'lxml')

position = soup.find('div', class_='product new_product dyother dyMonitor')
gameTitle = position.find('a', class_='ats-product-title-lnk').string

print(gameTitle)