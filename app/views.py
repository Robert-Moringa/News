from flask import render_template
from app import app
from .request import getNews_sources,get_articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general = getNews_sources('general')
    business = getNews_sources('business')
    sports = getNews_sources('sports')
    tech = getNews_sources('technology')
    entertainment = getNews_sources('entertainment')
    science = getNews_sources('science')
    health = getNews_sources('health')
    
    print(general)

    return render_template('index.html', health = health, science = science, business = business, sports = sports, tech = tech, entertainment = entertainment , general = general)

@app.route('/articles/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)

	return render_template('articles.html', articles = articles)