def display_search_items():
    '''
    This function displays the search items available in the tickets.json file.
    '''
    print('\nSearch Items:')
    print("_id")
    print("url")
    print("external_id")
    print("created_at")
    print("type")
    print("subject")
    print("description")
    print("priority")
    print("status")
    print("submitter_id")
    print("assignee_id")
    print("organization_id")
    print("tags")
    print("has_incidents")
    print("due_at")
    print("via")


def receive_search_inputs(tickets):
    '''
    This function receives input from the user, modifies the input as needed by calling on other functions, and finally calls on the function search_tickets() which conducts the search and displays the results.
    '''
    search_item = input('\nPlease choose search item: ')

    if (
    search_item == 'submitter_id' or
    search_item == 'assignee_id' or
    search_item == 'organization_id'):
        search_value = receive_integer_inputs()

    elif search_item == 'tags':
        search_value = receive_list_inputs()

    elif search_item == 'has_incidents':
        search_value = receive_boolean_inputs()

    else:
        search_value = input('\nPlease choose search value: ')

    search_tickets(tickets, search_item, search_value)


def search_tickets(tickets, search_item, search_value):
    '''
    This function searches the database and displays the results.
    '''
    count = 0
    for index in range(0, len(tickets)):
        dict_tuple = tickets[index].items()
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


# These Functions are used for the Tests Module.
def search_for_string(tickets):
    '''
    This function is used by the Test_Search_Tickets.py to determine that this module can read string values correctly.
    '''
    found_string = tickets[0]['type']
    return found_string


def search_for_integer(tickets):
    '''
    This function is used by the Test_Search_Tickets.py to determine that this module can read integer values correctly.
    '''
    found_integer = tickets[4]['submitter_id']
    return found_integer


def search_for_boolean(tickets):
    '''
    This function is used by the Test_Search_Tickets.py to determine that this module can read boolean values correctly.
    '''
    found_boolean = tickets[7]['has_incidents']
    return found_boolean


def search_for_list(tickets):
    '''
    This function is used by the Test_Search_Tickets.py to determine that this module can read list values correctly.
    '''
    found_list = tickets[10]['tags']
    return found_list
