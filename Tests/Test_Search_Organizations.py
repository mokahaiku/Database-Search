import unittest

class TestSearchOrganizations(unittest.TestCase):
    def test_for_string(self):
        result = Search_Organizations.search_for_string()
        self.assertEqual(result, 'Enthaze')

    def test_for_integer(self):
        result = Search_Organizations.search_for_integer()
        self.assertEqual(result, 105)

    def test_for_boolean(self):
        result = Search_Organizations.search_for_boolean()
        self.assertEqual(result, False)

    def test_for_list(self):
        result = Search_Organizations.search_for_list()
        self.assertEqual(result, ['Sheppard', 'Nunez', 'Bartlett', 'Giles'])

if __name__ == '__main__':
    unittest.main()
