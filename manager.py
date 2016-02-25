# -*- coding:utf-8 -*-

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from application.models import db, PB
from application import create_app

import os
filename = os.path.join(os.getcwd(), 'local_config.py')
app = create_app(filename)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()