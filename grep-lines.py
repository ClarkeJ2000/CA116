#!/usr/bin/env python

import sys
word = sys.argv[1]

s = raw_input()
while s != 'end':
    i = 0
    while i < (len(s) - len(word) + 1) and (s[i:i + len(word)] != word):
        i += 1
        if i < (len(s) - len(word) + 1):
            print s
        s = raw_input()
