import sqlite3
from flask import Flask, render_template, redirect, g, flash, request, url_for
import os
from FDataBase import FDataBase


"""Database settings"""
DATABASE = '/tmp/app.db'
DEBUG = True
SECRET_KEY = 'vHWIERF73480GWEEFPsihbd!2432r3784hfrvb'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'app.bd')))


def connect_db():
    """Connecting database with settings setup created before"""
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def get_bd():
    if not hasattr(g, 'link_db'):
        g.link_bd = connect_db()
    return g.link_bd


@app.teardown_appcontext
def close_bd(error):
    if hasattr(g, 'link_bd'):
        g.link_bd.close()


def create_db():
    """Creating database"""
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


@app.route("/")
def index():
    """Getting all the tasks from database"""
    db = get_bd()
    dbase = FDataBase(db)
    return render_template('index.html', uncompleted_tasks=dbase.get_uncompleted_tasks(), completed_tasks=dbase.get_completed_tasks())


@app.route("/add_task", methods=['POST', 'GET'])
def add_task():
    """Add new task to 'to do' list """
    db = get_bd()
    dbase = FDataBase(db)
    if request.method == 'POST':
        dbase.add_task(request.form['title'], request.form['info'])
        flash('Task was successfully added!')
    return render_template('add_task.html')


@app.route('/make_complete/<id>')
def make_complete(id):
    """Mark a task as a completed one"""
    db = get_bd()
    dbase = FDataBase(db)
    dbase.make_complete(id)
    return redirect(url_for('index'))


@app.route("/delete_task/<id>")
def delete_task(id):
    """Deleting task from to do list"""
    db = get_bd()
    dbase = FDataBase(db)
    dbase.delete_task(id)
    return render_template('index.html', uncompleted_tasks=dbase.get_uncompleted_tasks(), completed_tasks=dbase.get_completed_tasks())


@app.route("/delete_all")
def delete_all():
    """Deleting all the tasks from to do list"""
    db = get_bd()
    dbase = FDataBase(db)
    dbase.delete_all()
    return render_template('index.html', uncompleted_tasks=dbase.get_uncompleted_tasks(), completed_tasks=dbase.get_completed_tasks())


if __name__ == '__main__':
    app.run(debug=True)