import settings
from time import sleep
from pathlib import Path
from random import choice
from tweepy import TweepError
from config import create_api
from meta_details import get_metadata
from get_save_text import get_data, save_data

'''
Tweets paintings and related metadata
'''

count = 0

while count < 5:
    metadata_filepath = settings.METADATA_FILE
    meta_dict = get_metadata(metadata_filepath)

    # Selects a metadata item from meta_dict
    selected_metadata = choice(list(meta_dict.items()))

    image_name = selected_metadata[0]
    artist = selected_metadata[1][0]
    title = selected_metadata[1][1]
    year = selected_metadata[1][2]

    # Checks whether the selected image has already been tweeted
    tweeted_images = []
    tweeted_images_file_path = f'{settings.TOP_LEVEL_PATH}tweeted_images.txt'
    tweeted_images_file = Path(tweeted_images_file_path)
    if tweeted_images_file.is_file():
        tweeted_images = get_data(tweeted_images_file_path)

    if image_name not in tweeted_images:
        # Obtains the path to the selected image
        index = (metadata_filepath.rfind('\\')) + 1
        image_path = f"{metadata_filepath[:index]}img\\{image_name}"

        # Defines status text for tweet
        status_text = f"{title}\n{artist}, {year}\n\n#WikiArt\n#{settings.FOLDER_NAME}\n#CuratorBot"

        # Sends tweet
        api = create_api()

        is_uploaded = False

        while not is_uploaded:
            try:
                # Runs Tweepy command
                api.update_with_media(image_path, status=status_text)
                # Appends the name of the uploaded image to tweeted_images.txt
                save_data(tweeted_images_file_path, [image_name])
                count += 1
                is_uploaded = True
            except TweepError as e:
                print(e.api_code)
                print("  .. failed, sleeping for 5 seconds and then trying again.")
                sleep(5)
    sleep(1800)
