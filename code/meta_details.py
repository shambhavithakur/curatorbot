import json
from html import unescape
from collections import defaultdict


def get_metadata(text_file):
    """
    Extracts metadata about each painting from a relevant text file, stores the metadata by painting name in a dictionary, and returns the dictionary
    """

    meta_dict = defaultdict()

    try:
        with open(text_file, 'r') as input_file:
            data_list = json.load(input_file)
    except Exception as e:
        print(e)
        raise e

    for painting in data_list:
        artist = unescape(painting['artistName'])
        title = unescape(painting['title'])
        year = unescape(painting['year'])
        painting_url = unescape(painting["paintingUrl"])
        meta_text = [artist, title, year, painting_url]

        # Retrieve image name from link to image.
        index = painting['image'].rfind('/')
        image_name = painting['image'][index + 1:]

        try:
            meta_dict[image_name].append(meta_text)
        except KeyError:
            meta_dict[image_name] = (meta_text)

    return meta_dict
