import settings
from pathlib import Path
from random import choice, randrange
from meta_details import get_metadata
from get_save_text import get_data, convert_for_hashtag


def prepare_tweet_data():
    '''
    Consolidates the content that will be tweeted and returns relevant information
    '''
    # Selects a category of paintings
    # The upperlimit in randrange is not inclusive
    number = randrange(9)
    # print(number)
    # number = 0

    FOLDER_NAME, CUSTOM_URL, ASSET_PATH, METADATA_FILE = settings.build_paths(
        number)
    metadata_filepath = METADATA_FILE
    meta_dict = get_metadata(metadata_filepath)

    # Selects a metadata item from meta_dict
    selected_metadata = choice(list(meta_dict.items()))

    image_name = selected_metadata[0]
    artist = selected_metadata[1][0]
    title = selected_metadata[1][1]
    year = selected_metadata[1][2]
    painting_url = selected_metadata[1][3]

    # Prepares to check whether the selected image has already been tweeted
    tweeted_images = []
    tweeted_images_file_path = f'{settings.TOP_LEVEL_PATH}tweeted_images.txt'
    tweeted_images_file = Path(tweeted_images_file_path)
    if tweeted_images_file.is_file():
        tweeted_images = get_data(tweeted_images_file_path)

    if image_name not in tweeted_images:
        # Obtains the path to the selected image
        index = (metadata_filepath.rfind('\\')) + 1
        image_path = f"{metadata_filepath[:index]}img\\{image_name}"

        # Generates URL of image
        url = f"https://www.wikiart.org{painting_url}"

        # Edits folder name in URL
        folder_name = convert_for_hashtag(FOLDER_NAME)

        # Defines status text for tweet
        status_text = f"{title}\n{artist}, {year}\n\n#WikiArt\n#{folder_name}\n#CuratorBot\n\n{url}"
    return image_name, image_path, status_text, tweeted_images_file_path
