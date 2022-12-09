import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument('-p','--param1',help='x variable', required=True)
parser.add_argument('-q','--param2',help='y variable', required=True)
parser.add_argument('-r','--param3',help='z variable', required=True)

args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")