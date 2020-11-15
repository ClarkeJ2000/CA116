#!/usr/bin/env python

import sys
s = sys.argv[1]
total = 0
with open(s) as fd:
    s = fd.readline()
    while 0 < len(s):
        total = total + int(s)
        s = fd.readline()
print total
