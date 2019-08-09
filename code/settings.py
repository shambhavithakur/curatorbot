"""
Accesses the keys and builds the URLs and pathnames that are used by other files to download, save, and retrieve painting data and tweet paintings

Example URLs
  https://www.wikiart.org/en/paintings-by-media/terracotta?json=2&page=1
  http://www.wikiart.org/en/App/Painting/PaintingsByArtist?artistUrl=claude-monet&json=2
"""

# Initializes keys
ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

# Gets keys
try:
    from keys import *
except Exception:
    pass

# Defines basic paths
BASE_URL = "https://www.wikiart.org/en/"
ARTIST_URL = "http://www.wikiart.org/en/App/Painting/PaintingsByArtist?artistUrl={}&json=2"
# Specifies local folder path as per OS requirements
TOP_LEVEL_PATH = 'C:\\projects\\curatorbot\\code\\'

# Specifies timeout settings for downloads from Wikiart
# https://github.com/lucasdavid/wikiart/blob/master/wikiart/settings.py
METADATA_REQUEST_TIMEOUT = 2 * 60

# Builds URLs and pathnames for each available category based on choice
def build_paths(number):
    if number == 0:
        FOLDER_NAME = "claude-monet"
        SHORT_NAME = "monet"
    if number == 1:
        FOLDER_NAME = "auguste-renoir"
        SHORT_NAME = "renoir"
    if number == 2:
        FOLDER_NAME = "konstantin-yuon"
        SHORT_NAME = "yuon"
    
    # Builds the relevant URLs, the path to the folder where images will be downloaded, 
    # and the name of the file that will store JSON data downloaded from Wikiart
    CUSTOM_URL = ARTIST_URL.format(FOLDER_NAME)
    ASSET_PATH = f'{TOP_LEVEL_PATH}assets\\wiki\\{SHORT_NAME}\\'
    METADATA_FILENAME = f'{SHORT_NAME}.txt'
    print(
        f"{''.center(30, '=')}\n{FOLDER_NAME.center(30)}\n{''.center(30, '=')}\n")

    # Sets path to the file that will store the JSON data 
    METADATA_FILE = f'{ASSET_PATH}{METADATA_FILENAME}'

    return FOLDER_NAME, CUSTOM_URL, ASSET_PATH, METADATA_FILE


