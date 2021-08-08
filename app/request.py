from app import app
import urllib.request,json
from .models import sources

Source = sources.Source

# Getting the url
api_key = app.config['NEWS_API_KEY']

base_url = app.config["NEWS_SOURCES_BASE_URL"]


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
	Function that processes the news sources results and turns them into a list of objects
	Args:
		sources_list: A list of dictionaries that contain sources details
	Returns:
		sources_results: A list of sources objects
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