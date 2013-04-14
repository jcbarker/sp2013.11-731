#!/usr/bin/python

import sys, cPickle, codecs

Word = namedtuple('Word', ['ID', 'FORM', 'LEMMA', 'CPOS', 'POS', 'MORPH', 'HEAD', 'DEP', 'PH', 'PD'])

parses = cPickle.load(codecs.open('data/parse.pkl', 'rb', 'utf-8'))

# Reorder adjective noun pairs
def fixAdjectives(s, parse):
    for w in parse:
        if 


for line in codecs.open(sys.argv[1], 'rb', 'utf-8'):
    sent = line.strip().split()
    
