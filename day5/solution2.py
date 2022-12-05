import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
import os
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 


input = []
with open(os.path.join(sys.path[1], file_input), "r") as f:
    input = [i.replace("\n","") for i in f.readlines()]
pr(i_s, input)    
  
p1 = []

def parse_instruction(s):
    ar=s.split()
    return [int(i) for i in (ar[1],ar[3], ar[5])]

cnt=0
for i in input:
    if not i:
        break
    p1.append(i)
    cnt+=1
pr(i_s,p1)

c_num = max([int(i.strip()) for i in p1[-1].strip() if i.strip()])
pr(i_s,c_num)

buckets = [[] for i in range(0,c_num)]

for i in p1[:-1]:
    for j in range(0,c_num):
        t = i[1+j*4]
        if t.strip():
            buckets[j].append(t)
pr(i_s,buckets)            

instructions = [parse_instruction(i) for i in input[cnt+1:]]
pr(i_s, instructions)

for i in instructions:
    frm = i[1]
    to = i[2]
    t_ar = []
    for j in range(0,i[0]):
        t_ar.append(buckets[frm-1].pop(0))
    t_ar.reverse()
    for j in t_ar:
        buckets[to-1].insert(0,j)

print("".join([i[0] for i in buckets]))        