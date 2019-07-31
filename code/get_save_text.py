from pathlib import Path


def get_data(filepath):
    '''
    Returns a list containing items extracted from a text file
    '''
    list_from_file = []
    with open(filepath, 'r') as input_file:
        for line in input_file:
            # remove linebreak which is the last character of the string
            currentPlace = line[:-1]

            # add item to the list
            list_from_file.append(currentPlace)
    return list_from_file


def save_data(filepath, list):
    '''
    Extracts text items from a list and saves them in a file if they aren't already part of the file
    '''
    existing_data = []
    my_file = Path(filepath)
    if my_file.is_file():
        existing_data = get_data(filepath)
    with open(filepath, 'a+') as file:
        for item in list:
            if item not in existing_data:
                file.write(f'{item}\n')
