#!/usr/bin/env python

import os
files = os.listdir('.')

i = 0
while i < len(files):
	file = files[i]
	if file[-4:] != '.bak':
		with open(files[i], 'r') as fd:
			s = fd.read()
			new_file = file + '.bak'
			with open(new_file, 'w') as fd:
				fd.write(s)
	i += 1
