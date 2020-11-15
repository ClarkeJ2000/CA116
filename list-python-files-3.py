#!/usr/bin/env python

import os
files = os.listdir('.')

i = 0
while i < len(files):
	if files[i][-3:] == '.py':
		with open(files[i], 'r') as fd:
			if len(fd.read()) != 0:
				print files[i]
	elif files[i][0] != '.':
		with open(files[i], 'r') as fd:
			if fd.readline() == '#!/usr/bin/env python\n':
				print files[i]
	i += 1
