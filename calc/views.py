import config
from calc import app
from flask import render_template, request
from forms import WelcomeForm, CalcForm
from calculator import calculate, grades

global syllabus

@app.route('/', methods=['GET','POST'])
def home():
    form = WelcomeForm(request.form)
    calcform = CalcForm(request.form)

    if request.method == 'POST' and form.validate():
        if request.form['stream']:
            name = form.name.data
            stream = config.STREAM_CODE[request.form['stream']]
            global syllabus
            syllabus = config.STREAM[stream]
            return render_template('calc.html', name=name,
                                   syllabus = syllabus,
                                   stream = stream,
                                   grades = grades,
                                   calc = calcform)
        else:
            form.errors['stream'] = 'Please select a stream'
            return render_template('home.html', form = form,
                                   streams = config.STREAM_CODE)

    elif request.method == 'POST' and request.form['submit'] == 'Calculate':
        return render_template('result.html', result = calculate(request.form, syllabus))

    else:
        return render_template('home.html', form = form, 
                               streams = config.STREAM_CODE)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
