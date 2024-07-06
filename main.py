from flask import *
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userandposts.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(24),nullable=False,unique=True)
    password=db.Column(db.String(48),nullable=False)

    def __repr__(self) -> str:
        return f"<User {self.id}>"

@app.before_request
def create_databases():
    db.create_all()

@app.route("/")
def home():
    ...

app.run(debug=True)