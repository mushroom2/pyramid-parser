from grab import Grab
import json
from urllib import parse


class Parser(object):
    def __init__(self, minprice, maxprice):
        self.minprice = minprice
        self.maxprice = maxprice
        if self.minprice > self.maxprice:
            self.wrog_operation()
        else:
            self.rozparse()

    def wrog_operation(self):
        return print('something was wrong')

    def rozparse(self):
        g = Grab()
        names = []
        prices = []
        count = 1
        paginator = []
        res = {}
        g.go('http://rozetka.com.ua/stabilizers/c144719/')

        for i in g.doc.select('//ul[@name="paginator"]/li[@class="paginator-catalog-l-i"]/a'):
            paginator.append(i.text())


        while count < (int(paginator[-1])+1):
            g.go('http://rozetka.com.ua/stabilizers/c144719/page=' + str(count) + '/')
            for title in g.doc.select('//div[@class="g-i-tile-i-box-desc"]/div[@class="g-i-tile-i-title clearfix"]'):
                names.append(title.text())
            for i in g.doc.select('//div[@class="g-i-tile-i-box-desc"]'):
                prices.append(json.loads(parse.unquote(i.text().split('"')[1]))['price'])
            print(count)
            count += 1

        for key, value in zip(names, prices):
            res[key] = value


        print(res['Электромир Volter СНПТО 18пт'])
        return print(res)


p = Parser(1, 4)