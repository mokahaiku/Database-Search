import unittest
import Search_Users

class TestSearchusers(unittest.TestCase):
    def test_for_string(self):
        result = Search_Users.search_for_string()
        self.assertEqual(result, 'Francisca Rasmussen')

    def test_for_integer(self):
        result = Search_Users.search_for_integer()
        self.assertEqual(result, 101)

    def test_for_boolean(self):
        result = Search_Users.search_for_boolean()
        self.assertEqual(result, False)

    def test_for_list(self):
        result = Search_Users.search_for_list()
        self.assertEqual(result, ['Camptown', 'Glenville', 'Harleigh', 'Tedrow'])

if __name__ == '__main__':
    unittest.main()
