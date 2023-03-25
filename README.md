# pyradio-m3u-to-playlist

A pyradio playlist generator from m3u playlist files.

Did you ever wanted to insert that huge playlist m3u file into `pyradio`?

### Using it

#### Install

Download the `m3u_to_pyradio_playlist-X.X.X.tar.gz` file.
Run `pip install m3u_to_pyradio_playlist-X.X.X.tar.gz` and you're ready to go.

#### Usage

You should check `m3u-to-pyradio --help` for options:

```
usage: m3u_to_pyradio [-h] [-i INPUT -o OUTPUT] [-d] [-a]

This program converts .m3u files into pyradio playlists.

examples:
   m3u_to_pyradio -d    Downloads and creates a huge stations.csv
   m3u_to_pyradio -a    Same as -a and overrides current pyradio stations
   m3u_to_pyradio -i playlist.m3u -o playlist.csv
                        Creates playlist.csv file from your playlist.m3u file

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        The m3u input file
  -o OUTPUT, --output OUTPUT
                        The output CSV file where playlist will be saved
  -d, --download-super-list
                        Download and convert the complete m3u list from
                        https://github.com/junguler/m3u-radio-music-playlists.
  -a, --auto            DANGER: Same as -dsl but OVERRIDES your
                        ~/.config/pyradio/stations.csv
```

##### I have a m3u file i'd like to import to pyradio

`m3u_to_pyradio -i my_playlist.m3u -o converted.csv`

Now go to `pyradio` config folder and add your custom `converted.csv` playlist.

##### I wan't a pre-built stations list

Just run `m3u_to_pyradio -d` and it will automatically download the
`---everything-full.m3u` playlist from:
https://github.com/junguler/m3u-radio-music-playlists

And save it to `stations.csv`. Now use it with pyradio.

##### I just want to automatically download a pre-built stations list and override my `stations.csv`

_DANGER_ this will override your current playlist. Backup it first!

Run:
`m3u_to_pyradio -a`

This will download the same list as from with `-d`.
Converts it to a `stations.csv` and move this file _OVERRIDING_ your `~/.config/pyradio/stations.csv`.

Want to automatically updates the list and run pyradio?

Assuming you're on a shell and already have pyradio installed:
`m3u_to_pyradio -a && pyradio`

#### Uninstall

Simply use:
`pip uninstall m3u_to_pyradio_playlist`

### Development

If you want to use this package for development, without needin to proper
install the dist via pip, this project is made with pipenv, that is both an venv
manager and a pip tool combined.

#### Installing and Testing

Make sure you have the version of Python present on `Pipfile` and that you
installed `pipenv` globally with: `pip install pipenv`

Clone this repository, cd into it and run:
`pipenv install`

You can call commands just like if you where from the executable commandline
preciding it with `pipenv run python` with: `pipenv run python m3u-to-pyradio
--help` `pipenv run python m3u-to-pyradio -i playlist.m3u -o playlist.csv`

#### Build

If you want to build it and install your own.

```bash
pipenv run python setup.py sdist bdist_wheel
cd dist
pip install [the file generated].tar.gz
cd ~
m3u-to-pyradio --help
```

You than could uninstall with:
`pip uninstall [the file generated]`

### Tested on

Tested on:

```
Darwin MacBook-Pro.local 22.2.0 Darwin Kernel Version 22.2.0: Fri Nov 11 02:04:44 PST 2022; root:xnu-8792.61.2~4/RELEASE_ARM64_T8103 x86_64
```

Python version:

```
Python 3.11.2
```
