from flask import *
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userdb.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

user_db=SQLAlchemy(app)

app.config['SQLALCHEMY_BINDS'] = {
    'other': 'sqlite:///posts.db'
}

post_db=SQLAlchemy(app)

class User(user_db.Model):
    id=user_db.Column(user_db.Integer,primary_key=True)
    name=user_db.Column(user_db.String(24),nullable=False,unique=True)
    name=user_db.Column(user_db.String(48),nullable=False)

    def __repr__(self) -> str:
        return f"<User {self.id}>"

@app.before_request
def create_databases():
    user_db.create_all()
    post_db.create_all()

@app.route("home")
def home():
    ...

app.run(debug=True)