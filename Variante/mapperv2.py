#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

for line in sys.stdin:
    parts = line.strip().split(';')
    if len(parts) != 5:
        continue

    sexe, prenom, annais, dept, nombre = parts

    if not (sexe and prenom and annais and nombre and dept):
        continue
    if '_' in prenom or '-' in prenom:
        continue
    if not annais.isdigit() or not nombre.isdigit():
        continue

    annee = int(annais)
    decade = annee - (annee % 10)
    key = "%s-%s" % (sexe, prenom)
    sys.stdout.write("%s\t%s\n" % (key, nombre))
