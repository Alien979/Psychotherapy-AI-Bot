# init_db.py
from app import db, app

def init_db():
    with app.app_context():
        db.create_all()

init_db()
