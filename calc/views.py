import config
from calc import app
from flask import render_template, request
from forms import WelcomeForm, CalcForm

@app.route('/', methods=['GET','POST'])
def home():
    form = WelcomeForm(request.form)
    calcform = CalcForm(request.form)

    if request.method == 'POST' and form.validate():
        name = form.name.data
        stream = config.STREAM_CODE[request.form['stream']]
        return render_template('calc.html', name=name, 
                               syllabus = config.STREAM[stream],
                               stream = stream,
                               calc = calcform)

    elif request.method == 'POST' and calcform.validate():
        return render_template('result.html')

    else:
        return render_template('home.html', form = form, 
                               streams = config.STREAM_CODE)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
