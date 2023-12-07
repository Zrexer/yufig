#!/usr/bin/env python3

"""
Copyright 2023 host1let

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
"""

from ascii_magic import AsciiArt
import sys

lis = sys.argv

def handle(path):
    art = AsciiArt.from_image(path)
    art.to_terminal()

def check_formats(format_ : str):

    flist = ["jpg", "png", "svg", "jpeg"]

    if format_.split(".")[-1] in flist:
        return True

    else:
        False

if "--path" in lis:
    try:
        path = lis[lis.index("--path")+1]
        if check_formats(path):
            handle(path)
        else:
            print("[ - ] The {} its not in [jpg, jpeg, png, svg]".format(path))

    except Exception as E:
        print("[ - ] Error: {}".format(E))
