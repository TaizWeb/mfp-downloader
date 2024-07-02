"""Module to handle downloading and tagging of files"""

import os
import urllib.request
import ffmpeg


class Downloader:
    """
    Downloader class to download the links acquired from the Scraper class

    Attributes
    ----------
    link_list: list
        The list of source links to download
    directory_path: str
        The directory to store the songs into, if this doesn't exist, it will
        be created
    artist_name: str
        The name of the artist, used for tagging
    album_title: str
        The title of the album, used for tagging

    Methods
    -------
    download_links(indices=[])
        Downloads the links set on object creation, at the indices provided
    tag_links()
        Tags the links after downloading. Not currently used, since the songs
        appear to come pre-tagged
    """

    def __init__(
        self,
        link_list: list,
        directory_path: str,
        artist_name: str = "",
        album_title: str = "",
    ):
        self.directory_path = directory_path
        self.artist_name = artist_name
        self.album_title = album_title
        self.link_list = link_list

    def download_links(self, indices=None):
        """Download the links

        Parameters
        ----------
        indices: list
            The list of track numbers to download

        Example
        -------
        `download_links([5, 10, 20])` will download 3 tracks, track 5, 10, and
        20. This is useful if you have a few particular tracks you want to
        download instead of all of them
        """
        # Does the specified path exist? If not, create it
        if not os.path.isdir(self.directory_path):
            os.mkdir(self.directory_path)
        os.chdir(self.directory_path)

        # Does the user have specific tracks in mind?
        if indices is not None and len(indices) > 0:
            self.link_list = [self.link_list[i] for i in indices]

        # Download the files
        for link in self.link_list:
            print(f"Downloading {link}...")
            # Telling a quick lie to get around 403 errors
            headers = {
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537"
                    ".36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
                )
            }
            filename = link.split("/")[-1]
            # Encode the URL, pesky umlaut
            link = urllib.parse.quote(link, safe=":/")

            # Acquire the link's file
            request = urllib.request.Request(link, headers=headers)
            with urllib.request.urlopen(request) as response, open(
                filename, "wb"
            ) as out_file:
                data = response.read()
                out_file.write(data)

        # Lol, apparently the songs come pre-tagged
        # self.tag_links()

    def tag_links(self):
        """Tag the links"""
        for song in self.link_list:
            song_filename = song.split("/")[-1]
            song_name = song_filename.split(".")[0]
            tags = {
                "metadata": f"title={song_name} artist={self.artist_name} album={self.album_title}",
            }
            (
                ffmpeg.input(song_filename)  # Since we're already in the dir
                .output(f"tagged_{song_filename}", **tags)
                .run(overwrite_output=True)
            )
