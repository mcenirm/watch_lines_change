#!/usr/bin/env python

from __future__ import absolute_import, division, print_function, unicode_literals

from difflib import SequenceMatcher
from sys import stdin


RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

ON = dict(insert=GREEN, replace=RED, equal=RESET, delete=RESET)

a = ''
for line in stdin:
    b = line.rstrip()
    s = SequenceMatcher(None, a, b)
    for oc in s.get_opcodes():
        tag, i1, i2, j1, j2 = oc
        text = b[j1:j2]
        print(ON[tag], end='')
        if tag != 'delete':
            print(text, end='')
    print(RESET)
    a = b
