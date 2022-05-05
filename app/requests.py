from app import create_app
import urllib.request,json
from .models import Source,Article

api_key = None

base_url = None

articles_url = None

def configure_request(app):
  global api_key,base_url,articles_url
  api_key = 'da9f91b5fb274533ae16ec9618b97312'
  base_url = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
  articles_url = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'

def get_sources(category):
  '''
   Function that gets the json response to our url request
  '''
  get_sources_url = base_url.format(category, api_key)

  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)

    source_results = None 

    if get_sources_response['sources']:
      sources_results_list = get_sources_response['sources']
      source_results = process_results(sources_results_list)

  return source_results

def process_results(source_list):
  '''
  Function that processes the sources results and transforms them to a list of Objects
  '''
  source_results = []
  for source_item in source_list:

    id = source_item.get('id')
    name = source_item.get('name')
    description = source_item.get('description')
    category = source_item.get('category')
    language = source_item.get('language')
    source_url = source_item.get('source_url')

    source_object = Source(id, name, description, category, language, source_url)

    source_results.append(source_object)

  return source_results

def get_articles(id):
  get_articles_url =  articles_url.format(id,api_key)

  with urllib.request.urlopen(get_articles_url) as url:
    articles_data = url.read()
    articles_response =json.loads(articles_data)

    articles_results = None

    if articles_response['articles']:
      articles_results_list = articles_response['articles']
      articles_results = process_article_results(articles_results_list)

  return (articles_results)

def process_article_results(articles_list):
  '''
  Function to process the Article results and transforms them to a list of objects
  '''
  articles_results = []

  for article_item in articles_list:
    id = article_item.get('id')
    author = article_item.get('author')
    title = article_item.get('title')
    description = article_item.get('description')
    article_url = article_item.get('article_url')
    image_url = article_item.get('image_url')
    publishedAt = article_item.get('publishedAt')
    content = article_item.get('content')

    if image_url:
      articles_object = Article(id,author, title, description, article_url, image_url, publishedAt, content)

      articles_results.append(articles_object)

  return articles_results



    




   
  




