#!/usr/bin/env python

import re
import sys

if len(sys.argv) == 2:
    i = sys.argv[1]
    v = re.search('[aeiou]\Z', i, re.IGNORECASE)
    if v:
        print(i + ' is a word that ends in a vowel.')
    else:
        print(i + ' is not a word that ends in a vowel.')
else:
    print('Usage: sample_vowel_end.py word_to_test')