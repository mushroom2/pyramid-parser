from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.renderers import render_to_response

from grab import Grab
import json
from urllib import parse


class Parser(object):
    def __init__(self, minprice, maxprice):
        self.result = None
        try:
            self.minprice = int(minprice)
            self.maxprice = int(maxprice)
        except ValueError:
            self.wrog_operation()
            self.minprice = 1
            self.maxprice = 0
        if self.minprice > self.maxprice:
            self.wrog_operation()
        else:
            self.rozparse()

    def wrog_operation(self):
        self.result = 'something was wrong'

    def rozparse(self):
        g = Grab()
        names = []
        prices = []
        count = 1
        paginator = []
        res = {}
        g.go('http://rozetka.com.ua/stabilizers/c144719/')

        for i in g.doc.select('//ul[@name="paginator"]/li[@class="paginator-catalog-l-i"]/span'):
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
        self.result = res


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'ttt'}

@view_config(route_name='sec')
def sec_view(request):
    if request.method == 'POST':

        pricefrom = request.params['pricefrom']
        priceto = request.params['priceto']
        response = Response()
        response.set_cookie('pricefrom', value=pricefrom, max_age=3600)
        response.set_cookie('priceto', value=priceto, max_age=3600)
        return HTTPFound(location = "/", headers=response.headers)
    else:
        return render_to_response('templates/two.pt', {}, request)


@view_config(route_name='res')
def res_view(request):
    if 'priceto' in request.cookies and 'pricefrom' in request.cookies:
        priceto = request.cookies['priceto']
        pricefrom = request.cookies['pricefrom']
        pars = Parser(pricefrom, priceto)
        return render_to_response('templates/res.pt', {'priceto': priceto,
                                                       'pricefrom': pricefrom,
                                                       'pars': pars.result},
                                  request)
