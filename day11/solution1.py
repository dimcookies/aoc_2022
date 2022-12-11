from re import S
import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
import os
import math
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

input = my_input.readlines(file_input)
pr(i_s, input)    

monkeys = []
item = {}
ops = {}
tst = {}
dec = {}
res = {}
for i in chunker(input, 7):    
    id = int(i[0].split(" ")[-1].replace(":",""))
    monkeys.append(id)
    res[id] = 0
    item[id] = [int(j) for j in i[1].replace("Starting items: ","").replace(" ","").split(",")]
    ops[id] = i[2].replace("Operation: new = ","")
    tst[id] = int(i[3].split(" ")[-1])
    dec[id] = (int(i[4].split(" ")[-1]), int(i[5].split(" ")[-1]))

for round in range(20):
    for monkey in monkeys:
        while item[monkey]:
            old=item[monkey].pop(0)
            res[monkey]+=1
            #pr(i_s, old)
            new=eval(ops[monkey])
            #pr(i_s,new)
            new=int(new/3)
            #pr(i_s,new)
            new_monkey = dec[monkey][0] if new%tst[monkey] == 0 else dec[monkey][1]
            #pr(i_s,new_monkey)
            item[new_monkey].append(new)
    print(item)

print(math.prod(sorted(res.values())[-2:]))