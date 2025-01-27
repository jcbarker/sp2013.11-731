#!/usr/bin/python

import sys, cPickle
from collections import namedtuple

Word = namedtuple('Word', ['ID', 'FORM', 'LEMMA', 'CPOS', 'POS', 'MORPH', 'HEAD', 'DEP', 'PH', 'PD'])

sentences = []

sent = []
for line in sys.stdin:
    if line == "\n":
        sentences.append(sent)
        sent = []
    else:
        sent.append(Word(*line.strip().split()))

print len(sentences),"sentences parsed."
cPickle.dump(sentences, open(sys.argv[1], "wb"))

