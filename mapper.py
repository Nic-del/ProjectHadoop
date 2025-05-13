#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv

reader = csv.reader(sys.stdin, delimiter=';')

for line in reader:
    if len(line) != 5:
        continue
    sexe, prenom, annais, dept, nombre = line
    if not (annais and sexe and nombre and dept):
        continue
    if '_' in prenom:
        continue
    try:
        key = "{}_{}_{}".format(annais, sexe, prenom)
        print("{}\t{}".format(key, int(nombre)))
    except:
        continue
