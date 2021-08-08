import unittest
from models import sources
Articles = sources.Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('NTV','Robert Maina','Launched in 2007' , 'the site is now the largest business news site on the web.','myner.com','myner.com7643t94.jpg','2021-04-11T07:57:16Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEqual(self.new_article.id,'NTV')
        self.assertEqual(self.new_article.author,'Robert Maina')
        self.assertEqual(self.new_article.title,'Launched in 2007')
        self.assertEqual(self.new_article.description,'the site is now the largest business news site on the web.')
        self.assertEqual(self.new_article.url,'myner.com')
        self.assertEqual(self.new_article.image,'myner.com7643t94.jpg')
        self.assertEqual(self.new_article.date,'2021-04-11T07:57:16Z')