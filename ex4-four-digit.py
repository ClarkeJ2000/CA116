#!/usr/bin/env python
#!/usr/bin/env python

import sys
s = sys.stdin.read().split()

p = 'none'
i = 0
while i < len(s) and p == 'none':
	if len(s[i]) == 4:
		p = s[i]	
	i += 1
print p