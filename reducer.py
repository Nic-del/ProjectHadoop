#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

current_key = None
current_count = 0

for line in sys.stdin:
    key, value = line.strip().split('\t')
    try:
        value = int(value)
    except:
        continue

    if key == current_key:
        current_count += value
    else:
        if current_key is not None:
            print("{}\t{}".format(current_key, current_count))
        current_key = key
        current_count = value

if current_key is not None:
    print("{}\t{}".format(current_key, current_count))

