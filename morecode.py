#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import base64
import argparse
import html
from termcolor import cprint

# configure the format of output
print_decode = lambda x: cprint(x, 'magenta')
print_encode = lambda x: cprint(x, 'red')


def decode(string):
    html_decode = html.unescape(string)
    print_decode(html_decode)

def encode(string):
    # html entity encode
    html_encode1 = html.escape(string)
    html_encode2 = html.escape(string, quote=True)
    html_encode3 = html.escape(string, quote=True)
    print_encode(html_encode)

# handle input param
# doc link:https://docs.python.org/zh-cn/3/howto/argparse.html
def parse_param():
    logo = r"""
     __  __                 ____ ___      _
    |  \/  | ___  _ __ ___ / ___/ _ \  __| | ___
    | |\/| |/ _ \| '__/ _ \ |  | | | |/ _` |/ _ \
    | |  | | (_) | | |  __/ |__| |_| | (_| |  __/
    |_|  |_|\___/|_|  \___|\____\___/ \__,_|\___|

    Powered by MoreCode
    Author xq17
    """
    print(logo)
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--decode", help="decode string", action="store_true")
    parser.add_argument("-e", "--encode", help="encode string", action="store_true")
    parser.add_argument("string", type=str, default="", help="converted-string")
    args = parser.parse_args()
    return args

def main():
    args = parse_param()
    string = args.string.strip()
    # try to decode string
    if args.decode == True:
        result =  decode(string)
    if args.encode == True:
        result =  encode(string)
    if not args.decode and not args.encode:
        print("missing type to hanle string, example -d abc or -e abc")

if __name__ == '__main__':
    main()