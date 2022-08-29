import os
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
import uuid
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
"""
database_user = os.getenv('DATABASE_USER')
database_password = os.getenv('DATABASE_USER')
database_name = os.getenv('DATABASE_USER')
database_host = os.getenv('DATABASE_HOST')
"""

#database_name = 'user_mgt_service'

database_path = 'postgresql://postgres:chidera@localhost:5432/user_mgt_service'
#database_path = os.environ.get('postgresql://{}:{}@{}/{}'.format(database_user,database_password,database_host,database_name))
db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    country_code = db.Column(db.String(120),nullable=False)
    country_name = db.Column(db.String(120),nullable=False)
    short_code = db.Column(db.String(80), nullable=False)
    use = db.relationship('User',backref='country',lazy=True)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Text, default=lambda: str(uuid.uuid4()), unique=True) 
    first_name = db.Column(db.String(120),nullable=False)
    last_name = db.Column(db.String(120),nullable=False)
    email = db.Column(db.String(120),nullable=False)
    phone = db.Column(db.String(120),nullable=False)
    sex = db.Column(db.String, default=False)
    status = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime(),default=datetime.utcnow)
    update_at = db.Column(db.DateTime(),default=datetime.utcnow)   
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'),nullable=False)



