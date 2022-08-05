import sqlite3
from flask import Flask, render_template, request, g, flash
import os
from FDataBase import FDataBase

#database settings
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
    db = get_bd()
    dbase = FDataBase(db)
    return render_template('index.html', tasks=dbase.get_tasks())


if __name__ == '__main__':
    app.run(debug=True)