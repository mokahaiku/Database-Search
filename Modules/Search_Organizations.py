def display_search_items():
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


def receive_search_inputs(organizations):
    '''
    This function receives input from the user, modifies the input as needed by calling on other functions, and finally calls on the function search_organizations() which conducts the search and displays the results.
    '''
    search_item = input('\nPlease choose search item: ')

    if search_item == '_id':
        search_value = receive_integer_inputs()

    elif search_item == 'tags' or search_item == 'domain_names':
        search_value = receive_list_inputs()

    elif search_item == 'shared_tickets':
        search_value = receive_boolean_inputs()

    else:
        search_value = input('\nPlease choose search value: ')

    search_organizations(organizations, search_item, search_value)


def search_organizations(organizations, search_item, search_value):
    '''
    This function searches the database and displays the results.
    '''
    count = 0
    for index in range(len(organizations)):
        dict_tuple = organizations[index].items()
        for key, value in dict_tuple:
            if key == search_item and value == search_value:
                print('\n')
                for key, value in dict_tuple:
                    print(f'{key:<25} {value}')
                    count += 1
    if count == 0:
        print('No Results Found')


def receive_integer_inputs():
    '''
    This function converts string input from user into integer.
    '''
    search_value = input('\nPlease choose search value: ')
    search_value = int(search_value)
    return search_value


def receive_list_inputs():
    '''
    This function converts string input from the user into a list.
    '''
    values = []
    for i in range(4):
        search_value = input('Enter only one element at a time in order: ')
        values.append(search_value)
    search_value = values
    return search_value


def receive_boolean_inputs():
    '''
    This function converts string input from the user into a boolean.
    '''
    boolean_value = input('\nPlease enter true or false: ')
    if boolean_value == 'true':
        search_value = True
    elif boolean_value == 'false':
        search_value = False

    return search_value


# These functions are used in the Tests Module.
def search_for_string(organizations):
    '''
    This function is used by the Test_Search_Organization.py to determine that this module can read string values correctly.
    '''
    found_string = organizations[0]['name']
    return found_string


def search_for_integer(organizations):
    '''
    This function is used by the Test_Search_Organization.py to determine that this module can read integer values correctly.
    '''
    found_integer = organizations[4]['_id']
    return found_integer


def search_for_boolean(organizations):
    '''
    This function is used by the Test_Search_Organization.py to determine that this module can read boolean values correctly.
    '''
    found_boolean = organizations[7]['shared_tickets']
    return found_boolean


def search_for_list(organizations):
    '''
    This function is used by the Test_Search_Organization.py to determine that this module can read list values correctly.
    '''
    found_list = organizations[10]['tags']
    return found_list
