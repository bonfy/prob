# -*- coding:utf-8 -*-

def register_base(app):
    from .models import db
    db.init_app(app)

def create_app(config=None):
    from .app import create_app
    app = create_app(config)

    from .handlers import home
    app.register_blueprint(home.bp, url_prefix='')

    return app