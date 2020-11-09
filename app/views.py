from . import app
from .database import test_create, test_select, test_select_all, add_user, select_all_messages, add_message

from flask import render_template, request


@app.route('/')
def index():
    # test_create()
    # print('DATABASE CREATED')
    data_all = test_select_all()
    print('DATA ALL:', data_all)
    # data = test_select("admin")
    # print('DATA SELECT:', data)
    return render_template('index.html', data_all=data_all)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == 'POST':
    #
    # else:
    #     # show_the_login_form()
    return render_template('login.html')


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        add_message(username="user123", message=request.form["message"])
    data_all = select_all_messages()
    return render_template('chat.html', data_all=data_all)


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["pass"]
        add_user(username=username, password=password)
        return "Получил" + username + " " + password
    else:
        return render_template('reg.html')

