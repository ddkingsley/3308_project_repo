import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from app.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        zodiac = request.form['zodiac']

        checkUser = User.query.filter_by(username=username).first()
        if checkUser is not None:
            error = 'Username ' + str(username) + ' is already registered'
        else:
            user = User(username=username, password_hash=(generate_password_hash(password)), zodiac=zodiac)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html', title='Register')


@bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        checkUser = User.query.filter_by(username=username).first()

        if checkUser is None:
            error = 'Username is not registered'
        elif not check_password_hash(checkUser.password_hash, password):
            error = 'Incorrect password'
        else:
            user = checkUser
            session.clear()
            session['user_id'] = user.id
            session['username'] = user.username
            session['zodiac'] = user.zodiac
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html', title='Login')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
