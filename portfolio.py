from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View

app = Flask('__name__')
Bootstrap(app)
nav = Nav()

##############
### NAVBAR ###
##############

@nav.navigation()
def mynavbar():
    return Navbar(
        'AT',
        View('Home', 'index'),
        View('Sprint 1', 'viz')
    )

nav.init_app(app)

##############
### ROUTES ###
##############

@app.route('/')
def index():
    return render_template('index.html', title="Andrew's Page")


@app.route('/analysis')
def viz():
    return render_template('sprint1Summary.slides.html')