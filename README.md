# pyradio-m3u-to-playlist

A pyradio playlist generator from m3u playlist files.

Did you ever wanted to insert that huge playlist m3u file into `pyradio`?

### Using it

TO BE DONE...

#### Install

#### Usage

#### Uninstall

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
