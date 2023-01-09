#!/usr/bin/env python

import re
import sys
import argparse

parser = argparse.ArgumentParser();
parser.add_argument('word_to_test');

#argparse will throw useage error here if the input is invalid, no need to test sys.argv length
args = parser.parse_args();


i = args.word_to_test;
v = re.search('[aeiou]\Z', i, re.IGNORECASE)
if v:
    print(i + ' is a word that ends in a vowel.')
else:
    print(i + ' is not a word that ends in a vowel.')
