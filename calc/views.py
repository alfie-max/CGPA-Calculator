from calc import app

@app.route('/')
@app.route('/index')
def index():
    return 'This is the Index Page'
