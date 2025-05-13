#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

current_key = None
current_count = 0

for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) != 2:
        continue
    key, value = parts
    if not value.isdigit():
        continue
    value = int(value)

    if key == current_key:
        current_count += value
    else:
        if current_key and current_count >= 50:
            sys.stdout.write("%s\t%d\n" % (current_key, current_count))
        current_key = key
        current_count = value

if current_key and current_count >= 50:
    sys.stdout.write("%s\t%d\n" % (current_key, current_count))
