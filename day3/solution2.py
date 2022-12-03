import sys
sys.path.insert(0, "..")
import my_input
from utils import pr

i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines(file_input)
pr(i_s, input)    

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def convert(chr):
    if chr >= 'a' and chr <= 'z':
        return ord(chr) - 96
    return ord(chr)-64+26

def to_set(s):
    return set([i for i in s])

s =0
for group in chunker(input, 3):
   ar=[to_set(i) for i in group ]
   s+=sum([convert(i) for i in ar[0].intersection(ar[1]).intersection(ar[2])])
print(s)
