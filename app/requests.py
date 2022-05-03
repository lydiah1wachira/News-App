from multiprocessing import get_all_start_methods
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
      sources_results = process_results(sources_results_list)
      
  return sources_results