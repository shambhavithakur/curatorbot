from time import sleep, time
import tweet_data
from tweepy import TweepError
from config import create_api
from get_save_text import save_data


'''
Tweets paintings and related metadata
'''


def send_tweet():
    image_name, image_path, status_text, tweeted_images_file_path = tweet_data.prepare_tweet_data()

    # Sends tweet
    api = create_api()

    try:
        # Runs Tweepy command
        api.update_with_media(image_path, status=status_text)
        # Appends the name of the uploaded image to tweeted_images.txt
        save_data(tweeted_images_file_path, [image_name])
        print(f'Uploaded {image_name}...')
    except TweepError as e:
        print(e.api_code)
        print("  .. failed, sleeping for 5 seconds and then trying again")
        sleep(5)


count = 0
while count < 2:

    send_tweet()
    count += 1

    if count < 2:
        print(f'Will upload another in ...')

        for i in range(1800, -1, -1):
            start = time()
            print(f'\t{i} seconds...', end='\r')
            sleep(1.0 - ((time() - start) % 1.0))
    else:
        print(f"Uploaded the required {count} files...")
