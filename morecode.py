#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import base64
import argparse
from termcolor import cprint

# configure the format of output
print_decode = lambda x: cprint(x, 'magenta')
print_encode = lambda x: cprint(x, 'red')


def decode():
    pass

def encode():
    pass

# handle input param
# doc link:https://docs.python.org/zh-cn/3/howto/argparse.html
def parse_param():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--decode", help="decode string", action="store_true")
    parser.add_argument("-e", "--encode", help="encode string", action="store_true")
    parser.add_argument("string", type=str, default="", help="converted-string")
    args = parser.parse_args()
    return args

def main():
    args = parse_param()
    string = args.string
    # try to decode string
    if args.decode == True:
        result =  decode(string)
    if args.encode == True:
        result =  encode(string)




if __name__ == '__main__':
    main()