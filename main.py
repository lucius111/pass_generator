import argparse
from gen_pass import gen_pass

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the length')

args = parser.parse_args()

for i in args.integers:
    password = gen_pass(i)
    print(password)



