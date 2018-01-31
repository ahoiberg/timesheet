import sqlite3, os
from datetime import datetime
from flask import Flask, request, render_template, g, redirect, url_for
import sqlalchemy
from sqlalchemy import func, create_engine, Table, Column, Integer, Date, String, MetaData, ForeignKey
from sqlalchemy.sql import select
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy_utils import database_exists, create_database



app = Flask(__name__)
app.config.from_object(__name__)

engine = create_engine('sqlite:////Users/andrewhoiberg/personal_projects/timesheet/timesheet.db', echo=True)
if not database_exists(engine.url):
    create_database(engine.url)

print(database_exists(engine.url))

metadata = MetaData()

entries = Table('entries', metadata,
     Column('id', Integer, primary_key=True),
     Column('hours', Integer),
     Column('day', Date),
     Column('comment', String),
)

metadata.create_all(engine)


@app.route('/')
def history():
    db = engine.connect()
    print("connected")
    cur = entries.select()
    print("selected entries")
    items = db.execute(cur)
    print("executed")
    print(items)
    total = 0
    e = []
    for item in items:
        total += float(item["hours"])
        e.append(item)
    return render_template('show_entries.html', total=total, entries=e)

@app.route('/add', methods=['POST'])
def add_entry():
    db = engine.connect()
    d = list(map(int, request.form['day'].split('-')))
    print(d[0])
    d = datetime(d[0], d[1], d[2])
    cur = entries.insert().values(hours=request.form['hours'], day=d, comment=request.form['comment'])
    # db.execute('insert into entries (hours, day, comment) values (?, ?, ?)',
    #              [request.form['hours'], request.form['day'], request.form['comment']])
    db.execute(cur)
    return history()

