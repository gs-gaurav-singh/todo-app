# todo-app
Set your day-to-day routine here

## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements for this app.
```bash
pip install -r requirements.txt
```

## Imports
```python
from flask import Flask, render_template, request, redirect, url_for, session, g
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
```

## App creation
```python
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"
```

## Creating Database
```python
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key = os.urandom(24)
```

## Import database
```python
from app import db
db.create_all()
```
## Usage
Enter your customize username in app.py
```python
Add your custom password
if request.form['password'] == 'cutom password': Enter your custom password
```

## Contributing
Pull requests are welcome. 
