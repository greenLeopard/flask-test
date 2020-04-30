from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dr Stupid'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': "I'm definitely not day drinking."
        },
        {
            'author': {'username': 'Susan'},
            'body': "Is that a gin bottle behind your back?"
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
