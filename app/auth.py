import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from app.models import User

#register blueprint
bp = Blueprint('auth', __name__, url_prefix='/auth')

#register account
@bp.route('/register', methods=['GET','POST'])
def register():

    if request.method == 'POST':
        #get information from form
        username = request.form['username']
        password = request.form['password']
        zodiac = request.form['zodiac']

        checkUser = User.query.filter_by(username=username).first()
        if checkUser is not None: #check if username already registered
            error = 'Username ' + str(username) + ' is already registered'
        else: 
            user = User(username=username, password_hash=(generate_password_hash(password)), zodiac=zodiac)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login')) #change to login page

        flash(error) #prints error message in base.html

    return render_template('auth/register.html', title='Register')

#login
@bp.route('/login', methods=['GET','POST'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        checkUser = User.query.filter_by(username=username).first()

        if checkUser is None: #check if username exists
            error = 'Username is not registered'
        elif not check_password_hash(checkUser.password_hash, password): #check password matches
            error = 'Incorrect password'
        else:
            user = checkUser
            session.clear()
            session['user_id'] = user.id
            session['username'] = user.username
            session['zodiac'] = user.zodiac
            return redirect(url_for('index')) #change to homepage

        flash(error) #prints error message in base.html

    return render_template('auth/login.html', title='Login')


#runs before view function, stores user information if logged in in g
@bp.before_app_request 
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()


#logout
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


#require login for certain features
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        
        if g.user is None: 
            return redirect(url_for('auth.login')) #change to homepage trying to access page without being logged in

        return view(**kwargs)

    return wrapped_view
