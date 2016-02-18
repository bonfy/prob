# -*- coding:utf-8 -*-

from application import create_app

import os
filename = os.path.join(os.getcwd(), 'local_config.py')
app = create_app(filename)

app.run(host='0.0.0.0')
