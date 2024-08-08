from app import app
from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from os.path import join


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    session['USERNAME'] = ''
    if request.method == 'GET':
        return render_template("login.html")
    else:
        if request.form.get("username") == 'matthias' and request.form.get("password") == 'wurst':
            session['USERNAME'] = 'matthias'
            flash("Login erfolgreich", 'info')
            return redirect("/uebersicht")
        else:
            flash("Login fehlerhaft", 'error')
            return redirect('/login')


@app.route("/testseite")
def testseite():
    if session['USERNAME']:
        return render_template("testseite.html")
    else:
        return redirect('/login')


@app.route('/uebersicht')
def uebersicht():
    if session['USERNAME']:
        return render_template("uebersicht.html")
    else:
        return redirect('/login')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
