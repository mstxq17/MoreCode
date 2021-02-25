#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import base64
import argparse
import re
import html, binascii, chardet, base64
import urllib.parse
import hashlib
from termcolor import cprint

# configure the format of output
print_decode = lambda string: cprint(string, 'magenta')
print_encode = lambda string: cprint(string, 'red')
print_preview = lambda string: cprint(string, 'green')
print_type = lambda string: cprint(string, 'blue')

# core class, utils
class Utils:
    """utils include many functions to encode/decode"""
    def __init__(self, arg=""):
        self.arg = arg

    def html_encode(self, string, isChinese):
        print_type("[0] HTML entities Encode:")
        encode1 = html.escape(string, quote=True)
        encode2 = string.encode('ascii','xmlcharrefreplace').decode()
        _charref = re.compile('[^(&(#\[0-9\]+;?)]|[^(&(#\[xX\]\[0-9a-fA-F\]+;?)]')
        encode3 = re.sub(_charref, lambda x:"&#"+str(hex(ord(x.group(0)))).replace("0","")+";", encode2)
        encode4 = re.sub("[^&](#{1})", lambda x:str(x.group(1)).replace("#","&#"+str(hex(ord("#"))).replace("0","")+";"),encode3)
        print_encode(f"[Normal] >> {encode1}")
        if isChinese:
            print_encode(f"[Chinese] >> {encode2}")
        print_encode(f"[More] >> {encode4}")
        print_encode(f"[ALL] >> {encode4}")

    def url_encode(self, string):
        print_type("[1] URL Encode:")
        encode1 = urllib.parse.quote(string.encode())
        encode2 =  ''.join('%{:02X}'.format(c) for c in string.encode())
        print_encode(f"[Normal] >> {encode1}")
        print_encode(f"[ALL] >> {encode2}")

    def md5_encode(self, string):
        print_type("[2] MD5 Encode:")
        encode1 = hashlib.md5(string.encode()).hexdigest()
        print_encode(f"[16 md5] >> {encode1[8:24]}")
        print_encode(f"[32 md5] >> {encode1}")

    def base64_encode(self, string):
        print_type("[3] BASE64 Encode:")
        encode1 = base64.b64encode(string.encode())
        print_encode(f"[base64] >> {encode1}")

    def chr_encode(self, string, isChinese):
        print_type("[4] CHR Encode:")
        if isChinese:
            print_encode(f"[chr] >> Not support chinese")
        else:
            encode1 = "+".join(["chr("+str(ord(i)) + ")" for i in  string])
            encode2 = "&".join(["chr("+str(ord(i)) + ")" for i in  string])
            print_encode(f"[chr:+] >> {encode1}")
            print_encode(f"[chr:&] >> {encode2}")




    def html_decode(self, string):
        print_type("[0] HTML entities Decode:")
        decode1 = html.unescape(string)
        print_decode(f"[Normal] >> {decode1}")

    def url_decode(self, string):
        print_type("[1] URL Decode:")
        decode1 = urllib.parse.unquote(string.encode())
        print_decode(f"[Normal] >> {decode1}")

    def base64_decode(self, string):
        print_type("[3] BASE64 Decode:")
        try:
            decode1 = base64.b64decode(string.encode()).decode()
            print_decode(f"[base64] >> {decode1}")
        except:
            print_decode(f"[base64] >> Error")

    def chr_decode(self, string):
        pass


def priview_handle(string):
    print_preview("Now, checking the string status...")
    print(f"[+] string: {string.encode()} -> {string} ")
    print(f"[+] length: {len(string)}")
    _chardet = chardet.detect(string.encode())
    encoding = _chardet['encoding']
    print(f"[+] Chardet: {_chardet}")
    zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
    match = zhPattern.search(string)
    print("[+] Type: ", end="")
    if match:
        cprint("Chinese char in string", "white", "on_cyan")
    else:
        cprint("ASCII String", "white", "on_grey")
    print("[+] origin hex:", end="")
    cprint(binascii.hexlify(string.encode()), "yellow", end="   ")
    cprint(" ".join(["0x"+str(c) for c in string.encode()]), "yellow")
    return match


def decode(string, isChinese):
    print_preview("\nDeCode Result:")
    utils = Utils()
    utils.html_decode(string)
    utils.url_decode(string)
    utils.base64_decode(string)
    utils.chr_decode(string)

def encode(string, isChinese):
    print_preview("\nEnCode Result:")
    # html entity encode
    utils = Utils()
    utils.html_encode(string, isChinese)
    utils.url_encode(string)
    utils.md5_encode(string)
    utils.base64_encode(string)
    utils.chr_encode(string, isChinese)



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
    Online Tools:https://tool.leavesongs.com/ (Others)
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
    string = args.string
    # check input string
    isChinese = priview_handle(string)
    # start to handle the input string
    if args.decode == True:
        result =  decode(string, isChinese)
    if args.encode == True:
        result =  encode(string, isChinese)
    if not args.decode and not args.encode:
        print("missing type to hanle string, example -d abc or -e abc")

if __name__ == '__main__':
    main()