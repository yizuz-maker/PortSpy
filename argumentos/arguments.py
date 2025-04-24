"""
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", help="input file", required=True)
parser.add_argument("-o", "--output", help="output file", required=True)

args = parser.parse_args()
"""