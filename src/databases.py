from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import urllib, json

with open('./src/config.json') as f:
    key = json.load(f)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = key["mysql"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"

    _id = db.Column('id', db.Integer, primary_key = True, autoincrement=True)
    _username = db.Column('username', db.String(128))
    _type = db.Column('type', db.String(4))
    _data = db.Column('data', db.JSON)

    def __init__(self, _username = "", _type = "", _data = {"data":[]}):
        self._username = _username
        self._type = _type
        self._data = _data

    def createNetwork(_username, _type):
        to_insert = Data(_username, _type)
        db.session.add(to_insert)
        db.session.commit()

    def updateData(_username, _type, _data):
        to_update = Data.query.filter_by(_username = _username, _type = _type).first()
        to_update._data = _data
        db.session.commit()

    def getData(_username, _type):
        to_get = Data.query.filter_by(_username = _username, _type = _type).first()
        return to_get._data

    def delete(_username, _type):
        to_delete = Data.query.filter_by(_username = _username, _type = _type).first()
        db.session.delete(to_delete)
        db.session.commit()

    def exist(_username, _type):
        return Data.query.filter_by(_username = _username, _type = _type).count() == 1

    def tableSize():
        return Data.query.filter_by().count()

    def _dropTable():
        for nr in db.session.query(Data._id).distinct():
            row_to_delete = Data.query.get(nr)
            test = row_to_delete._username
            db.session.delete(row_to_delete)

        db.session.commit()
        


class Users(db.Model):
    __tablename__ = "users"

    _id = db.Column('id', db.Integer, primary_key = True, autoincrement=True)
    _username = db.Column('username', db.String(128))

    def __init__(self, _username = ""):
        self._username = _username

    def insert(_username):
        to_insert = Users(_username)
        db.session.add(to_insert)
        db.session.commit()

    def update(_id, _username):
        to_update = Users.query.filter_by(_id = _id).first()
        to_update._username = _username
        db.session.commit()

    def delete(_username):
        to_delete = Users.query.filter_by(_username = _username).first()
        db.session.delete(to_delete)
        db.session.commit()

    def exist(_username):
        return Users.query.filter_by(_username = _username).count() == 1

    def tableSize():
        return Users.query.filter_by().count()

    def _dropTable():
        for nr in db.session.query(Users._id).distinct():
            row_to_delete = Users.query.get(nr)
            test = row_to_delete._username
            db.session.delete(row_to_delete)

        db.session.commit()