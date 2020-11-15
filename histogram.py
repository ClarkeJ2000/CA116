#!/usr/bin/env python

n = 10
hist = [0] * n
s = raw_input()
while s != 'end':
	hist[int(s)] += 1
	s = raw_input()
i = 0
while i < n:
	print i, '*' * hist[i]
	i += 1