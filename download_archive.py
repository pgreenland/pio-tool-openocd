#!/bin/env python

from shutil import unpack_archive, move, Error
from os import getcwd, listdir
from os.path import join

import requests
from platformio.util import get_systype

# Get host system type
systype = get_systype().replace("_", "-")

# OpenOCD version
open_ocd_version = "0.12.0-7"

# Download and unpack OpenOCD archive
url = f"https://github.com/xpack-dev-tools/openocd-xpack/releases/download/v{open_ocd_version}/xpack-openocd-{open_ocd_version}-{systype}.tar.gz"
filename = f"xpack-openocd-{open_ocd_version}.tar.gz"

# Print info
print(f"Downloading and unpacking OpenOCD {open_ocd_version} for {systype} from {url} ...")

response = requests.get(url)
response.raise_for_status()

with open(filename, 'wb') as f:
    f.write(response.content)

unpack_archive(filename, getcwd())
for file in listdir(f"xpack-openocd-{open_ocd_version}"):
  try:
    move(join(f"xpack-openocd-{open_ocd_version}", file), getcwd())
  except Error as err:
    print(err)
