import math 
import numpy as np

iter = int(input('Put n '))
step = int(input('Put k '))

a = [None]*iter
a[0]= 1
a[1]= 1

for i in range(2,iter):
    if i <= step- 1:
        a[i]= a[i-1] + a[i-2]
    else:
        a[i]= a[i-1] + a[i-2] - a[i-step]
print(a[iter])
