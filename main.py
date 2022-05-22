import random
import os
import time
import itertools
from array import *

#====================Functions====================
def generateOptions(bits_length):
    print("------------------------------Number of key options------------------------------\n")
    for i in bits_length:
        try:
            res = (2**i)
            symbolsInLine = len(str(res))
            print(f"{i}-bits = {res} [{symbolsInLine}]\n")
        except OverflowError:
            print(f"{i}-bits = inf")

def generateKeys(bits_length, key_dict):
    print("\n------------------------------Generated keys------------------------------\n")
    for i in bits_length:
        try:
            key = random.getrandbits(i)
            key_dict[int(key)] = key
            print(f"=========={i}-bit encryption key==========\n{key}\n=========================================\n")
        except OverflowError:
            print(f"{i}-bits = inf")

def brute_force(key_dict):
    limit = 2**4096
    key_found = 0
    start = time.monotonic_ns()
    for i in range(limit):
        search_key = key_dict.get(i, False)
        if search_key:
            finish=time.monotonic_ns() 
            duration = finish -  start
            print(f"[+] Key {i} picked up in {duration//1000000}ms")
            key_found += 1

    print(f"[!] Total Keys found: {key_found}")

#====================Main====================
bits_length = array('i', [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096])
key_dict = dict()

generateOptions(bits_length)
generateKeys(bits_length, key_dict)
brute_force(key_dict)
