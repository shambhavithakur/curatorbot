## CuratorBot
### Introduction

CuratorBot downloads photos from specific repositories, including [WikiArt](https://www.wikiart.org/), resizes and optimizes the photos, and posts them on Twitter. Here is an overview of the steps it performs:

1. Download JavaScript Object Notation (JSON) data about photos.
2. Extract download links for each photo from the JSON data.
3. Using the links, download the photos to a folder.
4. Resize and optimize the photos.
5. Save the edited photos in a separate folder.
6. Select an edited photo.
7. Connect to Twitter via Tweepy.
8. Upload the selected photo to Twitter along with a status message.

Follow \#CuratorBot [@TheHazelEvans](https://twitter.com/TheHazelEvans). 

### Prerequisites

To be able to use CuratorBot as intended, you will need a [Twitter user](https://twitter.com/) account, a [Twitter developer](https://developer.twitter.com/en/apply-for-access.html) account, and [authentication tokens](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html). You should also have Python 3 installed on your computer and have access to a Windows Command Processor or Bash shell. The commands mentioned in the Installation section below were run in a Git Bash shell on a Windows 10 computer.

Although it is not necessary, I recommend that you use a code editor, such as [Microsoft Visual Studio Code](https://code.visualstudio.com/), or VS Code, to view and edit the CuratorBot code. A code editor offers various features, including error identification, error correction, and code formatting, that can simplify the coding process.

### Installation

1. On your computer, browse to a folder where you want to save the CuratorBot project.

2. Run the following command to clone the CuratorBot project in the folder, or get the [zipped version](https://github.com/tshambhavi/curatorbot/archive/master.zip) of the project.

    ```bash
    git clone https://github.com/tshambhavi/curatorbot.git
    ```
  
    <b>Note</b>: I used Git Bash to run the commands.
  
2. CD into the curatorbot folder, and run the following command to create a virtual environment: 

    ```bash
    python -m venv myvenv
    ```
  
    In the command above, myvenv is the name of the virtual environment. You can use any other name that makes sense to&nbsp;you.
  
3. Activate the virtual environment by running the following command:

    ```bash
    source myvenv/Scripts/activate
    ```
  
    You should now see `(myvenv)` above the command&nbsp;prompt.
    
4. To install the external modules that have been used in the project, make sure you are in the curatorbot folder and myvenv is active. Then, run the following command:

    ```bash
    pip install -r requirements.txt
    ```

5. Open the keys.py file, which is in the code folder, and add your Twitter authentication tokens to the&nbsp;file.

6. In the settings.py file, edit the path assigned to the TOP_LEVEL_PATH variable, if required. 

    Aside from editing TOP_LEVEL_PATH in settings.py, you can also add details about other WikiArt artists to the build_paths function in the file. For example, to obtain Ivan Shishkin's paintings, append the following chunk of code to the build_paths defintion. 

    ```python
    if number == 3:
        FOLDER_NAME = "ivan-shishkin"
        SHORT_NAME = "shishkin"
    ```

    In the code above, the FOLDER_NAME value is the artist's full name, lowercased and joined by hyphens. You can obtain the name from the WikiArt website. The SHORT_NAME variable should ideally be the artist's last name in lowercase. 

    Once you have chosen the SHORT_NAME, make sure that you add a folder bearing the SHORT_NAME to the curatorbot/code/assets/wiki folder—for example, curatorbot/code/assets/wiki/shishkin. And to the SHORT_NAME folder, add folders named img and img_large.

7. In download.py, in the get_json function, change the number of paintings you want to download per artist. In the main() function, edit the range—`for number in range(3)`—according to the number of artists you have in settings.py.

8. In tweet_data.py, in the prepare_tweet_data function, edit the following code according to the number of artists you have added to settings.py. 

    ```python
    number = randrange(3)
    ```
    For example, if you have added four artists, ranging from 0 to 3, replace `randrange(3)` with `randrange(4)`. The randrange function will then randomly select a number from 0 through 3 (inclusive), and the tweet_data.py function will use this number to decide which artist's painting should be tweeted.

9. In the tweet.py file, you could change the number of paintings you want to tweet during a session and the gap between each download.

### Use

1. In Bash, if you are in the curatorbot folder, run the following command to download meta data and paintings from WikiArt. If you are in the code folder, you can omit the 'code/' part.

    ```bash
    python code/download.py
    ```
  
 2. To tweet paintings, run the following command from the curatorbot folder in Bash:

       ```bash
       python code/tweet.py
       ```

### References:

* [Soviet Art Bot](https://github.com/veekaybee/soviet-art-bot)
* [Building a Twitter Art Bot](http://veekaybee.github.io/2018/02/19/creating-a-twitter-art-bot/)
