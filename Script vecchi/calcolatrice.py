#!/usr/bin/env python3
# NOTA: si raccomanda di usare questo template anche se non lo si capisce completamente.

import sys

# decommenta le due righe seguenti se vuoi leggere/scrivere da file
sys.stdin = open('input.txt')
#sys.stdout = open('output.txt', 'w')

T = int(input().strip())
for test in range(1, T+1):
    input()
    N = int(input().strip())

    operazioni = 1

    while(N > 2):
        operazioni += 1
        if(N%2 != 0):
            N += 1
        else:
            N = N//2
        
    


    print("Case #%d: " % test, end='')
    print(operazioni)

sys.stdout.close()
