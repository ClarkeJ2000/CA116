#!/usr/bin/env python

import os
files = os.listdir('.')

i = 0
while i < len(files):
    if files[i].split('.')[-1] != 'bak' and os.path.isfile(files[i]):
        with open(files[i], 'r') as fd:
            with open(files[i] + '.bak', 'w') as f:
                f.write(fd.read())
    i += 1
