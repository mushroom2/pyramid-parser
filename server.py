import threading
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
import os

def create_app():
    config = Configurator()

    path = os.path.abspath(__file__)
    root = path[:path.rindex("/")]

    config.add_route("index_route", "/")
    config.scan("views")
    config.add_static_view("css", "{0}/css".format(root))
    config.add_static_view("js", "{0}/js".format(root))
    
    app = config.make_wsgi_app()
    return app


if __name__ == '__main__':
#    t = threading.Thread(target=run_bot)
#    t.daemon = True
#    t.start()

    app = create_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()