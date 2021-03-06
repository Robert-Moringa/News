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
        self.new_source = Source('NTV','NTV News','The Covid 19 infections are on an alarming rise, be warned!','ntv.com','general')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

    def test_to_check_instance_variables(self):
        self.assertEqual(self.new_source.id,'NTV')
        self.assertEqual(self.new_source.name,'NTV News')
        self.assertEqual(self.new_source.description,'The Covid 19 infections are on an alarming rise, be warned!')
        self.assertEqual(self.new_source.url,'ntv.com')
        self.assertEqual(self.new_source.category,'general')

if __name__ == '__main__':
    unittest.main()