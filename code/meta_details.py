import json


def get_metadata_artists(text_file):
    """
    Extracts the dictionary that has been saved in the meta.txt file for the selected artist
    """

    data_dict = {}

    try:
        with open(text_file, 'r') as input_file:
            data_dict = json.load(input_file)
    except Exception as e:
        print(e)
        raise e

    return data_dict
