# -*- coding: utf-8 -*-
import os
from weshop import create_app
from flask_script import Manager

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


@app.route('/')
def index():
    return 'hello world.'


if __name__ == '__main__':
    manager.run()





