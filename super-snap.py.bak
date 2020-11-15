#!/usr/bin/env python

import sys
words = sys.stdin.readlines()

firsts = []
no_snap = True

i = 0
while i < len(words) and no_snap:
    word = words[i].strip()
    if word not in firsts:
        firsts.append(word)
    elif word in firsts:
        print 'snap:' + ' ' + word
        no_snap = False
    i += 1

