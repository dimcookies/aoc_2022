import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
import os
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines(file_input)
pr(i_s, input)    

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

for i in input:
    pr(i_s, i)
    cnt = 0
    for k in range(0,len(i)):
        j=i[k:k+14]
        #pr(i_s, j)
        if len(j) == len(set(j)):
            print(cnt+14)
            break
        cnt+=1
        