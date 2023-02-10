from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/songs')

def songs():
    user = {'username': 'Lohann'}
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
    return render_template('songs.html', title='Home', user=user, songs=songs)

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
    return render_template('index.html', title='Home', user=user, posts=posts)
