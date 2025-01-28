from flask_sqlalchemy import SQLAlchemy
import datetime

from sqlalchemy import Column

db = SQLAlchemy()


class Automobilis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gamintojas = db.Column(db.String)
    modelis = db.Column(db.String)
    spalva = db.Column(db.String)
    salis = db.Column(db.String)
    kaina = db.Column(db.Float)


