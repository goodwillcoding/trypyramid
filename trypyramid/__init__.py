# -*- coding: utf-8 -*-

from pyramid.config import Configurator


def main(global_config, **settings):
    """
    Initialize Configurator, add applicaiton routes.
    :return: a WSGI app.
    """

    # setup up the configurator from passed in settings
    config = Configurator(settings=settings)
    # include application routes and scan them into Configurator
    config.include(application_routes)
    config.scan()
    # create WSGI app and return it
    wsgi_app = config.make_wsgi_app()
    return wsgi_app


def application_routes(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
