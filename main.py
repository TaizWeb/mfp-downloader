"""Main file to utilize the scraper and downloader"""

# from scraper.scraper import Scraper
from scraper import Scraper
from downloader import Downloader

# Constants
SITE_LINK = "https://musicforprogramming.net/latest/"  # The domain of the site
SOURCE_LINK = "https://datashat.net/"  # The domain of the actual data storage
WEBDRIVER_PATH = "/home/taiz/chromedriver/chromedriver-linux64/chromedriver"
FOLDER_NAME = "foobar"  # The folder to save the tracks to

# Use the modules to download the tracks
web_scraper = Scraper(WEBDRIVER_PATH, SITE_LINK, SOURCE_LINK)
avail_titles = web_scraper.parse_available_titles()
human_titles = [web_scraper.title_to_link(title) for title in avail_titles]
downloader = Downloader(human_titles, FOLDER_NAME)
downloader.download_links(indices=[5])  # NOTE: Track 20 seems to fail?
