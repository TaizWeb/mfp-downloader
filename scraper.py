"""Module to handle scraping the source site"""

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


class Scraper:
    """
    Scraper class to parse data from the site into a download links

    Attributes
    ----------
    webdriver_path: str
        The path to the webdriver
    site_link: str
        The link to the source, user-facing site
    source_link: str
        The link to the site that has the mp3 files

    Methods
    -------
    create_driver(webdriver_path: str)
        Create the webdriver object for the class instance
    get_site_html()
        Retrieves the site's HTML as a BeautifulSoup object
    parse_available_titles()
        Pulls the titles out of the site specified in site_link
    title_to_link(human_title: str):
        Converts the titles into the link format for the source_link site
    """

    def __init__(self, webdriver_path: str, site_link: str, source_link: str):
        self.site_link = site_link
        self.source_link = source_link
        self.driver = self.create_driver(webdriver_path)
        self.site_soup = self.get_site_html()

    def create_driver(self, webdriver_path: str):
        """Sets up the webdriver

        Parameters
        ----------
        webdriver_path: str
            The path to the webdriver

        Returns
        -------
        driver: WebDriver
            The driver that will be used for HTML retrieval
        """
        service = Service(webdriver_path)
        return webdriver.Chrome(service=service)

    def get_site_html(self):
        """Retrieves the site's HTML"""
        self.driver.get(self.site_link)
        # The site is "fancy" and hides the song titles until they "load"
        # Sure it looks nice but boy is it annoying to work around
        time.sleep(4)
        site_html = self.driver.page_source
        self.driver.quit()
        return BeautifulSoup(site_html, "lxml")

    def parse_available_titles(self):
        """Returns a list of the titles

        Returns
        -------
        titles: list
            A list of every available title on the site
        """
        sections = self.site_soup.find_all("section")
        title_section = sections[2]  # This is the last section
        return [
            title_link.contents[0].text for title_link in title_section.find_all("a")
        ]

    def title_to_link(self, human_title: str):
        """Converts a songs title to the actual link

        Parameters
        ----------
        human_title: str
            The title the user sees

        Returns
        -------
        link: str
            The link to the source mp3 file

        Notes
        -----
        Converts this:
        71: Neon Genesis
        To this:
        71-neon_genesis.mp3
        """
        # Remove the leading 0 if it exists
        if human_title[0] == "0":
            human_title = human_title[1:]
        # Replace the invalid characters for a link
        source_title = (
            human_title.replace(": ", "-").replace(" ", "_").replace("+", "and").lower()
        )
        # Return the full result
        return f"{self.source_link}music_for_programming_{source_title}.mp3"


# web_scraper = Scraper(WEBDRIVER_PATH, SITE_LINK, SOURCE_LINK)
# # print(web_scraper.get_site_html())
# avail_titles = web_scraper.parse_available_titles()
# print(avail_titles)
# print([web_scraper.title_to_link(title) for title in avail_titles])
