def display_search_items():
    '''
    This function displays the search items available in the users.json file.
    '''
    print('\nSearch Items:')
    print("_id")
    print("url")
    print("external_id")
    print("name")
    print("alias")
    print("created_at")
    print("active")
    print("verified")
    print("shared")
    print("locale")
    print("timezone")
    print("last_login_at")
    print("email")
    print("phone")
    print("signature")
    print("organization_id")
    print("tags")
    print("suspended")
    print("role")


def receive_search_inputs(users):
    '''
    This function receives input from the user, modifies the input as needed by calling on other functions, and finally calls on the function search_users() which conducts the search and displays the results.
    '''
    search_item = input('\nPlease choose search item: ')

    if search_item == '_id' or search_item == 'organization_id':
        search_value = receive_integer_inputs()

    elif search_item == 'tags':
        search_value = receive_list_inputs()

    elif (
    search_item == 'active' or
    search_item == 'verified' or
    search_item == 'shared' or
    search_item == 'suspended'):
        search_value = receive_boolean_inputs()

    else:
        search_value = input('\nPlease choose search value: ')

    search_users(users, search_item, search_value)


def search_users(users, search_item, search_value):
    '''
    This function searches the database and displays the results.
    '''
    count = 0
    for index in range(0, len(users)):
        dict_tuple = users[index].items()
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
    This function converts string input from user into list.
    '''
    values = []
    for i in range(4):
        search_value = input('Enter only one element at a time in order: ')
        values.append(search_value)
    search_value = values
    return search_value


def receive_boolean_inputs():
    '''
    This function converts string input from user into boolean.
    '''
    boolean_value = input('\nPlease enter true or false: ')
    if boolean_value == 'true':
        search_value = True
    elif boolean_value == 'false':
        search_value = False

    return search_value


# These functions are used in the Tests Module.
def search_for_string(users):
    '''
    This function is used by the Test_Search_Users.py to determine that this module can read string values correctly.
    '''
    found_string = users[0]['name']
    return found_string


def search_for_integer(users):
    '''
    This function is used by the Test_Search_Users.py to determine that this module can read integer values correctly.
    '''
    found_integer = users[4]['organization_id']
    return found_integer


def search_for_boolean(users):
    '''
    This function is used by the Test_Search_Users.py to determine that this module can read boolean values correctly.
    '''
    found_boolean = users[7]['active']
    return found_boolean


def search_for_list(users):
    '''
    This function is used by the Test_Search_Users.py to determine that this module can read list values correctly.
    '''
    found_list = users[10]['tags']
    return found_list
