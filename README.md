# MFP Scraper

## What is this??
This is a tool to download the contents of [musicForProgramming();](https://musicforprogramming.net/latest/), that being every single track they have to offer. While the site does provide a way to download a single track at a time, there isn't any way (that I'm aware of) to download the entire "album" at once. As someone who's seen good internet content disappear all the time, I'm quite the data hoarder and this being another one of my data hoarding projects.

## Installing Dependencies
1. Clone the repo and enter it
2. Ensure you have [Python 3.10.12](https://www.python.org/downloads/) (or later, but imagine putting breaking changes in a minor release lol)
3. Install the dependencies: `pip install -r requirements.txt`

## Configuration
In the root of the project, you'll find the `.env` file. This contains the necessary constants used in the program.

| Key            | Value                                                                     |
| -------------- | ------------------------------------------------------------------------- |
| SITE_LINK      | The path to the site, this can likely be left at the default              |
| SOURCE_LINK    | The path to the mp3 storage part of the site, this can be left at default |
| WEBDRIVER_PATH | The path to the webdriver. See "Acquiring a Webdriver"                    |


### Acquiring a Webdriver
Download one from [Chrome's Repository](https://googlechromelabs.github.io/chrome-for-testing/) and update the `.env` variable to match the path to it

## Usage
While in the directory, execute `python main.py <folder_name>` to run the script. This will download all ~7GB(!) worth of tracks to the folder specified in <folder_name>.
For example, `python main.py songs` will create a folder called "songs" that holds all the songs inside of it.
