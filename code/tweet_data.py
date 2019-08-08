from pathlib import Path
from random import choice, randrange

import settings
import word_list
from meta_details import get_metadata_artists
from get_save_text import get_data, convert_for_hashtag


def prepare_tweet_data():
    '''
    Selects the artist whose painting will be tweeted and generates relevant paths and URLs
    Generates a dictionary that contains meta data about the artist's paintings and selects a painting from the dictionary
    Returns the name of the selected painting, the path to the local folder where the painting is saved, the status message that will accompany
    the tweeted painting, and the path to the file where names of tweeted paintings are stored
    '''

    image_name = ''
    image_path = ''
    status_text = ''
    tweeted_images_file_path = ''

    # Selects a category of paintings
    # The upperlimit in randrange is not inclusive
    number = randrange(4)

    FOLDER_NAME, CUSTOM_URL, ASSET_PATH, METADATA_FILE = settings.build_paths(
        number)
    metadata_filepath = METADATA_FILE

    meta_dict = get_metadata_artists(metadata_filepath)        

    # Selects a metadata item from meta_dict
    selected_metadata = choice(list(meta_dict.items()))

    title = selected_metadata[1][0]
    if len(title) < 4:
        title = "Another Painting"
    image_name = selected_metadata[0]
    artist = selected_metadata[1][1]
    year = selected_metadata[1][2]
    painting_url = selected_metadata[1][3]

    # Prepares to check whether the selected image has already been tweeted
    tweeted_images = []
    tweeted_images_file_path = f'{settings.TOP_LEVEL_PATH}tweeted_images.txt'
    tweeted_images_file = Path(tweeted_images_file_path)

    # If the tweeted-images file exists, retrieves image names from the file
    if tweeted_images_file.is_file():
        tweeted_images = get_data(tweeted_images_file_path)

    if image_name not in tweeted_images:
        # Obtains the local path to the selected image
        index = (metadata_filepath.rfind('\\')) + 1
        image_path = f"{metadata_filepath[:index]}img\\{image_name}"

        # Generates URL of image
        url = f"https://www.wikiart.org{painting_url}"
        
        # Returns a blank url if the link is broken
        response = requests.head(url)
        if response.status_code < 400:
            url = '  ' + url
        else:
            url = ''

        # Converts the folder name for use as a hashtag
        folder_name = convert_for_hashtag(FOLDER_NAME)

        # Defines status text for tweet
        status_text = f"{title}\n{artist}, {year}\n\n#WikiArt #{folder_name} #CuratorBot{url}"

    return image_name, image_path, status_text, tweeted_images_file_path
