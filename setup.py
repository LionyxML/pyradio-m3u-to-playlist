from setuptools import setup, find_packages

setup(
    name="m3u-to-pyradio-playlist",
    version="0.0.1",
    description="Converts M3U playlists to pyradio format",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "m3u-to-pyradio=m3u_to_pyradio_playlist.__main__:main"
        ]
    },
    install_requires=[
        # list of required packages
    ],
)
