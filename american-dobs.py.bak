#!/usr/bin/env python

import sys
with open("irish-dobs.txt") as fd:
    lines = fd.readlines()
with open("american-dobs.txt", "w") as fo:
    i = 0
    while i < len(lines):
        tokens = lines[i].split()
        date = tokens[0].split("/")
        tokens[0] = "/".join([date[1], date[0], date[2]])
        fo.write(" ".join(tokens) + "\n")
        i = i + 1
