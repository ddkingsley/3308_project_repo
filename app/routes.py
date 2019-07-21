import random

from flask import Blueprint, g, render_template, session

from app.functions.cookie import getAFortune, getALuckyNumber
from app.auth import login_required
from app.db import get_db

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
    luckyNumber = getALuckyNumber()
    return render_template('cookie.html', title='Fortune Cookie', fortune=fortune, luckyNumber=luckyNumber)

@bp.route('/mystic9ball')
#@login_required
def mystic9ball():
	randomFortunes = ('you gonna be very rich', 'you gonna be rich')
	return(random.choice(randomFortunes))

@bp.route('/Horoscope')
#@login_required
def horoscope():
	return('this is your horoscope')

@bp.route('/Genie')
#@login_required
def genie():
    return('make a wish!')

@bp.route('/Mood Ring')
#@login_required
def moodRing():
	return render_template('mood.html', title = 'Mood Ring')

