from flask import render_template
from . import main
from ..requests import get_sources


@main.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''
  sources = get_sources()
  print(sources)
  title = 'Home - News Highlights'
  return render_template('index.html', title= title, sources = sources)