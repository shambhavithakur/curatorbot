"""
This code queries WikiArt and returns data categorized by artist name
"""

import settings
import word_list

import re
import json
import requests


from PIL import Image
from html import unescape
from wget import download

from sys import exit
from pathlib import Path
from os import path, listdir


class WikiDownloader():
    
    def __init__(self, number):
        '''
        Uses the builds_paths() function in the settings file to select an artist and generate paths and URLs pertaining to the artist
        '''
        self.FOLDER_NAME, self.CUSTOM_URL, self.ASSET_PATH, self.METADATA_FILE = settings.build_paths(
            number)

    def get_paths(self):
        return self.METADATA_FILE

    def substitute(self, text):
        return re.sub(r'[\s]+', '-', text)

    def create_meta_dict(self, title, artist, year, image_temp):
        '''
        Generates a dictionary that contains meta data about a painting of the chosen artist
        
        Format:
        {<image_name>: [<title>, <artist>, <year>, <painting_url>, <image_url>]}
        
        Example:
        {"landscape-1868.jpg": ["Landscape", "Pierre-Auguste Renoir", "1868", "/en/pierre-auguste-renoir/landscape-1868", 
        "https://uploads7.wikiart.org/images/pierre-auguste-renoir/landscape-1868.jpg"],}
        '''
        meta_dict = {}
        artist_url = (self.substitute(artist)).lower()

        index = image_temp.rfind('!')
        image_url = image_temp[:index]

        index_slash = image_url.rfind('/')
        image_name = image_url[index_slash + 1:]

        index_dot = image_name.rfind('.')
        image_name_minus_ext = image_name[:index_dot]
        painting_url = f'''/en/{artist_url}/{image_name_minus_ext}'''

        meta_text = [title, artist, year, painting_url, image_url]

        try:
            meta_dict[image_name].append(meta_text)
        except KeyError:
            meta_dict[image_name] = (meta_text)

        return meta_dict

    def get_json(self):
        """
        Gets JSON data about a specified number of paintings made by the artist who was chosen in the __init__() function
        Returns a dictionary containing data about the paintings
        """
        data_dict = {}
        json_url = self.CUSTOM_URL
        try:
            response = requests.get(
                json_url, timeout=settings.METADATA_REQUEST_TIMEOUT)

            if response.json():
                # Gets data about three paintings
                # The range can be modified as per requirements
                for number in range(0, 3):
                    painting_data = response.json()[number]
                    title = unescape(painting_data['title'])
                    has_word = word_list.prune_title(title)
                    if not has_word:
                        artist = unescape(painting_data['artistName'])
                        year = unescape(painting_data['yearAsString'])
                        image_temp = unescape(painting_data['image'])
                        meta_dict = self.create_meta_dict(
                            title, artist, year, image_temp)
                        data_dict.update(meta_dict)
                    else:
                        continue
        except requests.exceptions.RequestException as e:
            print(e)
            exit(1)
        return data_dict

    def get_dict_from_file(self, text_file):
        '''
        Accepts a text file and, if the file exists and is not empty, extracts its elements into a dictionary
        Returns the dictionary
        '''
        data_dict = {}
        file = Path(text_file)
        if file.is_file() and file.stat().st_size != 0:
            try:
                with open(text_file, 'r') as input_file:
                    data_dict = json.load(input_file)
            except Exception as e:
                print(e)
                raise e
        return data_dict

    def save_data(self, text_file, data_dict):
        """
        Saves the dictionary that is passed on to it as a text file
        If the text file already exists and contains items, updates the file using the data in the dicitonary
        """
        existing_dict = self.get_dict_from_file(text_file)
        existing_dict.update(data_dict)

        with open(text_file, 'w+') as output_file:
            json.dump(existing_dict, output_file)

    def get_image_links(self, text_file):
        """
        Converts a text file into a dictionary, and extracts painting names and links from each element in the dictionary
        """
        painting_tuples = []

        with open(text_file, 'r') as input_file:
            data_dict = json.load(input_file)

        for key in data_dict:
            tuple = (key, data_dict[key][-1])
            painting_tuples.append(tuple)

        return painting_tuples

    def download_images(self, tuple_list):
        """
        Accepts a list of painting names and links, downloads each painting, and saves it in a specified location
        """

        count = 0
        download_folder = f'{self.ASSET_PATH}img_large\\'

        downloaded_img_count = len([name for name in listdir(
            download_folder) if path.isfile(path.join(download_folder, name))])

        if len(tuple_list) == downloaded_img_count:
            print('Nothing to download')
        elif len(tuple_list) > downloaded_img_count:
            print(
                f'Going to download from {len(tuple_list) - downloaded_img_count} links')
        else:
            print(
                f'Going to download from {downloaded_img_count - len(tuple_list)} links')

        for element in tuple_list:
            image_name = element[0]
            image_link = element[1]
            file_location = f'{self.ASSET_PATH}img_large\\{image_name}'

            if image_name.endswith(('.png', '.jpg', '.jpeg')):
                if not path.isfile(file_location):
                    print(f"\nProcessing {image_name}")
                    try:
                        download(image_link, file_location)
                        count += 1
                    except Exception as e:
                        print(e)
                        continue
                
        print(f'\nDownloaded {count} photos\n')

    def resize_save_images(self):
        """
        Retrieves names of image files from a specified folder, resizes and compresses the image files, and saves them in a separate folder
        """

        folder_path = f'{self.ASSET_PATH}img_large\\'
        resized_folder_path = f'{self.ASSET_PATH}img\\'
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
                            if img.size[0] > 1024:
                                if path.getsize(image_path) > (max_size * 1024):
                                    basewidth = 1024
                                    width_percent = (
                                        basewidth / float(img.size[0]))
                                    horizontal_size = int(
                                        (float(img.size[1]) * float(width_percent)))
                                    img = img.resize(
                                        (basewidth, horizontal_size))
                                    count_resized += 1
                        except:
                            print(f'Could not resize {image}')
                            count_unresized += 1

                        if img.size[0] >= 506 and img.size[1] >= 512:
                            try:
                                img.save(resized_image_path,
                                         quality=88, optimize=True)
                                count_saved += 1
                            except:
                                print(
                                    f'Could not compress {image}. Not saving it.')

        print(
            f'resized = {count_resized}, unresized = {count_unresized}, saved={count_saved}')


def main():
    list = [1, 2, 3]
    for number in list:
        downloader = WikiDownloader(number)
        metadata_file = downloader.get_paths()
        data_list = downloader.get_json()
        downloader.save_data(metadata_file, data_list)
        links = downloader.get_image_links(metadata_file)
        downloader.download_images(links)
        downloader.resize_save_images()


if __name__ == '__main__':
    main()
