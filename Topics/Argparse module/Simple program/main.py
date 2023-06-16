import argparse

# Create the argument parser
parser = argparse.ArgumentParser()
# Add the --number argument
parser.add_argument("--number", type=int)

# Parse the command-line arguments
args = parser.parse_args()