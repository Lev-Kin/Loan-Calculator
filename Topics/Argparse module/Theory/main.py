import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--print_answer", action="store_true")

args = parser.parse_args()

print(args.print_answer)