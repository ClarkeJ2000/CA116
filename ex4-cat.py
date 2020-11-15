#!/usr/bin/env python

import sys

file_name = sys.argv[1]

with open(file_name) as fd:
	sys.stdout.write(fd.read())
