# -*- coding: utf-8 -*-
import sys
import codecs

counts = {}

for line in sys.stdin:
    try:
        line = line.decode('utf-8').strip()  
        parts = line.split('\t')
        if len(parts) != 2:
            continue
        key, count = parts
        count = int(count)

        if key in counts:
            counts[key] += count
        else:
            counts[key] = count
    except:
        continue  


with codecs.open('resultat.txt', 'w', 'utf-8') as out:
    for key in sorted(counts.keys()):
        out.write(u"%s: %d\n" % (key, counts[key]))
