import unittest
import Search_Tickets

class TestSearchTickets(unittest.TestCase):
    def test_for_string(self):
        result = Search_Tickets.search_for_string()
        self.assertEqual(result, 'incident')

    def test_for_integer(self):
        result = Search_Tickets.search_for_integer()
        self.assertEqual(result, 9)

    def test_for_boolean(self):
        result = Search_Tickets.search_for_boolean()
        self.assertEqual(result, True)

    def test_for_list(self):
        result = Search_Tickets.search_for_list()
        self.assertEqual(result, ['Michigan', 'Florida', 'Georgia', 'Tennessee'])

if __name__ == '__main__':
    unittest.main()
