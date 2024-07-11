from flask import *
from flask_sqlalchemy import SQLAlchemy
import os
import json
import endtoend
app=Flask(__name__)

app.secret_key = '2a58f67140a0e2399b844fe294ecc21c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), nullable=False,unique=True)
    password = db.Column(db.String(48), nullable=False)
    gender=db.Column(db.String(40),nullable=False)
    birth_date=db.Column(db.String(20),nullable=False)
    ip_addr=db.Column(db.String(60),nullable=False)

    def __init__(self,username,password,gender,birth_date) -> None:
        self.username=username 
        self.password=password
        self.gender=gender 
        self.birth_date=birth_date
        self.ip_addr=request.remote_addr
    def __repr__(self) -> str:
        return f"<User {self.id}>"

#Functions
def get_user(username:str)->User:
    return User.query.filter_by(username=username).first()
def delete_user(id:int):
    db.session.delete(User.query.filter_by(id=id).first())
    db.session.commit()
def send_post(post_id,username,to,subject,content,title):
    
    data=f"{post_id}-{username}-{to}-{subject}-{content}-{title}"

    with open(f"users/{username}/giden.txt","a") as file:
        file.write(f"{data}\n")

    
    data=f"{post_id}-{username}-{subject}-{content}-{title}"
    with open(f"users/{to}/gelen.txt","a") as file:
        file.write(f"{data}\n")

def get_post(username,post_id):
    with open(f"users/{username}/gelen.txt","r") as file:
        lines=[line for line in file.readlines()]
        for line in lines:
            if line.split("-")[0]==post_id:
                return line.strip()
#Other decarators
@app.before_request
def create_databases():
    db.create_all()
    users=User.query.all()
    for user in users:
        if not os.path.exists(f"users/{user.username}"):
            os.makedirs(f"users/{user.username}")
            with open(f"users/{user.username}/giden.txt","w") as f:
                ...

            with open(f"users/{user.username}/gelen.txt","w") as f:
                ...

#Routes
@app.route("/")
def homepage():
    return redirect(url_for("home"))

@app.route("/home/",methods=["GET", "POST"])
def home():
    visiter_ip = ""
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        rememberme=request.form.get("remember-me")

        user=User.query.filter_by(username=username,password=password).first()
        
        if not user:
            return redirect(url_for("login"))
        
        if rememberme:
            if rememberme =="on":
                visiter_ip = request.remote_addr
                rmipf = open("rmip.txt",'a')
                rmipf.writelines(f"{visiter_ip}-{username}\n")
                rmipf.close()
        return redirect(f"/home/{username}")
    with open("rmip.txt","r") as f:
        lines=[line.strip() for line in f.readlines()]
        if f"{visiter_ip}-value" in lines:
            return render_template("home.html",loged_in=True)            
    return render_template("home.html",loged_in=False)

@app.route("/home/<username>/")
def usernamehome(username):
    """
    ! hata veriyo kod
    ! try except kullanın
    ! hata kulanıcı hesabına girisyapmamısken /home/<username>/ e gitmeye çalısırsa oluyo (AttributeError: 'NoneType' object has no attribute 'ip_addr')
    ? ben kodu neden kulandınızı anlamadım o yüzden try execpt koyamam
    * -mirhanveekibi
    """
    user=get_user(str(username)) 
    if user.ip_addr==request.remote_addr:
        return render_template("home.html",user=user,loged_in=True)
    return f"Güvenlik sebebi nedeniyle buraya erişiminiz engellendi!"
@app.route("/create-account")
def createaccountpage():
    return render_template("createaccount.html")

#change
@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method=="POST":
        username = request.form['username']
        password = endtoend.password_hash(str(request.form['password']))
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
                        ...

                    with open(f"users/{username}/gelen.txt","w") as f:
                        ...
            except: 
                os.makedirs("users") 
                os.makedirs(f"users/{str(username)}")
                with open(f"users/{username}/giden.txt","w") as f:
                    pass

                with open(f"users/{username}/gelen.txt","w") as f:
                    pass
            db.session.add(user)
            db.session.commit()
        return redirect(url_for("home"))  
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