import math
import random
import os
from array import *

#====================generating Functions====================
def generateOptions(bits_length):
    print("------------------------------Number of key options------------------------------\n")
    for i in bits_length:
        try:
            res = (2**i)
            symbolsInLine = len(str(res))
            print(f"{i}-bits = {res} [{symbolsInLine}]")
        except OverflowError:
            print(f"{i}-bits = inf")

def generateKeys(bits_length):
    print("\n------------------------------Generated keys------------------------------\n")
    for i in bits_length:
        try:
            key = random.getrandbits(i);
            print(f"=========={i}-bit encryption key==========\n{key}\n==========end of encryption key==========\n\n")
        except OverflowError:
            print(f"{i}-bits = inf")

#====================Main====================
bits_length = array('i', [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096])
generateOptions(bits_length)
generateKeys(bits_length)
