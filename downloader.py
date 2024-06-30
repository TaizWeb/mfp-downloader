from scraper import Scraper

# Site constants
SITE_LINK = "https://musicforprogramming.net/latest/"  # The domain of the site
SOURCE_LINK = "https://datashat.net/"  # The domain of the actual data storage
WEBDRIVER_PATH = "/home/taiz/chromedriver/chromedriver-linux64/chromedriver"


web_scraper = Scraper(WEBDRIVER_PATH, SITE_LINK, SOURCE_LINK)
# print(web_scraper.get_site_html())
avail_titles = web_scraper.parse_available_titles()
print(avail_titles)
print([web_scraper.title_to_link(title) for title in avail_titles])
