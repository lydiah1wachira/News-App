import unittest

from app.models import Source

class SourceTest(unittest.TestCase):
  '''
  Test class to test the behaviour of the Source class
  '''
  def setUp(self):
    '''
    Set up method that will run before every test
    '''
    self.new_source = Source("new-york-times", "The New York Times", "All  the News That's Fit to Print","en","https://www.nytimes.com/international/")

  def test_instance(self):
    
    self.assertTrue(isinstance(self.new_source,Source))

