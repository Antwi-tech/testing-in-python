# Fixture is the preparation needed to create/ perform oen or more tests
# Fixture setup, fixture teardown. The implementtion syntax change here. Here they are methods . 
# the correct namineng is setUp and tearDown

import unittest

class TestWord(unittest.TestCase):
    # Fixture setup method
    def setUp(self):
        # Initialize the word banana here
        self.word = 'banana'

    # Test method
    def test_the_word(self):
        # Add the tests here
        self.assertNotIn('B', self.word)
        self.assertNotIn('y', self.word)
        self.assertIn('b', self.word)
    
    # Fixture teardown method
    def tearDown(self):
        # Delete the word variable here
        del self.word

