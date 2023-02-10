from flask import render_template
from app import app

@app.route('/')
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
