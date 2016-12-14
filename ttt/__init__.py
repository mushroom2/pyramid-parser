from pyramid.config import Configurator
from pyramid.renderers import JSON


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')

    config.add_renderer('json', JSON(indent=4))
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('sec', '/')
    config.add_route('res', '/res/')
    config.add_route('jres', 'jres.json')
    config.scan()
    return config.make_wsgi_app()
