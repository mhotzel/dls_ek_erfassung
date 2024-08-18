from app import app
from flask import render_template, request, redirect, session, flash, url_for, send_from_directory, g
from os.path import join
from .user import User, Role
from .user_manager import UserManager, TestUserManager

um: UserManager = TestUserManager()


@app.before_request
def check_user():

    if not request.path.startswith('/restricted/'):
        return
    
    user = um.get_user_by_id(session['USERNAME'])

    if user:
        g.user = user
        return    

    return redirect('/login')


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    session['USERNAME'] = ''
    if request.method == 'GET':
        return render_template("login.html")
    else:
        user_id = request.form.get("username")
        passwd = request.form.get("password")
        user_from_db = um.get_user_by_id(user_id)
        if user_from_db and user_from_db.passwd_valid(passwd):
            session['USERNAME'] = user_from_db.id
            flash("Login erfolgreich", 'info')
            return redirect("/restricted/uebersicht")
        else:
            flash("Login fehlerhaft", 'error')
            return redirect('/login')


@app.route("/testseite")
def testseite():
    return render_template("testseite.html", user=session['USERNAME'])


@app.route('/restricted/uebersicht')
def uebersicht():
    return render_template("uebersicht.html", user=g.user)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
