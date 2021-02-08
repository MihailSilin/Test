from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Mihail' } # выдуманный пользователь
    id = [ # список выдуманных пользователей
    {
    'user': { 'nickname': 'Sergey' },
    'id': '1'
    },
    {
    'user': { 'nickname': 'Ruslan' },
    'id': '2'
    }
    ]
    return render_template("index.html",
    title = 'Home', user = user, id = id)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for Nickaname="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', 
        title = 'Sign In',
        form = form)
        
        

        
