#! /usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--filename', default='test.txt', help="name of the file to process")
parser.add_argument('--verbose',
                    action="store_true",
                    help='enable verbose mode, this actually works')

parser.add_argument('--test_mode',
                    action="store_true",
                    help='enable verbose mode, train only with 10 examples')

args = parser.parse_args()
print(f'verbose flag {args.verbose}')
print(f'test mode flag {args.test_mode}')
print(args.filename)