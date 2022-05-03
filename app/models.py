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

