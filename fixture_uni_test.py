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

# Another example

def check_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

def create_data():
    return ['level', 'step', 'peep', 'toot']

class TestPalindrome(unittest.TestCase):
    def setUp(self):
        # Initialize data here
        self.data = create_data()
    
    def test_func(self):
        expected_result = [True, False, True, True]
        data_checked = list(map(check_palindrome, self.data))
        # Verify the checked data here
        self.assertEqual(expected_result, data_checked )

    def tearDown(self):
        # Clear the data here
        self.data.clear()
