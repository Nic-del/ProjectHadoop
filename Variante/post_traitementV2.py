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

sorted_counts = sorted(counts.items(), key=lambda x: -x[1])

top_5 = sorted_counts[:5]

with codecs.open('resultat.txt', 'w', 'utf-8') as out:
    for key, count in top_5:  
        sexe, prenom = key.split('-')
        out.write("%s-%s: %d\n" % (sexe, prenom, count))
