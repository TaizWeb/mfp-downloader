"""Module to handle downloading and tagging of files"""

from scraper import Scraper
import os
import urllib.request
import ffmpeg

# Site constants
SITE_LINK = "https://musicforprogramming.net/latest/"  # The domain of the site
SOURCE_LINK = "https://datashat.net/"  # The domain of the actual data storage
WEBDRIVER_PATH = "/home/taiz/chromedriver/chromedriver-linux64/chromedriver"


class Downloader:
    """docstring for Downloader."""

    def __init__(self, link_list, directory_path, artist_name, album_title):
        self.directory_path = directory_path
        self.artist_name = artist_name
        self.album_title = album_title
        self.link_list = link_list

    def download_links(self):
        """Download the links"""
        # Does the specified path exist? If not, create it
        if not os.path.isdir(self.directory_path):
            os.mkdir(self.directory_path)
        os.chdir(self.directory_path)

        # Download the files
        for link in self.link_list:
            print(f"Downloading {link}...")
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            filename = link.split("/")[-1]
            request = urllib.request.Request(link, headers=headers)
            with urllib.request.urlopen(request) as response, open(
                filename, "wb"
            ) as out_file:
                data = response.read()
                out_file.write(data)

        self.tag_links()

    def tag_links(self):
        """Tag the links"""
        for song in self.link_list:
            song_filename = song.split("/")[-1]
            song_path = f"{self.directory_path}/{song_filename}"
            song_name = song_filename.split(".")[0]
            tags = {
                "metadata": f"title={song_name}",
                "metadata": f"artist={self.artist_name}",
                "metadata": f"album={self.album_title}",
            }
            (
                ffmpeg.input(song_path)
                .output(song_path, **tags)
                .run(overwrite_output=True)
            )


web_scraper = Scraper(WEBDRIVER_PATH, SITE_LINK, SOURCE_LINK)
avail_titles = web_scraper.parse_available_titles()
human_titles = [web_scraper.title_to_link(title) for title in avail_titles]
downloader = Downloader(human_titles, "foobar", "MFP", "MFP")
downloader.download_links()
