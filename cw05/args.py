##import sys
##
##print(sys.argv)

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("infile",
                    help="Input file")
parser.add_argument("outfile",
                    help="Output file")
parser.add_argument("-n", "--num-tries", type=int,
                    help="Number of attempts to guess")
args = parser.parse_args()

print("infile", args.infile)
print("outfile", args.outfile)
print("num tries", args.num_tries)
