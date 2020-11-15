#!/usr/bin/env python

import sys
words = sys.stdin.read().split()
d = {}
i = 0
while i < len(words):
    word = words[i]
    if word not in d:
        d[word] = 0
    d[word] += 1
    i += 1
 
for word in d:
    if d[word] == 1:       
        print word
