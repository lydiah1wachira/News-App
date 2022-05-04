import urllib.request,json
from .models import Source,Article

api_key = None

base_url = None

articles_url = None

def configure_request(app):
  global api_key,base_url,articles_url
  api_key = app.config['NEWS_API_KEY']
  base_url = app.config['NEWS_API_BASE_URL']
  articles_url = app.config['ARTICLES_BASE_URL']

def get_sources():
  '''
   Function that gets the json response to our url request
  '''
  get_sources_url = base_url.format(api_key)

  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)

    source_results = None 

    if get_sources_response['results']:
      sources_results_list = get_sources_response['results']
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
    language = source_item.get('language')
    source_url = source_item.get('source_url')

    source_object = Source(id, name, description, language, source_url)

    source_results.append(source_object)

  return source_results

def get_articles(source):
  get_articles_url =  articles_url.format(source, api_key)

  with urllib.request.urlopen(get_articles_url) as url:
    articles_data = url.read()
    articles_response =json.loads(articles_data)

    get_articles_results = None

    if articles_response['articles']:
      articles_results_list = articles_response['articles']
      articles_results = process_article_results(articles_results_list)

  return (articles_results)

def process_article_results(articles_results_list):
  '''
  Function to process the Article results and transforms them to a list of objects
  '''
  articles_results = []

  for article_item in articles_results_list:
    author = article_item.get('author')
    title = article_item.get('title')
    description = article_item.get('description')
    article_url = article_item.get('article_url')
    image_url = article_item.get('image_url')
    publishedAt = article_item.get('publishedAt')
    content = article_item.get('content')

    articles_object = Article(author, title, description, article_url, image_url, publishedAt, content)

    articles_results.append(articles_object)

  return articles_results



    




   
  




