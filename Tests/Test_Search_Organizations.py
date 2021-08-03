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


class TestSearchOrganizations(unittest.TestCase):
    def test_for_string(self):
        result = Search_Organizations.search_for_string(organizations)
        self.assertEqual(result, 'Enthaze')

    def test_for_integer(self):
        result = Search_Organizations.search_for_integer(organizations)
        self.assertEqual(result, 105)

    def test_for_boolean(self):
        result = Search_Organizations.search_for_boolean(organizations)
        self.assertEqual(result, False)

    def test_for_list(self):
        result = Search_Organizations.search_for_list(organizations)
        self.assertEqual(result, ['Sheppard', 'Nunez', 'Bartlett', 'Giles'])


if __name__ == '__main__':
    import Search_Organizations

    file_name = r'organizations.json'
    path_organizations = os.path.join(base_path, file_name)
    with open (path_organizations) as file_object:
        organizations = json.load (file_object)

    unittest.main()
