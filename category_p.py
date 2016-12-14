from grab import Grab

g = Grab()

g.go('http://rozetka.com.ua/all-categories-goods/')

for i in g.doc.select('//div[@class="clearfix"]/ul[@class="all-cat-b-l"]/'):
    print(i.text())
#for i in g.doc.select('//div[@class="clearfix"]//ul[@class="all-cat-b-l"]'):
#    print(i.text())

#('//div[@class="clearfix"]//ul[@class="all-cat-b-l"]//li[@class="all-cat-b-l-i"]//a[@class="all-cat-b-l-i-link-child novisited"]/href')