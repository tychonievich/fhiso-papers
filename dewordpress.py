import re, sys

for filename in sys.argv[1:]:
	with open(filename) as f:
		s = f.read()
		s = re.sub("&nbsp;"," ",s);
		s = re.sub("\s\s+"," ",s);
		rows = s.split("<tr")
		for r in rows:
			if 'lid=' in r:
				lid = r.find("lid=")+4
				lid2 = r.find("&", lid);
				lid = r[lid:lid2]
				r2 = re.split("<[^>]*>",r)
				surname = r2[8].strip()
				given = r2[31].strip()
				kind = r2[33].strip()
				title = r2[35].strip()
				date = r2[37].strip()
				version = r2[39].strip()
				filename = 'fhiso-paper-%04d-%s.pdf' % (int(lid), re.sub("[^a-zA-Z0-9]+","-",version))
				print '''<tr><td class="author">%s, %s</td><td class="title">%s</td><td class="type">%s</td><td class="date">%s</td><td class="version">%s</td><td class="pdf"><a href="%s">PDF</a></td></tr>''' % (surname,given, title,kind,date,version,filename)
