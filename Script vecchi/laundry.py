#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys

# uncomment the two following lines if you want to read/write from files
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

N, C, W = map(int, input().strip().split())

T = list(map(int, input().strip().split()))

ans = W

tempo = W
BATCH = []  

while len(T) > 0:
    if(len(T) >= C):
        BATCH = T[:C]
        T = T[C:]
    else:
        BATCH = T
        T = []
    ans += max(BATCH)
    if(tempo < ans):
        tempo += W
    
    ans += tempo

    
    BATCH.clear()


print(ans)

sys.stdout.close()
