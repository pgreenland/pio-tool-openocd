#!/bin/env python

from urllib.request import urlretrieve
from shutil import unpack_archive, move, Error
from os import getcwd, listdir
from os.path import join

url = (
  "https://github.com/xpack-dev-tools/openocd-xpack/releases/download/"
  "v0.12.0-7/xpack-openocd-0.12.0-7-linux-arm64.tar.gz"
)
filename = "xpack-openocd-0.12.0-7.tar.gz"
path, headers = urlretrieve(url, filename)
unpack_archive(path, getcwd())
for file in listdir("xpack-openocd-0.12.0-7"):
  try:
    move(join("xpack-openocd-0.12.0-7", file), getcwd())
  except Error as err:
    print(err)
