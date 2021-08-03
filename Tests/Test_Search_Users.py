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


class TestSearchusers(unittest.TestCase):
    def test_for_string(self):
        result = Search_Users.search_for_string(users)
        self.assertEqual(result, 'Francisca Rasmussen')

    def test_for_integer(self):
        result = Search_Users.search_for_integer(users)
        self.assertEqual(result, 101)

    def test_for_boolean(self):
        result = Search_Users.search_for_boolean(users)
        self.assertEqual(result, False)

    def test_for_list(self):
        result = Search_Users.search_for_list(users)
        self.assertEqual(result, ['Camptown', 'Glenville', 'Harleigh', 'Tedrow'])


if __name__ == '__main__':
    import Search_Users

    file_name = r'users.json'
    path_users = os.path.join(base_path, file_name)
    with open (path_users) as file_object:
        users = json.load (file_object)

    unittest.main()
