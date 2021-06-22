
"""
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'MNBVCXXZ'

    from .views import views
    from .auth_users import auth_users

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth_users, url_prefix='/')

    return app
"""