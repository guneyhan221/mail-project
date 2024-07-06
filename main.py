from flask import *
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # SQLite veritabanı için URI
db = SQLAlchemy(app)

@app.route("home")
def home():
    ...
    
app.run(debug=True)