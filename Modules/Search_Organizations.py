def display_search_items_organizations_database():
    '''
    This function displays the search items available in the organizations.json file.
    '''
    print('\nSearch Items:')
    print("\n_id")
    print("url")
    print("external_id")
    print("name")
    print("domain_names")
    print("created_at")
    print("details")
    print("shared_tickets")
    print("tags")


def receive_search_inputs_organizations_database(organizations):
    '''
    This function receives input from the user, modifies the input as needed by calling on other functions, and finally calls on the function search_organizations_database() which conducts the search and displays the results.
    '''
    search_item = input('\nPlease choose search item: ')

    if search_item == '_id':
        search_value = receive_integer_value_inputs_organizations_database()

    elif search_item == 'tags' or search_item == 'domain_names':
        search_value = receive_list_value_inputs_organizations_database()

    elif search_item == 'shared_tickets':
        search_value = receive_boolean_value_inputs_organizations_database()

    else:
        search_value = input('\nPlease choose search value: ')

    search_organizations_database(organizations, search_item, search_value)


def search_organizations_database(organizations, search_item, search_value):
    '''
    This function searches the database and displays the results.
    '''
    count = 0
    for index in range(0, len(organizations)):
        dict_tuple = organizations[index].items()
        for key, value in dict_tuple:
            if key == search_item and value == search_value:
                print('\n')
                for key, value in dict_tuple:
                    print(f'{key:<25} {value}')
                    count += 1
    if count == 0:
        print('No Results Found')


def receive_integer_value_inputs_organizations_database():
    '''
    This function converts string input from user into integer.
    '''
    search_value = input('\nPlease choose search value: ')
    search_value = int(search_value)
    return search_value


def receive_list_value_inputs_organizations_database():
    '''
    This function converts string input from the user into a list.
    '''
    list_of_values = []
    for i in range(4):
        search_value = input('Enter only one element at a time in order: ')
        list_of_values.append(search_value)
    search_value = list_of_values
    return search_value


def receive_boolean_value_inputs_organizations_database():
    '''
    This function converts string input from the user into a boolean.
    '''
    boolean_search_value = input('\nPlease enter true or false: ')
    if boolean_search_value == 'true':
        search_value = True
    elif boolean_search_value == 'false':
        search_value = False

    return search_value


# The following functions are used in the Tests Module
def search_for_string():
    '''
    This function is used by the Test_Search_Organization.py to determine that this module can read string values correctly.
    '''
    with open ('organizations.json') as file_object:
        organizations = json.load (file_object)

    found_string = organizations[0]['name']
    return found_string


def search_for_integer():
    '''
    This function is used by the Test_Search_Organization.py to determine that this module can read integer values correctly.
    '''
    with open ('organizations.json') as file_object:
        organizations = json.load (file_object)

    found_integer = organizations[4]['_id']
    return found_integer


def search_for_boolean():
    '''
    This function is used by the Test_Search_Organization.py to determine that this module can read boolean values correctly.
    '''
    with open ('organizations.json') as file_object:
        organizations = json.load (file_object)

    found_boolean = organizations[7]['shared_tickets']
    return found_boolean


def search_for_list():
    '''
    This function is used by the Test_Search_Organization.py to determine that this module can read list values correctly.
    '''
    with open ('organizations.json') as file_object:
        organizations = json.load (file_object)

    found_list = organizations[10]['tags']
    return found_list
