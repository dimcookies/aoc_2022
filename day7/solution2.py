from re import S
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

fs = {}
current_path=[""]
t=[]
for i in input:
    cmd = i.split()
    pr(i_s, cmd)
    if cmd[0] == '$':
        if cmd[1] == 'cd':
            if cmd[2] == '/':
                current_path=[""]
            elif cmd[2] == '..':
                current_path = current_path[:-1]
            else:
                current_path.append(cmd[2])
            pr(i_s,"Changed path:" + "".join(current_path))
        elif cmd[1] == 'ls':
            continue
    else:
        item = cmd[1] if cmd[0] == 'dir' else int(cmd[0])
        s="".join(current_path)
        if s in fs:
            fs[s].append(item)
        else:
            fs[s] = [item,]
pr(i_s, fs)
def du(dir):
    sz =0
    for i in fs[dir]:
        if type(i) is int:
            sz+=i
        else:
            sz+=du(dir+i)
    return sz

sz = sorted([du(i) for i in fs])
lmt = abs(70000000-du("")-30000000)
print([i for i in sz if i > lmt])