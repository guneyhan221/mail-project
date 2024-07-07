from flask import *
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userandposts.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24), nullable=False,unique=False)
    password = db.Column(db.String(48), nullable=False)

    def __repr__(self) -> str:
        return f"<User {self.id}>"

#Functions
def get_user(id:int)->User:
    return User.query.get_or_404(id)
#Other decarators
@app.before_request
def create_databases():
    db.create_all()

#Routes
@app.route("/")
def home():
    return ""


app.run(debug=True)