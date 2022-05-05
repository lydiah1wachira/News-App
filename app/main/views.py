from flask import render_template,request,redirect, url_for
from . import main
from ..requests import get_sources,get_articles



@main.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''
  business_sources = get_sources('business')
  tech_sources =get_sources('technology')
  politics_sources = get_sources('politics')
  sports_sources = get_sources('sports')

  print('business_sources')

  title = 'The Daily Prophet'
  
  
  return render_template('index.html', title= title, technology = tech_sources, business = business_sources, politics=politics_sources,sports = sports_sources)


@main.route('/source/<id>')
def article(id):
    '''
    view articles function that returns a list of articles on the articles
    '''

    article = get_articles(id)
    title = 'Top Headlines'
    print(title)
  

    return render_template('articles.html', article = article)  