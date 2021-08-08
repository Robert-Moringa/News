from app import app
import urllib.request,json
from .models import sources

Source = sources.Source
Articles=sources.Articles

# Getting the url
api_key = app.config['NEWS_API_KEY']

base_url = app.config["NEWS_SOURCES_BASE_URL"]

articles_url = app.config["ARTICLES_URL"]


def getNews_sources(category):
	'''
	GetNews function gets response from the url request
	'''
	get_sources_url = base_url.format(category,api_key)

	with urllib.request.urlopen(get_sources_url) as url:
		get_sources_data = url.read()
		get_sources_response = json.loads(get_sources_data)

		sources_results = None

		if get_sources_response['sources']:
			sources_results_list = get_sources_response['sources']
			sources_results = process_the_sources(sources_results_list)

	return sources_results

def process_the_sources(sources_list):
	'''
	Function that processes the news sources results and transforms them to list of objects
	'''
	sources_results = []

	for source_item in sources_list:
		id = source_item.get('id') 
		name = source_item.get('name')
		description = source_item.get('description')
		url = source_item.get('url')
		category = source_item.get('category')


		sources_object = Source(id,name,description,url,category)
		sources_results.append(sources_object)


	return sources_results


def get_articles(id):
	'''
	A function that returns a list of articles objects
	'''
	get_articles_url = articles_url.format(id,api_key)

	with urllib.request.urlopen(get_articles_url) as url:
		articles_results = json.loads(url.read())


		articles_object = None
		if articles_results['articles']:
			articles_object = process_articles(articles_results['articles'])

	return articles_object

def process_articles(articles_list):
	'''
    Function that processes the articles results and transforms them to list of objects
	'''
	articles_object = []
	for article_item in articles_list:
		id = article_item.get('id')
		author = article_item.get('author')
		title = article_item.get('title')
		description = article_item.get('description')
		url = article_item.get('url')
		image = article_item.get('urlToImage')
		date = article_item.get('publishedAt')
		
		if image:
			articles_result = Articles(id,author,title,description,url,image,date)
			articles_object.append(articles_result)	
		


	return articles_object