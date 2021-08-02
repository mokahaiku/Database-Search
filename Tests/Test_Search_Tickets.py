import unittest
import json
import sys
import yaml
import pathlib
import os  # File directory manipulations


config_file_path = ('C:\OrangeShine\Config\config.yml')

def yaml_loader(config_file_path):
    with open (config_file_path, "r") as file_descriptor:
        data = yaml.load (file_descriptor, Loader=yaml.FullLoader)

    return data

data = yaml_loader (config_file_path)

files = data.get('files')
base_path = (files['base_path'])
modules_path = (files['modules_path'])

sys.path.append(modules_path) # Finds modules in the indicated directory.

class TestSearchTickets(unittest.TestCase):
    def test_for_string(self):
        result = Search_Tickets.search_for_string(tickets)
        self.assertEqual(result, 'incident')

    def test_for_integer(self):
        result = Search_Tickets.search_for_integer(tickets)
        self.assertEqual(result, 9)

    def test_for_boolean(self):
        result = Search_Tickets.search_for_boolean(tickets)
        self.assertEqual(result, True)

    def test_for_list(self):
        result = Search_Tickets.search_for_list(tickets)
        self.assertEqual(result, ['Michigan', 'Florida', 'Georgia', 'Tennessee'])

if __name__ == '__main__':
    import Search_Tickets

    file_name = r'tickets.json'
    path_tickets = os.path.join(base_path, file_name)
    with open (path_tickets) as file_object:
        tickets = json.load (file_object)

    unittest.main()
