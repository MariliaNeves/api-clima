# -*- encoding: utf-8 -*-

from app import app
DEBUG = app.config['DEBUG']

if DEBUG:
    app.logger.info('DEBUG            = ' + str(DEBUG))

if __name__ == "__main__":
    app.run()

