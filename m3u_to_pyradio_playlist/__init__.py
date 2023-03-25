" m3u_to_pyradio -- File converter to pyradio. "

version_info = (0, 0, 1)

__version__ = version = ".".join(map(str, version_info))
__project__ = __name__
__author__ = "Rahul M. Juliato"
__license__ = "GPL-2.0"


# Set default encoding to utf-8
import sys
import importlib

importlib.reload(sys)
sys.setdefaultencoding("utf-8")
