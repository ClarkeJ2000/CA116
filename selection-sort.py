#!/usr/bin/env python

a = []
i = 0
p = 0
s = raw_input()
#build list
while s != "end":
    a.append(int(s))
    s = raw_input()

#cycles through list
while i < len(a):
    p = i
    j = i + 1
#finds smallest
    while j < len(a):
        if a[j] < a[p]:
            p = j
        j = j + 1
#moves smallest to start    
    tmp = a[p]
    a[p] = a[i]
    a[i] = tmp
    i = i + 1

#cycles through list and prints each element        
i = 0
while i < len(a):
    print a[i]
    i = i + 1
