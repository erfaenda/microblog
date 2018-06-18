# -*- coding: utf-8 -*-
from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Царь Дадон'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Если у тебя есть бит, я его убил!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'КАУ каУУу каУУ кауУУ каУУУУУ'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        },
        {
            'author': {'username': 'Дэнчик Писька'},
            'body': 'Че тут вообще происходит такое'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)