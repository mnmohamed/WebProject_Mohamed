import requests
import datetime

today = str(datetime.datetime.now()).split(' ')[0]

sites = {'Bestbuy': 'https://bestbuy.com/',
         'Gamestop':'http://www.gamestop.com/browse/playstation-4/games?nav=28-xu0,131dc-ffff2418',
         'Amazon' : 'https://www.amazon.com'}

for name, link in sites.items():
    response = requests.get(link)
    html = response.content

    fileName = today + '.' + name + '.html'
    outfile = open(fileName, "wb")
    outfile.write(html)
    outfile.close()