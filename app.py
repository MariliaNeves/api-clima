from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.py')

from app.views import *

if __name__ == '__main__':
    app.run()
app.debug = True
