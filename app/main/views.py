from flask import render_template,request,redirect, url_for
from . import main
from ..requests import get_sources,get_articles
from ..models import Source,Article


@main.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''
  sources = get_sources()
  
  title = f'{sources.name}'


  return render_template('index.html', title= title, sources = sources)

@main.route('/source/<id>')
def articles(id):
  '''
  View Articles page function that returns the Article-list  details and its data
  '''
  business_aricles= get_articles('business')
  tech_articles = get_articles('technology')
  politics_articles=get_articles('politics')
  sports_articles = get_articles('sports')

  print(tech_articles)

  return render_template('articles.html', business = business_aricles, technology = tech_articles, politics = politics_articles, sports = sports_articles)
  