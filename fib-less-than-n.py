#!/usr/bin/env python

n = input()
i = 0
current = 1
previous = 0
print '0'
print current
new = 0
while new < n:
    new = previous + current
    if new < n:
        print new
    tmp = new
    new = current
    current = tmp
    tmp = new
    new = previous
    previous = tmp
    i += 1
