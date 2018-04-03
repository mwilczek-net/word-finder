#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import argparse

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("available", help="Available characters (number of occurence count)", type=str)
    parser.add_argument("--any", help="Number of 'any' characters", type=int, default="0")

    return parser.parse_args()

def wordToCharCount(word):
    characters = dict()
    for c in word:
        characters[c] = characters.get(c, 0) + 1

    return characters

def wordMatch(word, available, any_count):
    characters = wordToCharCount(word)
    for c in available:
        characters[c] = characters.get(c, 0) -1

    remainingLetters = [characters[c] for c in characters if ((characters.get(c, None) is not None) and characters[c] >= 0)]
    remainingLettersCount = sum(remainingLetters)

    return remainingLettersCount <= any_count

# -------------

if __name__ == '__main__':
    args = parseArgs();

    for line in sys.stdin:
        line = line.strip()
        if wordMatch(line, args.available, args.any):
            print line

