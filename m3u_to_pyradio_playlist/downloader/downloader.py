"""Functions used to download a m3u file."""

import requests

list_url = (
    "https://raw.githubusercontent.com/junguler/"
    "m3u-radio-music-playlists/main/---everything-full.m3u"
)


def get_huge_playlist():
    """Download a huge playlist."""
    print("Downloading playlist...")
    response = requests.get(list_url)

    with open("temp.m3u", "wb") as file:
        file.write(response.content)

    print("List downloaded!")
    return
