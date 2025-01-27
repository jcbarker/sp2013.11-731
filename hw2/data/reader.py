import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--input", help="The input file containing tuples.", default="/home/jon/School/MachineTranslation/sp2013.11-731/hw2/data/test.hyp1-hyp2-ref")
parser.add_option("-d", "--dev", help="The input file containing dev tuples.", default="/home/jon/School/MachineTranslation/sp2013.11-731/hw2/data/train.hyp1-hyp2-ref")
parser.add_option("-g", "--gold", help="The input file containing dev gold.", default="/home/jon/School/MachineTranslation/sp2013.11-731/hw2/data/train.gold")
(ops, args) = parser.parse_args()

def dev_data():
    rawdev = open(ops.dev, "rb")
    dev = []
    for raw in rawdev:
        line = raw.strip().split("|||")
        a_sent = line[0].strip()
        b_sent = line[1].strip()
        ref = line[2].strip()
        yield (a_sent, b_sent, ref)

def input_data():
    rawinput = open(ops.input, "rb")
    data = []
    for raw in rawinput:
        line = raw.strip().split("|||")
        a_sent = line[0].strip()
        b_sent = line[1].strip()
        ref = line[2].strip()
        yield (a_sent, b_sent, ref)

def gold_refs():
    rawgold = open(ops.gold, "rb")
    for line in rawgold:
        yield int(line.strip())
