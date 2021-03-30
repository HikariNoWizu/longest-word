# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask, render_template, request, session
from game import Game
from flask_session.__init__ import Session

app = Flask(__name__)
# Check Configuration section for more details
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.route('/')
def home():
    game = Game()
    return render_template('home.html', grid=game.grid, score=session.get('score', '0'))

@app.route('/check', methods=["POST"])
def check():
    game = Game()
    game.grid = list(request.form['grid'])
    word = request.form['word']
    is_valid = game.is_valid(word)
    if 'score' in session:
        session['score'] += 1
    else:
        session['score'] = 1
    return render_template('check.html', is_valid=is_valid, grid=game.grid, word=word)