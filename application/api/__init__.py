# -*- coding:utf-8 -*-

import re
from flask import Blueprint, request
from . import prob


VERSION_URL = re.compile(r'^/api/\d/')
CURRENT_VERSION = '1'

bp = Blueprint('api', __name__)


@bp.after_request
def headers_hook(response):
    remaining = getattr(request, '_rate_remaining', None)
    if remaining:
        response.headers['X-Rate-Limit'] = str(remaining)

    expires = getattr(request, '_rate_expires', None)
    if expires:
        response.headers['X-Rate-Expires'] = str(expires)

    # javascript can request API
    if request.method in ['GET','POST']: # == 'GET': # 
        response.headers['Access-Control-Allow-Origin'] = '*'

    # api not available in iframe
    response.headers['X-Frame-Options'] = 'deny'
    # security protection
    response.headers['Content-Security-Policy'] = "default-src 'none'"
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

def find_version(environ):
    return CURRENT_VERSION


class ApiVersionMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # when not start with '/api/'
        # when start with '/api/\d/'
        # replace '/api/' to '/api/\d/'
        path = environ.get('PATH_INFO')
        if not path.startswith('/api/'):
            return self.app(environ, start_response)
        if VERSION_URL.match(path):
            print('match')
            return self.app(environ, start_response)

        version = find_version(environ)
        environ['PATH_INFO'] = path.replace('/api/', '/api/%s/' % version)
        return self.app(environ, start_response)


def init_app(app):
    app.wsgi_app = ApiVersionMiddleware(app.wsgi_app)

    prob.api.register(bp)

    app.register_blueprint(bp, url_prefix='/api/%s' % CURRENT_VERSION)