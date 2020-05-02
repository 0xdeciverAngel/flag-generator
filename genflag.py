#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random
char_map = [
    ['A', 'a', '4', '@'],
    ['B', 'b', '8'],
    ['C', 'c'],
    ['D', 'd'],
    ['E', 'e', '3'],
    ['F', 'f'],
    ['G', 'g', '6'],
    ['H', 'h'],
    ['I', 'i', '1'],
    ['J', 'j'],
    ['K', 'k'],
    ['L', 'l', '1'],
    ['M', 'm'],
    ['N', 'n'],
    ['O', 'o', '0'],
    ['P', 'p'],
    ['Q', 'q'],
    ['R', 'r'],
    ['S', 's', '5', '$'],
    ['T', 't', '7'],
    ['U', 'u'],
    ['V', 'v'],
    ['W', 'w'],
    ['X', 'x'],
    ['Y', 'y'],
    ['Z', 'z', '2'],
  	['0', 'o', 'O', 'Q'],
  	['1', 'l', 'i', 'I'],
  	['2', 'z', 'Z'],
  	['3', 'e', 'E'],
  	['4', 'A'],
  	['5', 's', 'S', '$'],
    ['6'],
   	['7'],
  	['8''&', 'B'],
   	['9', '?'],
]


def change(c):
    if c.isalpha():
        c = c.upper()
        char_set = char_map[ord(c) - ord('A')]
        return char_set[random.randint(0, len(char_set) - 1)]
    if c.isnumeric():
        char_set = char_map[ord(c) - ord('0')+26]
        return char_set[random.randint(0, len(char_set) - 1)]
    else:
        return '_'


# str_in = input('input:')
str_in = "0123456789"
# str_in = "my name is 0xdeciverAngel"
for c in str_in:
    print(change(c), end='')
