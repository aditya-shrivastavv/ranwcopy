# Random Word Copy to Clipboard

Python program to generate random words and copy them to clipboard

## Features

- Custom number of words to generate
- Custom time gap between word generation
- Beep sound when text is ready to be pasted
- Auto mount word to clipboard
- Supports CLI arguments

## Usage

Install required libraries

```py copy
pip install -r requirements.txt
```

Add the script to your PATH

- Linux
  
  ```bash copy
  cp ranwcopy /usr/local/bin
  ```

- Windows
  
  ```bash copy
  setx /M PATH "%PATH%;<your-new-path>"
  ```

Start generating words (10 default)

```bash copy
ranwcopy
```

Generate 20 words

```py copy
ranwcopy -i 20
# or
ranwcopy --iterations 20
```

Get Help

```py copy
ranwcopy --help
```

## Possible Use Cases

- I made this script to get rewards from **Bing Searches**. Bing gives points when you make searches on it. Those points can then be converted into Amazon / Flipcart Giftcards.
