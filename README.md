# OPTC Infographic

A simple python script to create OPTC infographics

## Prerequisites

Python 3 or above

## Usage

### Input using sugofest.json

- Rename `sugofest.json.sample` to `sugofest.json`
- Open `sugofest.json` in a text editor
- Modify each of the lists with the character ID of the boosted character
- **Optional Step** - Create an `images` folder in the same directory and add a `background.png` file to use as the background graphic. If this step is not done, the background will be a static aqua blue color (does not look that good)
- Run the script using the following command
```
$ python main.py
```
- Follow the instructions on screen for urls for the banner and the Dates of each of the parts
- Infographic output will be generated at: `images\infographic.png`

This is how the `sugofest.json` file should look (The file below mimics the road to 100 million downloads sugofest a.k.a Gear 4 v2 Sugofest)
<img src="https://i.imgur.com/npIDo4v.png">

This is the final output
<img src="https://i.imgur.com/ntaOVVn.jpg">

### Manual Input

This method is generally not recommended since the json method is usually faster. However this method just requires you to run the script using:
```
$ python main.py
```
The script should ask all the relevant questions for all parts of the sugo. Once all questions are answered, it will generate the infographic file at: `images\infographic.png`