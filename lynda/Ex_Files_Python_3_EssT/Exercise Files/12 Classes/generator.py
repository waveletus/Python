#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class my_range:
    def __init__(self, *args):
        arglen = len(args)
        if (arglen == 1):
            self.start = 0
            self.step = 1
            self.end = args[0]
        elif (arglen == 2):
            self.start, self.end = args
            self.step = 1
        elif (arglen == 3):
            self.start, self.end, self.step = args
        else:
            raise TypeError("Invalid parameter")

    def __iter__(self):
        i = self.start
        while i < self.end:
            yield i
            i = i + self.step



def main():
    for i in my_range(5, 25, 3,5): print(i, end = ' ')

if __name__ == "__main__": main()
