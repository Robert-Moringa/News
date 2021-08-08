from flask import render_template
from app import app
from .request import getNews_sources

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    business = getNews_sources('business')
    sports = getNews_sources('sports')
    tech = getNews_sources('technology')
    entertainment = getNews_sources('entertainment')

    return render_template('index.html', business = business, sports = sports )