#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

def validate_file(input_file, output_file):
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile, delimiter=';')

        try:
            next(reader)
        except StopIteration:
            return

        for line in reader:
            if len(line) != 5:
                continue

            sexe, prenom, annais, dept, nombre = line

            if annais == 'XXXX':
                continue

            if not (annais and sexe and nombre and dept):
                continue

            if '_' in prenom:
                continue

            writer.writerow(line)

if __name__ == "__main__":
    input_file = "dpt2022.csv"
    output_file = "dpt2022_valid.csv"
    validate_file(input_file, output_file)
