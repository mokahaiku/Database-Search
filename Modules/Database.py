import pathlib
import os  # File directory manipulations


def organizations_data_base(base_path):
    """From rows of the csv table, creates lists for each organizations' data and places them within another list."""

    file_name = r'organizations.json'
    path = os.path.join(base_path, file_name)  # Concatenates file directory paths.

    with open(path) as birthday_file:
        reader = csv.reader(birthday_file)
        headers = next(reader)  # Eliminates the header from the csv file to enter the list.
        for row in reader:
            organizations.append(row)

    return organizations


def tickets_data_base(base_path):
    """Returns all tickets from the text file, tickets.txt."""

    file_name = r'tickets.json'
    path = os.path.join(base_path, file_name)  # Concatenates file directory paths.

    with open(path) as file_object:

        tickets = file_object.readlines()

    return tickets


def users_data_base(base_path):
    """Returns all tickets from the text file, tickets.txt."""

    file_name = r'users.json'
    path = os.path.join(base_path, file_name)  # Concatenates file directory paths.

    with open(path) as file_object:

        tickets = file_object.readlines()

    return tickets
