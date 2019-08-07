import random

from flask import url_for, request, redirect, render_template, Blueprint, g, session

from app.functions.cookie import getAFortune, getLuckyNumbers
from app.functions.horoscope import horoscopeTraits
from app.auth import login_required

bp = Blueprint('routes', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    if g.user:
        user = session['username']
        zodiac = session['zodiac']
    else:
        user = 'New Person'
        zodiac = 'Register an account for zodiac information'
    return render_template('index.html',user=user, zodiac=zodiac)

@bp.route('/cookie', methods = ['GET'])
#@login_required
def cookie():
    fortune = getAFortune()
    luckyNumber = getLuckyNumbers()
    return render_template('cookie.html', fortune=fortune, luckyNumber=luckyNumber)

@bp.route('/mystic9ball')
#@login_required
def mystic9ball():
    return render_template('m9.html')

@bp.route('/Horoscope')
@login_required
def horoscope():
    zodiac = session['zodiac'].capitalize()
    horoscope = horoscopeTraits(zodiac)
    return(horoscope)

@bp.route('/Genie')
#@login_required
def genie():
    return render_template('turtlejs.html')

@bp.route('/Mood Ring')
#@login_required
def moodRing():
	return render_template('mood.html', title = 'Mood Ring')

