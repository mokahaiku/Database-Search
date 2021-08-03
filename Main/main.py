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


if __name__ == '__main__':

    import Search_Organizations
    import Search_Tickets
    import Search_Users


    file_name = r'organizations.json'
    path_organizations = os.path.join(base_path, file_name)
    with open (path_organizations) as file_object:
        organizations = json.load (file_object)

    file_name = r'tickets.json'
    path_tickets = os.path.join(base_path, file_name)
    with open (path_tickets) as file_object:
        tickets = json.load (file_object)

    file_name = r'users.json'
    path_users = os.path.join(base_path, file_name)
    with open (path_users) as file_object:
        users = json.load (file_object)


    search_database = input('Search for organizations, tickets, users (input 1, 2, 3): ' )

    if search_database == '1':
        Search_Organizations.display_search_items()
        Search_Organizations.receive_search_inputs(organizations)

    elif search_database == '2':
        Search_Tickets.display_search_items()
        Search_Tickets.receive_search_inputs(tickets)

    elif search_database == '3':
        Search_Users.display_search_items()
        Search_Users.receive_search_inputs(users)
