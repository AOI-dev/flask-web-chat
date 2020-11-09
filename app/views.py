from . import app
from .database import test_create, test_select, test_select_all

from flask import render_template

@app.route('/')
def index():
    test_create()
    print('DATABASE CREATED')
    data_all = test_select_all()
    print('DATA ALL:', data_all)
    data = test_select("admin")
    print('DATA SELECT:', data)
    return render_template('index.html', data = data, data_all = data_all)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    return "<h2>this is login<h2>"

@app.route('/reg', methods = ['GET', 'POST'])
def reg():
    return "<h2>this is reg<h2>"

