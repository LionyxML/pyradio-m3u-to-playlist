"""Setup file for m3u_to_pyradio"""

from setuptools import setup, find_packages

from m3u_to_pyradio_playlist import (
    __project__,
    version,
    __license__,
    __author__,
)


meta = dict(
    name=__project__,
    version=version,
    license=__license__,
    description="Converts M3U playlists to pyradio format",
    platforms=("Any"),
    author=__author__,
    author_email="rahul.juliato@gmail.com",
    url="https://github.com/LionyxML/pyradio-m3u-to-playlist",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "m3u_to_pyradio=m3u_to_pyradio_playlist.__main__:main"
        ]
    },
    install_requires=["requests"],
    test_suite="tests",
)


if __name__ == "__main__":
    setup(**meta)
