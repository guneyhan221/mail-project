from flask import *
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userandposts.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24), nullable=False,unique=False)
    password = db.Column(db.String(48), nullable=False)
    gender=db.Column(db.String(10),nullable=False)
    birth_date=db.Column(db.String(20),nullable=False)

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
def homepage():
    return redirect(url_for("home"))

@app.route("/home/")
def home():
    return render_template("home.html",loged_in=False)

@app.route("/create-account")
def createaccontpage():
    return render_template("createaccount.html")


@app.route('/submit', methods=['POST'])
def submit():
    if request.method=="POST":
        username = request.form['username']
        password = request.form['pasword-input']
        gender = request.form['gender-label']
        birth = request.form['birth-date']

    else:
        return redirect(url_for("createaccontpage"))


app.run(debug=True)