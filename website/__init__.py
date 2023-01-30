from flask import Flask
from flask_cors import CORS
# from werkzeug import exceptions

def create_app():
    app = Flask(__name__) #intialise flask
    CORS(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
