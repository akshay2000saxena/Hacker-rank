#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    ans = bin(n)

    fin = str(ans)
    count = 0
    res = fin[0]

    for i in range(len(fin)):
        ncount = 1
        for j in range(i + 1, len(fin)):
            if(fin[i] != fin[j]):
                break
            ncount += 1
        if ncount > count:
            count = ncount
    print(count)


