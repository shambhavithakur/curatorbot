"""
This code queries WikiArt and returns data from the category that is chosen in settings.py
"""

from PIL import Image
import requests
import shutil
import json
from os import path, listdir
from sys import exit
import settings

# from PIL import ImageFile
# ImageFile.LOAD_TRUNCATED_IMAGES = True


def get_json():
    """
    Gets JSON data about a category of paintings from WikiArt, and returns a list of objects containing data specific to each painting
    """

    for page in range(1, 2):
        url = settings.CUSTOM_URL + str(page)
        print(page, "pages processed")
        try:
            response = requests.get(
                url, timeout=settings.METADATA_REQUEST_TIMEOUT)
            # json_data = response.json()
            if response.json()['Paintings']:
                data = response.json()['Paintings']
        except requests.exceptions.RequestException as e:
            print(e)
            exit(1)
    return data


def save_data(text_file, data_list):
    """
    Saves the list of objects returned by get_json() as a text file
    """
    with open(text_file, 'a+') as output_file:
        json.dump(data_list, output_file)


def get_image_links(text_file):
    """
    Converts the text file into a list, and extracts image links from each object in the list
    """
    painting_links = []

    with open(text_file, 'r') as input_file:
        data_list = json.load(input_file)

    for painting in data_list:
        painting_links.append(painting['image'])

    return painting_links


def download_images(links):
    """
    Accepts a list of links to images, downloads each image, and saves it in a specified location
    """
    print(f'Going to download from {len(links)} links')
    count = 0
    for link in links:
        image_name = link.rsplit('/', 1)[1]
        file_location = f'{settings.ASSET_PATH}img_large\\{image_name}'

        if image_name.endswith(('.png', '.jpg', '.jpeg')):
            if not path.isfile(file_location):
                print("Processing", link)
                try:
                    response = requests.get(link,
                                            timeout=settings.METADATA_REQUEST_TIMEOUT, stream=True)
                except requests.exceptions.RequestException as e:
                    print(e)
                    return

                with open(str(file_location), 'wb') as outfile:
                    shutil.copyfileobj(response.raw, outfile)
                    count += 1

    print(f'Downloaded {count} photos')


def resize_save_images():
    """
    Retrieves names of image files from a specified folder, resizes and compresses the image files and saves them in a separate folder
    """

    folder_path = f'{settings.ASSET_PATH}img_large\\'
    resized_folder_path = f'{settings.ASSET_PATH}img\\'
    images = listdir(folder_path)
    max_size = 100

    count_resized = 0
    count_unresized = 0
    count_saved = 0

    for image in images:
        if image.endswith(('.png', '.jpg', '.jpeg')):
            image_path = folder_path + image
            resized_image_path = resized_folder_path + image

            if path.isfile(image_path):
                if not path.isfile(resized_image_path):
                    img = Image.open(image_path)
                    try:
                        if img.size[0] > 500:
                            if path.getsize(image_path) > (max_size * 1024):
                                basewidth = 500
                                width_percent = (
                                    basewidth / float(img.size[0]))
                                horizontal_size = int(
                                    (float(img.size[1]) * float(width_percent)))
                                img = img.resize(
                                    (basewidth, horizontal_size), Image.ANTIALIAS)
                                count_resized += 1
                    except:
                        print(f'Could not resize {image}')
                        count_unresized += 1

                    try:
                        img.save(resized_image_path, quality=85, optimize=True)
                        count_saved += 1
                    except:
                        print(f'Could not compress {image}. Not saving it.')

    print(
        f'resized = {count_resized}, unresized = {count_unresized}, saved={count_saved}')


def main():
    data_list = get_json()
    save_data(settings.METADATA_FILE, data_list)
    links = get_image_links(settings.METADATA_FILE)
    download_images(links)
    resize_save_images()


if __name__ == '__main__':
    main()
