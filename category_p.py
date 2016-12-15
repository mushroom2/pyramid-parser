from grab import Grab

g = Grab()

g.go('http://hard.rozetka.com.ua/monitors/c80089/page=1/')

for i in g.doc.select('//div[@class="g-i-tile-i-box-desc"]'):
    print(i.text().split('"')[2])
#for i in g.doc.select('//div[@class="clearfix"]//ul[@class="all-cat-b-l"]'):
#    print(i.text())

#('//div[@class="clearfix"]//ul[@class="all-cat-b-l"]//li[@class="all-cat-b-l-i"]//a[@class="all-cat-b-l-i-link-child novisited"]/href')