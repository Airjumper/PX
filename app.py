
from datetime import datetime
from flask import Flask
from flask import render_template
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/vsonline/workspace/PX/diona.db'
app.config['SECRET_KEY'] = 'PX2002'


# login_manager = LoginManager()
# login_manager.init_app(app)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'welcome.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/userview')
def userview():
    """Renders the user page."""
    return render_template(
        'userview.html',
        title='User View',
        year=datetime.now().year
    )

@app.route('/login')
def login():
    """Renders the user page."""
    return render_template(
        'login.html',
        title='Login Page',
        year=datetime.now().year
    )

