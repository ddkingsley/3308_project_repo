from flask import render_template
from flask import url_for
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'The Class'}   
    return render_template('index.html', user=user)

@app.route('/cookie/')
def cookie():
    return render_template('cookie.html')
