from calc import app
from flask import render_template
from forms import CalcForm

@app.route('/')
@app.route('/home')
def home():
    form = CalcForm()
    return render_template('home.html', form=form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
