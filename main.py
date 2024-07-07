from flask import *
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userandposts.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
#a
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
    print("merhaba")
    return render_template("home.html",loged_in=False)


app.run(debug=True)