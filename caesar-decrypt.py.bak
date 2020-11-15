#!/usr/bin/env python

import sys
n = 13
d = {}
s = sys.stdin.readlines()
lower = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
upper = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]

i = 0
while i < len(lower):
    d[upper[i]] = lower[i]
    i = i + 1
i = 0
while i < len(s):
    total = ""
    j = 0
    line = s[i].strip()
    while j < len(line):
        if line[j] in d:
            total = total + d[line[j]]
        else:
            total = total + line[j]
        j = j + 1
    print total
    i += 1
