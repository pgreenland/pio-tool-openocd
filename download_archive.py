#!/bin/env python

from urllib.request import urlretrieve
from shutil import unpack_archive, move, Error
from os import getcwd, listdir
from os.path import join

from platformio.util import get_systype

# Get host system type
systype = get_systype().replace("_", "-")

# OpenOCD version
open_ocd_version = "0.12.0-7"

url = (
  "https://github.com/xpack-dev-tools/openocd-xpack/releases/download/"
  f"v{open_ocd_version}/xpack-openocd-{open_ocd_version}-{systype}.tar.gz"
)
filename = f"xpack-openocd-{open_ocd_version}.tar.gz"
path, headers = urlretrieve(url, filename)
unpack_archive(path, getcwd())
for file in listdir(f"xpack-openocd-{open_ocd_version}"):
  try:
    move(join(f"xpack-openocd-{open_ocd_version}", file), getcwd())
  except Error as err:
    print(err)
