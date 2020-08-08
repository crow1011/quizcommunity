from .db import db

class SimpleQuestions(db.Document):
    ask = db.StringField(required=True, unique=True)
    ans = db.StringField(required=True)
    status = db.StringField(required=True)


