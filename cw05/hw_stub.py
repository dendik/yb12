import argparse

def calculate_resistances(infile, outfile):
    ...

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("infile")
    parser.add_argument("outfile")
    args = parser.parse_args()

    calculate_resistances(args.infile, args.outfile)
