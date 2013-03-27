import re, sys

for filename in sys.argv[1:]:
	with open(filename) as f:
		l = []
		for line in f.readlines():
			if 'font-family' in line and '<strong>' not in line:
				l.append(re.search("<font[^>]*>(.*)</font>", line).group(1))
		for i in xrange(0,len(l),12):
			print l[i:i+12]
			# filename = "fhiso-paper-%04d-$s.pdf" % 
			print '''<tr><td class="author">{1}, {0}</td><td class="title">{5}</td><td class="type">{3}</td><td class="date">{4}</td><td class="version">{6}</td></tr>'''.format(*l)
