from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get('http://www.gamestop.com/browse/games?nav=28-xu0,13ffff2418')
html = browser.page_source

fileName = 'gamestop.html'
outfile = open(fileName, 'w')
outfile.write(html)
outfile.close()

browser.quit()
soup = BeautifulSoup(html, 'lxml')

position = soup.find('div', class_='product new_product dyother dyMonitor') or soup.find('div', class_='product preowned_product dyother dyMonitor') or soup.find('div', class_='product digital_product dyother dyMonitor')
gameTitle = position.find('a', class_='ats-product-title-lnk').string
console = gameTitle.find_next('strong').string
publisher = console.find_next('p').string
condition = position.find('h4', class_='ats-product-condition').find_next('strong').string
price = condition.find_next('p').string

print(gameTitle)
print(console)
print(publisher)
print(condition)
print(price)