# -*- coding:utf-8 -*-

def register_base(app):
    from .models import db
    db.init_app(app)

def register_home(app):
    from .handlers import home
    app.register_blueprint(home.bp, url_prefix='')

def register_api(app):
    from .api import init_app
    init_app(app)

def create_app(config=None):
    from .app import create_app
    app = create_app(config)
    register_base(app)
    register_home(app)
    register_api(app)
    return app