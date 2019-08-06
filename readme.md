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

To be able to use CuratorBot as intended, you will need a [Twitter](https://twitter.com/) account, a [Twitter developer](https://developer.twitter.com/en/apply-for-access.html) account, and [access tokens](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html). You should also have Python 3 installed on your computer and have access to a Windows Command Processor or Bash shell. The commands mentioned in the Installation section below were run in the Git Bash shell on a Windows 10 computer.

Although it is not necessary, I recommend that you use a code editor, such as [Microsoft Visual Studio Code](https://code.visualstudio.com/), or VS Code, to view and edit the CuratorBot code. A code editor offes various features, including error identification, error correction, and code formatting, that can simplify the coding process.

### Installtion

1. On your computer, browse to a folder where you want to save the CuratorBot project.

2. Run the following code to clone the CuratorBot project into the folder or get the [zipped version](https://github.com/tshambhavi/curatorbot/archive/master.zip) of the project.

    ```bash
    https://github.com/tshambhavi/curatorbot.git
    ```
  
    <b>Note</b>: I used Git Bash to run the commands.
  
2. CD into the curatorbot folder, and run the following command to create a virtual environment. 

    ```bash
    python -m venv myvenv
    ```
  
    In command above, `myvenv` is the name of the virtual environment. You can use any other name that makes sense to you.
  
3. Activate the virtual environment by running the following command:

    ```bash
    source myvenv/Scripts/activate
    ```
  
    You should now see `(myvenv)` above the command-prompt path.

4. Open the kyes.py file, which is in the code folder, and add your Twitter access tokens.

5. In the settings.py file, edit the paths to your local folders if required.

6. In the tweet.py file, edit the number of paintings you want to tweet during a session and the gap between each download.

### Use

1. Make sure you are in the code folder and then run the following command to download meta data and paintings from WikiArt.

    ```bash
    python download.py
    ```
  
 2. To tweet paintings, run the following command:
 
   ```bash
   python tweet.py
   ```

### References:

* [Soviet Art Bot](https://github.com/veekaybee/soviet-art-bot)
* [Building a Twitter Art Bot](http://veekaybee.github.io/2018/02/19/creating-a-twitter-art-bot/)
