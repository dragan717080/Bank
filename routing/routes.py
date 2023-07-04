from flask import render_template, Blueprint
from flask_login import current_user

index_pages = Blueprint('index', __name__, url_prefix='/')

@index_pages.route('/')
def index():
    if current_user.is_anonymous:
        return render_template('index.html')
    return render_template('index.html', loggedinuser=current_user.username)

@index_pages.route('/', methods=['POST'])
def index_post():
    return render_template('index.html')
