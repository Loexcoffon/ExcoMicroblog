from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/index')
def index():
    user = {'username': 'Lohann'}
    posts = [
        {
            'author': {'username': 'Samuel'},
            'body': 'Michael is cool!'
        },
        {
            'author': {'username': 'Michael'},
            'body': 'Samuel is sorta cool!'
        }
    ]
    return render_template('index.html', title='Comments', user=user, posts=posts)

@app.route('/songs')

def songs():
    songs = [
        {
            'artist': {'username': 'The Beatles'},
            'song': 'Let It Be'
        },
        {
            'artist': {'username': 'Michael Jackson'},
            'song': 'Billy Jean'
        }
    ]
    return render_template('songs.html', title='Songs', songs=songs)
