#!/Users/satinderjitsingh/anaconda3/bin/python

'''
Summation of primes

Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''

import math

n=2_000_000
A = {k:True for k in range(2,n)}

k=int(math.sqrt(n))
k=k+1

for i in range(2,k):
  if A[i] == True:
    for j in range(i*i, n, i):
      A[j] = False
sum=0
for key, val in A.items(): 
    if val == True: 
        sum = sum + key
print(sum)
