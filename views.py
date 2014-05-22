from flask import render_template
from app import app


# Create the mappings of both URLs to function index()
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'edk'}  # fake user
    posts =  [ # array of placeholder posts of user
        {
            'author': {'nickname': 'Bob'},
            'body': 'Blue skies!'
        },
        {
            'author': {'nickname': 'Jessica'},
            'body': 'Bobocop!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)
