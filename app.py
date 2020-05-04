
from datetime import datetime
from flask import Flask
from flask import render_template
import sqlite3


app = Flask(__name__)


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


@app.route('/userview/mobiles')
def user_mobile():
    conn = sqlite3.connect(r"diona.db")
    results = conn.execute("SELECT * FROM AssetTablets")
    colNames = conn.execute("select group_concat(name,'|') from pragma_table_info('AssetTablets')")

    """Renders the user page."""
    return render_template(
        'userview.html',
        title='User View',
        tableRows = results,
        headers = colNames,
        year=datetime.now().year       
    )
