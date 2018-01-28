import sqlite3, os
from flask import Flask, request, render_template, g, redirect, url_for
from sqlalchemy import func, create_engine, MetaData, Table
from sqlalchemy.sql import select
from sqlalchemy.orm import mapper, sessionmaker


app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'timesheet.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    # Closes the database again at the end of the request.
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def history():
    db = get_db()
    cur = db.execute('select day, hours, comment from entries order by id desc')
    items = cur.fetchall()
    total = 0
    for item in items:
        total += float(item["hours"])
    return render_template('show_entries.html', total=total, entries=items)

@app.route('/add', methods=['POST'])
def add_entry():
    db = get_db()
    db.execute('insert into entries (hours, day, comment) values (?, ?, ?)',
                 [request.form['hours'], request.form['day'], request.form['comment']])
    db.commit()
    return history()

