import unittest

from app.models import Article

class ArticlesTest(unittest.TestCase):
  '''
  Test Class to test the behaviour of the Articles class
  '''
  def setUp(self):
    '''
    Set up method that will run before every test
    '''
    self.new_article = Article('Severus Snape','Harry Potter defeats He who must not be named', 'Lorem ipsum dolor sit adipiscing elit.','https://www.wizardingworld.com/', 'https://www.wizardingworld.com/', '2022-05-02T08:45:18Z','gfygft7fqd wf gdcod c')

  def test_instance(self):
    
    self.assertTrue(isinstance(self.new_article,Article))

    