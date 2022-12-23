from flask import Flask
from config import config


import routes


app = Flask(__name__)

def page_not_found(error):
    return('Page not found'), 404

if __name__=='__main__':
    app.config.from_object(config['development'])

    app.register_blueprint(routes.movies_main, url_prefix = '/movies')
    app.register_blueprint(routes.users_main, url_prefix = '/CreateAcount')
    app.register_blueprint(routes.login_main, url_prefix = '/login')

    app.register_error_handler(404, page_not_found)
    app.run()
