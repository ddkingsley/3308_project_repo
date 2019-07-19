from flask import render_template
from flask import url_for
from app import app
import random
from app.functions.cookie import getAFortune, getLuckyNumbers

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'The Class'}   
    return render_template('index.html', user=user)

@app.route('/cookie', methods = ['POST', 'GET'])
def cookie():
    fortune = getAFortune()
    luckyNumber = getLuckyNumbers()
    return render_template('cookie.html', fortune=fortune, luckyNumber=luckyNumber)

@app.route('/mystic9ball')
def mystic9ball():
	randomFortunes = ('you gonna be very rich', 'you gonna be rich')
	return(random.choice(randomFortunes))

@app.route('/Horoscope')
def horoscope():
	return('this is your horoscope')

@app.route('/Genie')
def genie():
    return('make a wish!')

@app.route('/Mood Ring')
def moodRing():
	return render_template('mood.html')

