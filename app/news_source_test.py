import unittest
from models import sources
Source = sources.Source

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('CNN','CNN News','Cable News Newtork that is a leader in providing news worldwide','cnn.com','general')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

    def test_to_check_instance_variables(self):
        self.assertEqual(self.new_source.id,'CNN')
        self.assertEqual(self.new_source.name,'CNN News')
        self.assertEqual(self.new_source.description,'Cable News Newtork that is a leader in providing news worldwide')
        self.assertEqual(self.new_source.url,'cnn.com')
        self.assertEqual(self.new_source.category,'general')

if __name__ == '__main__':
    unittest.main()