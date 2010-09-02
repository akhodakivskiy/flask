from flask import Flask
import os
import sys

SECRET_KEY = '6RZ~Iz{*>a5R&ZX>s@>a*(H,rlaU*<hn1?{A5A7V/C9Z)lIB_xqmpe]^45}4*9|+L'

APPS = [ 'admin', 'accounts' ]
APP_NAME = 'skeleton'

def create_app(app_name=APP_NAME):
    app = Flask(__name__)
    app.config.from_object(__name__)

    cur = os.path.abspath(__file__)
    sys.path.append(os.path.dirname(cur) + '/apps')
    for a in APPS:
        app.register_module(__import__('%s.views' % a).module)
    
    return app

