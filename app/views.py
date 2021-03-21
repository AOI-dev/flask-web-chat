from . import app
from .database import test_create, test_select, test_select_all, add_user, select_all_messages, add_message, \
    user_exists, user_entered_the_pass

from flask import render_template, request, make_response, session, redirect, escape, url_for

app.secret_key = '12354'


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
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pass']
        print(username, password)
        session["username"] = username
        # if user_exists(username=username) and user_entered_the_pass(username=username, password=password):
        #     session['username'] = request.form['username']
    return render_template('login.html')


@app.route('/logout')
def logout():
    # удалить из сессии имя пользователя, если оно там есть
    session.pop('username', None)
    return f"<H1>Вышел</H1>"


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    data_all = select_all_messages()
    if request.method == 'POST':
        if not session['username']:
            return redirect(url_for('login'))
        else:
            add_message(username=session['username'], message=request.form['message'])
            return redirect(url_for('chat'))
            # return 'Logged in as %s' % escape(session['username']) + render_template('chat.html', data_all=data_all)
    return render_template('chat.html', data_all=data_all)


@app.route('/get_messages')
def get_messages():
    data_all = select_all_messages()
    if not session['username']:
        return redirect(url_for('login'))
    else:
        result = ""
        for i in range(len(data_all)):
            result += data_all[i][0] + " " + data_all[i][1]+"<br>"
        return result


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["pass"]
        print(user_exists(username=username))
        if not user_exists(username=username):
            add_user(username=username, password=password)
            return "Получил" + username + " " + password
        else:
            return "ЮЗЕР УЖЕ ЗАРЕГАН"
    else:
        return render_template('reg.html')


@app.route('/session')
def sess():
    try:
        if session['username']:
            return f"<F1>{session['username']}</F1>"
    except Exception:
        return redirect(url_for('login'));
