from pyramid.renderers import render_to_response
from pyramid.view import view_config


@view_config(route_name="index_route")
def index(request):
    return render_to_response('pt/index.pt', {'name': 'world'}, request)
