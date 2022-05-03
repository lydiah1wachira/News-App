
import urllib.request,json
from .models import Source

api_key = None

base_url = None

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

  




