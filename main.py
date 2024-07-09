from flask import *
from flask_sqlalchemy import SQLAlchemy
import os
import json
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), nullable=False,unique=True)
    password = db.Column(db.String(48), nullable=False)
    gender=db.Column(db.String(40),nullable=False)
    birth_date=db.Column(db.String(20),nullable=False)

    def __init__(self,username,password,gender,birth_date) -> None:
        self.username=username 
        self.password=password
        self.gender=gender 
        self.birth_date=birth_date
    def __repr__(self) -> str:
        return f"<User {self.id}>"

#Functions
def get_user(id:int)->User:
    return User.query.get_or_404(id)
def delete_user(id:int):
    db.session.delete(User.query.filter_by(id=id).first())
    db.session.commit()
def send_post(post_id,username,to,subject,content,title):
    data={post_id:{"username":username,"to":to,"title":title,"subject":subject, "content":content}}

    with open(f"users/{username}/giden.txt","a") as file:
        file.write(data)
        file.write("\n")
def get_post(username,post_id):
    ...
#Other decarators
@app.before_request
def create_databases():
    db.create_all()
    users=User.query.all()
    for user in users:
        if not os.path.exists(f"users/{user.username}"):
            os.makedirs(f"users/{user.username}")
            with open(f"users/{user.username}/giden.txt","w") as file:
                pass
            with open(f"users/{user.username}/gelen.txt","w") as file:
                pass
    send_post("ggdfdfgg2","bbbb1","post","subject","body","test")
#Routes
@app.route("/")
def homepage():
    return redirect(url_for("home"))

@app.route("/home/",methods=["GET", "POST"])
def home():
    if request.method=="POST":
        rememberme=request.form["remember-me"]
        if rememberme =="on":
            visiter_ip = request.remote_addr
            rmipf = open("rmip.txt",'w')
            rmipf.writelines(visiter_ip)
            rmipf.close()
        print(rememberme)
        return render_template("home.html",loged_in=True)
    return render_template("home.html",loged_in=False)

@app.route("/create-account")
def createaccountpage():
    return render_template("createaccount.html")

#change
@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method=="POST":
        username = request.form['username']
        password = request.form['password']
        gender = request.form['gender']
        birth_date = request.form['birth-date']
        user_found = User.query.filter_by(username=username).first()

        if user_found:
            return redirect(url_for("createaccountpage"))
        else:
            user = User(username=username, password=password, gender=gender, birth_date=birth_date)
            try:
                if username not in os.listdir("users/"):
                    os.makedirs(f"users/{str(username)}")
                    with open(f"users/{username}/giden.txt","w") as f:
                        pass

                    with open(f"users/{username}/gelen.txt","w") as f:
                        pass
            except: 
                os.makedirs("users") 
                os.makedirs(f"users/{str(username)}")
                with open(f"users/{username}/giden.txt","w") as f:
                    pass

                with open(f"users/{username}/gelen.txt","w") as f:
                    pass
            db.session.add(user)
            db.session.commit()
        return redirect(url_for("users"))  
    else:
        return redirect(url_for("createaccountpage"))

@app.route("/login")
def login():

    return render_template("login.html")
@app.route("/users")
def users():
    users=User.query.all()

    return "<br>".join([f"{user.username}-{user.password}-{user.gender}-{user.birth_date}" for user in users])

app.run(debug=True)