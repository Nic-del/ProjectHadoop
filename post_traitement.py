# -*- coding: utf-8 -*-

from collections import defaultdict
from operator import itemgetter
import sys

def post_traitement():
    grouped_data = defaultdict(list)

    
    for line in sys.stdin:
        parts = line.strip().split('\t')
        if len(parts) != 2:
            continue
        key, count = parts
        count = int(count)
        key_parts = key.split('_')
        if len(key_parts) != 3:
            continue
        year, gender, name = key_parts
        grouped_data[(year, gender)].append((name, count))

    top_names_by_group = {}
    for group, names in grouped_data.iteritems():
        sorted_names = sorted(names, key=itemgetter(1), reverse=True)[:5]
        top_names_by_group[group] = sorted_names

    with open('resultat.txt', 'w') as out:
        for group, top_names in sorted(top_names_by_group.iteritems(), key=lambda x: int(x[0][0])):
            year, gender = group
            out.write("Annee: {}, Sexe: {}\n".format(year, gender))
            for name, count in top_names:
                out.write("  {}: {}\n".format(name, count))



if __name__ == "__main__":
    post_traitement()  