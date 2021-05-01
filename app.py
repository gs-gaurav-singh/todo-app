from flask import Flask, render_template, request, redirect, url_for, session, g
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key = os.urandom(24)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user', None)

#         if request.form['password'] == 'cutom password': Enter your custom password
            session['user'] = request.form['username']
            return render_template('index.html')

    return render_template('login.html')


@app.route('/todo', methods=['GET', 'POST'])
def my_app():
    if g.user:
        if request.method == "POST":
            title = request.form['title']
            desc = request.form['desc']
            todo = Todo(title=title, desc=desc)
            db.session.add(todo)
            db.session.commit()

        alltodo = Todo.query.all()
        return render_template('index.html', alltodo=alltodo)
    return render_template('login.html')


@app.before_request
def before_request():
    g.user = None

    if 'user' in session:
        g.user = session['user']


@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if g.user:
        if request.method == "POST":
            title = request.form['title']
            desc = request.form['desc']
            todo = Todo.query.filter_by(sno=sno).first()
            todo.title = title
            todo.desc = desc
            db.session.add(todo)
            db.session.commit()
            return redirect('/todo')

        todo = Todo.query.filter_by(sno=sno).first()
        return render_template('update.html', todo=todo)
    return render_template('login.html')


@app.route('/delete/<int:sno>')
def delete(sno):
    if g.user:
        todo = Todo.query.filter_by(sno=sno).first()
        db.session.delete(todo)
        db.session.commit()
        return redirect('/todo')
    return redirect(url_for('login'))

@app.route('/logout')
def dropsession():
    session.pop('user', None)
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=False)
