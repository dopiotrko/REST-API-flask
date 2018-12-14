# this file is necessary so app can be run by heroku, not by app.py directly
from app import app
from db import db

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()
