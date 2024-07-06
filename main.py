from flask import *
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userdb.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

user_db=SQLAlchemy(app)

app.config['SQLALCHEMY_BINDS'] = {
    'other': 'sqlite:///other.db'
}

email_db=SQLAlchemy(app)

@app.route("home")
def home():
    ...

app.run(debug=True)