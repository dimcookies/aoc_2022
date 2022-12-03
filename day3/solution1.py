import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines(file_input)
pr(i_s, input)    

def convert(chr):
    if chr >= 'a' and chr <= 'z':
        return ord(chr) - 96
    return ord(chr)-64+26

s=0
for i in input:
    t= int(len(i)/2)
    
    common = set([j for j in i[:t]]).intersection(set([j for j in i[t:]]))
    #print(common)
    #print([convert(i)  for i in common])
    s+=sum([convert(i)  for i in common])

print(s)    