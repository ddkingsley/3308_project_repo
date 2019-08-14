import random

from flask import url_for, request, redirect, render_template, Blueprint, g, session

from app.functions.cookie import getAFortune, getLuckyNumbers
from app.functions.horoscope import horoscopeTraits, horoscopeFortuneGenerator
from app.functions.advice import getAdvice
from app.auth import login_required

#register blueprint
bp = Blueprint('routes', __name__)

#homepage
@bp.route('/')
@bp.route('/index')
def index():
    if g.user: #if user logged in
        user = session['username']
        zodiac = session['zodiac']
    else: #if not logged in
        user = 'New Person'
        zodiac = 'Register an account today'
    return render_template('index.html',user=user, zodiac=zodiac)

#fortune cookie
@bp.route('/cookie', methods = ['GET'])
def cookie():
    fortune = getAFortune()
    luckyNumber = getLuckyNumbers()
    return render_template('cookie.html', fortune=fortune, luckyNumber=luckyNumber, title = 'Fortune Cookie')

#mystic 9-ball
@bp.route('/mystic9ball')
def mystic9ball():
    return render_template('m9.html', title = 'Mystic 9-Ball')

#Horoscope
@bp.route('/Horoscope', methods =['POST', 'GET'])
def horoscope():
    if request.method == 'POST':
        sign = request.form['zodiac']
        fortune = request.form['fortunes']
        horoscope = horoscopeFortuneGenerator(fortune)
        trait = horoscopeTraits(sign)
        return render_template('horoscopeOutput.html', horoscope=horoscope, trait=trait, title = 'Horoscope')

    return render_template('horoscope.html', title='Horoscope')
    
#Genie
@bp.route('/Genie')
def genie():
    return render_template('turtlejs.html', title = 'Genie')

#Mood Ring
@bp.route('/Mood Ring')
def moodRing():
	return render_template('mood.html', title = 'Mood Ring')

#Advice
@bp.route('/Advice')
@login_required #only logged in users can access
def advice():
    advice = getAdvice()
    return render_template('advice.html', advice=advice, title = 'Advice')

