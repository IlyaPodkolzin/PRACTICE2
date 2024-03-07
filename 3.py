import random
import string
from ctypes import c_uint32


def func31(s):  # 3.1
    return [int(sel) for sel in s]


def func32(s):  # 3.2
    print(len(set(s)))


def func33(s):  # 3.3
    return s[::-1]


def func34(s, x):  # 3.4
    return [index for index in range(0, len(s)) if s[index] == x]


def func35(s):  # 3.5
    return sum([s[k] for k in range(len(s)) if k % 2 == 0])


def func36(s):  # 3.6
    return max([len(el) for el in s])


def func37(s):  # 3.7
    return (s % sum([int(el) for el in str(s)])) == 0


def func38(max_num):
    return ''.join([random.choice(string.ascii_letters) for _ in range(max_num)])


# print()
# print(func31(["12", "24", "36"]))
# func32('aaaaaaabbbcda')
# print(func33("abcdefg"))
# print(func34("Hello, World!HelloHellHello!", "H"))
# print(func35([1, 2, 3, 4, 5, 6, 10, 150, 10000]))
# print(func36(['ddsf', 'wrgfhryjyrhgr', 'r']))
# print(func37(12))
# print(func38(10))