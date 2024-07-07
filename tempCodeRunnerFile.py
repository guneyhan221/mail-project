from flask import *
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userandposts.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24), nullable=False,unique=True)
    password = db.Column(db.String(48), nullable=False)
    gender=db.Column(db.String(40),nullable=False)
    birth_date=db.Column(db.String(20),nullable=False)

    def __init__(self,name,password,gender,birth_date) -> None:
        self.name=name 
        self.password=password
        self.gender=gender 
        self.birth_date=birth_date
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


@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method=="POST":
        username = request.form['username']
        password = request.form['password']
        gender = request.form['gender']
        birth = request.form['birth-date']

        users=User.query.all()
        user_found=False 

        for user in users:
            if user.name==username:
                user_found=True
        
        if user_found:
            return redirect(url_for("submit"))
        else:
            user=User(username=username,password=password,gender=gender,birth=birth)
            db.session.add(user)
            db.session.commit()
        
    else:
        return redirect(url_for("createaccontpage"))


app.run(debug=True)