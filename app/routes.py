from flask import render_template
from flask import url_for
from app import app
import random
from app.functions.cookie import getAFortune

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'The Class'}   
    return render_template('index.html', user=user)

@app.route('/cookie/')
def cookie():
    fortune = {'theFortune' : getAFortune()}
    return render_template('cookie.html', fortune=fortune)

@app.route('/mystic9ball')
def mystic9ball():
	randomFortunes = ('you gonna be poor', 'you gonna be rich')
	return(random.choice(randomFortunes))

@app.route('/Horoscope')
def horoscope():
	return('this is your horoscope')

@app.route('/Genie')
def genie():
    return('make a wish!')

@app.route('/Mood Ring')
def moodRing():
	randomMood = ('good mood', 'bad mood')
	return(random.choice(randomMood))
