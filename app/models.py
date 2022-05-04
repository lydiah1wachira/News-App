class Source:
  '''
  Source class to define news Source Objects
  '''
  def __init__(self, id, name, description, language, source_url):
    self.id = id
    self.name = name
    self.description = description
    self.language = language
    self.source_url = source_url

class Article:
  '''
  class to define new article objects
  '''
  def __init__(self, id, author,title,description, article_url, image_url,publishedAt, content):
    self.id = id
    self.author = author
    self.title = title
    self.description = description
    self.article_url = article_url
    self.image_url = image_url
    self.publishedAt = publishedAt
    self.content = content

    


