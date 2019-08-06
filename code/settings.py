"""
Puts together URLs and pathnames, which are used by other files to download, save, and retrieve painting data and tweet paintings
"""

# Example URLs
# https://www.wikiart.org/en/paintings-by-media/terracotta?json=2&page=1
# https://www.wikiart.org/en/paintings-by-style/cubo-expressionism?json=2&page=1

BASE_URL = "https://www.wikiart.org/en/"
TYPE_STYLE = 'paintings-by-style/'
TYPE_GENRE = 'paintings-by-genre/'
TYPE_MEDIA = 'paintings-by-media/'
JSON_PAGINATION = "?json=2&page="
# Specifies a path as per OS requirements
TOP_LEVEL_PATH = 'C:\\projects\\curator_bot\\code\\'

# Specifies timeout settings for downloads from Wikiart
# https://github.com/lucasdavid/wikiart/blob/master/wikiart/settings.py

METADATA_REQUEST_TIMEOUT = 2 * 60
PAINTINGS_REQUEST_TIMEOUT = 5 * 60


# Builds URLs and pathnames for each available category based on choice
def build_paths(choice):
    if choice == 0:
        FOLDER_NAME = "pastorale"
        SHORT_NAME = "pasto"
        CUSTOM_URL = f"{BASE_URL}{TYPE_GENRE}{FOLDER_NAME}{JSON_PAGINATION}"
        ASSET_PATH = f'{TOP_LEVEL_PATH}assets\\wiki\\{SHORT_NAME}\\'
        METADATA_FILENAME = f'{SHORT_NAME}.txt'
    if choice == 1:
        FOLDER_NAME = "cubo-expressionism"
        SHORT_NAME = "cubo"
        CUSTOM_URL = f"{BASE_URL}{TYPE_STYLE}{FOLDER_NAME}{JSON_PAGINATION}"
        ASSET_PATH = f'{TOP_LEVEL_PATH}assets\\wiki\\{SHORT_NAME}\\'
        METADATA_FILENAME = f'{SHORT_NAME}.txt'
    if choice == 2:
        FOLDER_NAME = "terracotta"
        SHORT_NAME = "terra"
        CUSTOM_URL = f"{BASE_URL}{TYPE_MEDIA}{FOLDER_NAME}{JSON_PAGINATION}"
        ASSET_PATH = f'{TOP_LEVEL_PATH}assets\\wiki\\{SHORT_NAME}\\'
        METADATA_FILENAME = f'{SHORT_NAME}.txt'
    if choice == 3:
        FOLDER_NAME = "cloisonnism"
        SHORT_NAME = "clois"
        CUSTOM_URL = f"{BASE_URL}{TYPE_STYLE}{FOLDER_NAME}{JSON_PAGINATION}"
        ASSET_PATH = f'{TOP_LEVEL_PATH}assets\\wiki\\{SHORT_NAME}\\'
        METADATA_FILENAME = f'{SHORT_NAME}.txt'
    if choice == 4:
        FOLDER_NAME = "cityscape"
        SHORT_NAME = "city"
        CUSTOM_URL = f"{BASE_URL}{TYPE_GENRE}{FOLDER_NAME}{JSON_PAGINATION}"
        ASSET_PATH = f'{TOP_LEVEL_PATH}assets\\wiki\\{SHORT_NAME}\\'
        METADATA_FILENAME = f'{SHORT_NAME}.txt'
    if choice == 5:
        FOLDER_NAME = "fauvism"
        SHORT_NAME = "fauv"
        CUSTOM_URL = f"{BASE_URL}{TYPE_STYLE}{FOLDER_NAME}{JSON_PAGINATION}"
        ASSET_PATH = f'{TOP_LEVEL_PATH}assets\\wiki\\{SHORT_NAME}\\'
        METADATA_FILENAME = f'{SHORT_NAME}.txt'
    if choice == 6:
        FOLDER_NAME = "veduta"
        SHORT_NAME = "veduta"
        CUSTOM_URL = f"{BASE_URL}{TYPE_GENRE}{FOLDER_NAME}{JSON_PAGINATION}"
        ASSET_PATH = f'{TOP_LEVEL_PATH}assets\\wiki\\{SHORT_NAME}\\'
        METADATA_FILENAME = f'{SHORT_NAME}.txt'
    if choice == 7:
        FOLDER_NAME = "mixed-media"
        SHORT_NAME = "mixed"
        CUSTOM_URL = f"{BASE_URL}{TYPE_MEDIA}{FOLDER_NAME}{JSON_PAGINATION}"
        ASSET_PATH = f'{TOP_LEVEL_PATH}assets\\wiki\\{SHORT_NAME}\\'
        METADATA_FILENAME = f'{SHORT_NAME}.txt'
    if choice == 8:
        FOLDER_NAME = "oilcloth"
        SHORT_NAME = "oil"
        CUSTOM_URL = f"{BASE_URL}{TYPE_MEDIA}{FOLDER_NAME}{JSON_PAGINATION}"
        ASSET_PATH = f'{TOP_LEVEL_PATH}assets\\wiki\\{SHORT_NAME}\\'
        METADATA_FILENAME = f'{SHORT_NAME}.txt'
    # Sets path to the file that will store JSON data downloaded from Wikiart
    METADATA_FILE = f'{ASSET_PATH}{METADATA_FILENAME}'

    return FOLDER_NAME, CUSTOM_URL, ASSET_PATH, METADATA_FILE


# print(METADATA_FILE)
# print(f'{CUSTOM_URL}{str(1)}')
# print(f'#{str(FOLDER_NAME)}\n#CuratorBot')
