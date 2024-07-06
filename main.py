from flask import *
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///database.db'  # SQLite veritabanı için URI
db = SQLAlchemy(app)
                
app.run(debug=True)