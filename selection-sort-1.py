#!/usr/bin/env python

j = 1
a = []
i = 0
p = 0
s = raw_input()
while s != 'end':
	a.append(int(s))
	s = raw_input()

while j < len(a):
	if a[j] < a[p]:
		p = j
	j += 1
print p
