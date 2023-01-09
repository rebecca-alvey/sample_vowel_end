#!/usr/bin/env python

import re
import sys
import argparse

#function to test if the word is a vowel or not, returns bool
def testWordEndVowel(word):
    vowel = re.search('[aeiou]\Z', word, re.IGNORECASE)
    return vowel

parser = argparse.ArgumentParser();
parser.add_argument('word_to_test');

#argparse will throw useage error here if the input is invalid, no need to test sys.argv length
args = parser.parse_args();

w = args.word_to_test;
v = testWordEndVowel(w)
if v:
    print(w + ' is a word that ends in a vowel.')
else:
    print(w + ' is not a word that ends in a vowel.')

