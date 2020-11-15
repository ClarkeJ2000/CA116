#!/usr/bin/env python

import sys
s = sys.stdin.read()

count = 0
i = 0
while i < len(s):
	if s[i] >= '0' and s[i] <= '9':
		count += 1
	i += 1
print count
