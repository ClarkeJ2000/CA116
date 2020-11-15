#!/usr/bin/env python

import sys
i = 1
total = 0
while i < len(sys.argv):
    s = sys.argv[i]
    with open(s) as fd:
        s = fd.read().split()
        while 0 < len(s):
            total = total + int(s)
            s = fd.read().split()
    i = i + 1
print total
