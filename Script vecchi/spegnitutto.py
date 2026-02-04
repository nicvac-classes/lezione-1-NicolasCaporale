#!/usr/bin/env python3
# NOTA: si raccomanda di usare questo template anche se non lo si capisce completamente.

import sys

# decommenta le due righe seguenti se vuoi leggere/scrivere da file
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input().strip())
for test in range(1, T+1):
    input()
    N = int(input().strip())

    A = list(map(int, input().strip().split()))

    ris = 0

    for i in range(N):
        if A[i] == 1:
            ris += 1
            if i < N - 1 and A[i + 1] == 1:
                A[i + 1] = 0
            A[i] = 0


    print("Case #%d: " % test, end='')
    print(ris)

sys.stdout.close()
