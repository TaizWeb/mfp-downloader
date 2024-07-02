"""Main file to utilize the scraper and downloader"""

import argparse
from scraper import Scraper
from downloader import Downloader

# Constants
SITE_LINK = "https://musicforprogramming.net/latest/"  # The domain of the site
SOURCE_LINK = "https://datashat.net/"  # The domain of the actual data storage
WEBDRIVER_PATH = "/home/taiz/chromedriver/chromedriver-linux64/chromedriver"

# Argparse
parser = argparse.ArgumentParser(description="MFP Downloader")
parser.add_argument(
    "destination_folder", help="The folder to store the downloaded tracks"
)
args = parser.parse_args()

# Use the modules to download the tracks
web_scraper = Scraper(WEBDRIVER_PATH, SITE_LINK, SOURCE_LINK)
avail_titles = web_scraper.parse_available_titles()
human_titles = [web_scraper.title_to_link(title) for title in avail_titles]
downloader = Downloader(human_titles, args.destination_folder)
downloader.download_links(indices=[5])  # NOTE: Track 20 seems to fail?
