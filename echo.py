#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "Scott Reese"
__github__ = "reessm01"


import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        description = "Perform transformation on input text."
    )
    parser.add_argument("text", help="text to be manipulated")  
    parser.add_argument("-u", "--upper", action="store_true", help="convert text to uppercase")
    parser.add_argument("-l", "--lower", action="store_true", help="convert text to lowercase")
    parser.add_argument("-t", "--title", action="store_true", help="convert text to titlecase")
    return parser
    
def to_upper(text):
    return text.upper()

def to_lower(text):
    return text.lower()

def to_titlecase(text):
    return text.title()

def main(args):
    result = args.text
    if args.upper:
        result = to_upper(args.text)
    if args.lower:
        result = to_lower(args.text)
    if args.title:
        result = to_titlecase(args.text)

    print(result)


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    if not args:
        parser.print_usage()
        sys.exit()
    else:
        main(args)
