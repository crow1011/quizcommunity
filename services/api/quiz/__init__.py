from flask_restful import Api
from quiz.database.db import initialize_db
from quiz.resources.routes import initialize_routes
from flask import Flask


app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/quizcommunity'
}
initialize_db(app)
initialize_routes(api)
