#!/usr/bin/env python

import sys

file_name = sys.argv[1]

with open(file_name, 'r') as fd:
	fd.write(file_name)
