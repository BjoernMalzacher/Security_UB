import numpy as np
import matplotlib.pyplot as mp

def rot(arr:list):
    temp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[-1] = temp
count =0
with open(r"C:\Users\malza\Security_UB\U1\ciphertext.txt", 'r') as file:
    li = file.readline()
    line = list(li)
    rotted_line = list(line)
    rot(rotted_line)
    print(len(line))
    c = [None]*30
    for i in range(30):
        rot(rotted_line)
        for l, rl in enumerate(line):
            if rotted_line[l] == rl:
                count +=1
        c[i] = count
        print(count)
        count = 0;
    mp.plot(np.linspace(0,len(line), 30),c)
    mp.show()