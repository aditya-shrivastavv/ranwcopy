# `ranwcopy` ✨

Python program which generates random words and sentences and copy them to clipboard🗒️.

## Features

- 👍 Excellent command line experience.
- 🙂 User friendly.
- 🔊 Produces sound so you don't have to start at it.
- 🔁 Auto copy to clipboard🗒️
- 💡 Intuitive help menu

## Setup

1. Clone repo

     ```bash copy
     git clone https://github.com/aditya-shrivastavv/bing-reward-script.git

     cd bing-reward-script/
     ```

2. Install required libraries

     ```py copy
     pip install -r requirements.txt
     ```

3. (**Optional**)
    **WINDOWS**
    The script is ready to use, but if you want to access it from anywhere, then you have to add it to the path which is show in this step

    1. Open this directory in the windows file explorer
    2. Copy the path from the bar below title bar
    3. Search for **Edit environment variables** in the windows search menu, then open it
    4. Under the **User variables** double click **Path**
    5. Click on **New** and paste the copied path there
    6. Click **OK** > **OK**

    ✅ Added to the path, restart the terminal session to start using the *commmand*

    ---
    **LINUX**

    Add the script to your PATH

    ```bash copy
    cp ranwcopy /usr/local/bin
    ```

    ✅ Added to the path, restart the terminal session to start using the *commmand*

## Commands

Help menu

```bash copy
ranwcopy -h
#OR
ranwcopy --help
```

Start generating words (10 default with 8 seconds gap)

```bash copy
ranwcopy
```

Generate 20 words with 9 seconds gap

```py copy
ranwcopy -i 20 -g 9
# or
ranwcopy --iterations 20 --timegap 9
```

## Possible Use Cases

I made this script to get rewards 🍭 from **Bing Searches**. Bing gives points when you make searches on it. Those points can then be converted into Amazon / Flipcart Giftcards.

## Flow

1. First run the command, to get the javascript code on your clipboards which automatically searches the words on the search engine

    ```bash copy
    ranwcopy --gethelper
    ```

2. Open the Bing search page or any page that appears after searching anything on bing
3. Open browser Devtools
4. Under the tabs, click on `+` icon and add **Rendering** tab
5. Open **Rendering** > Check mark "*Emulate focused page*" (***This is very important***)
6. On the console paste the javascript code, don't run it yet.
7. Run command (on shell) and return to browser

    ```bash copy
    ranwcopy -i 10 -g 8
    ```

8. On the browser keep running the javascript code everytime you hear beep sound.
