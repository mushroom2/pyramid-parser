from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.renderers import render_to_response

from grab import Grab
import json
from urllib import parse


class Parser(object):
    def __init__(self, minprice, maxprice, category):
        self.result = None
        try:
            self.minprice = int(minprice)
            self.maxprice = int(maxprice)
            self.category = category
        except ValueError:
            self.wrog_operation()
            self.minprice = 1
            self.maxprice = 0
        if self.minprice > self.maxprice:
            self.wrog_operation()
        else:
            self.rozparse()

    def wrog_operation(self):
        self.result = [{"name": "ERROR Invslid input", "price": 0}]

    def rozparse(self):
        g = Grab()
        names = []
        prices = []
        count = 1
        paginator = []
        res = {}
        jres = []
        g.go(self.category)

        for i in g.doc.select('//ul[@name="paginator"]/li[@class="paginator-catalog-l-i"]/a'):
            paginator.append(i.text())

        while count < (int(paginator[-1])+1):
            g.go(self.category + 'page=' + str(count) + '/')
            for title in g.doc.select('//div[@class="g-i-tile-i-box-desc"]/div[@class="g-i-tile-i-title clearfix"]'):
                names.append(title.text())
            for i in g.doc.select('//div[@class="g-i-tile-i-box-desc"]'):
                try:
                    prices.append(json.loads(parse.unquote(i.text().split('"')[1]))["price"])
                except ValueError:
                    prices.append(0)
                except TypeError:
                    prices.append(0)
            print(count)
            count += 1

        for key, value in zip(names, prices):
            res[key] = value

        for i in list(filter(lambda v: v[1] <= self.maxprice and v[1] >= self.minprice, list(res.items()),)):
            jres.append(dict([("name", i[0]), ("price", i[1])]))
        self.result = jres


@view_config(route_name='sec')
def sec_view(request):
    if request.method == 'POST':

        pricefrom = request.params['pricefrom']
        priceto = request.params['priceto']
        cat = request.params['myselect']
        response = Response()
        response.set_cookie('cat', value=cat, max_age=3600)
        response.set_cookie('pricefrom', value=pricefrom, max_age=3600)
        response.set_cookie('priceto', value=priceto, max_age=3600)
        return HTTPFound(location="/res/", headers=response.headers)
    else:
        return render_to_response('templates/two.pt', {}, request)


@view_config(route_name='res')
def res_view(request):
    return render_to_response('templates/res.pt', {}, request)


@view_config(route_name='jres', renderer='json')
def json_view(request):
    if 'priceto' in request.cookies and 'pricefrom' in request.cookies:
        cat = request.cookies['cat']
        priceto = request.cookies['priceto']
        pricefrom = request.cookies['pricefrom']
        pars = Parser(pricefrom, priceto, cat)
        r = Response()
        r.content_type = 'application/json'
        r.charset = 'utf8'
        return pars.result
