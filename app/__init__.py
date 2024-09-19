from flask import Flask
from config import Config
from .extensions import db
from app import models

from app.services.LeageAPI import LeagueAPI


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init Extensions
    #db.init_app(app)
    #api = LeagueAPI("https://gql.poolplayers.com/graphql")
    #league_info = api.query_league("birmingham")
    #league_divisions = api.query_divisions("birmingham", league_info['data']['league']['currentSessionId'])

    #print(league_info)
    #print(league_divisions)

    from app.index.routes import bp as index_bp
    app.register_blueprint(index_bp)

    return app
