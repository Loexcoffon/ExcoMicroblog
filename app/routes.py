from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/songs')

def index():
    user = {'username': 'Lohann'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


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
