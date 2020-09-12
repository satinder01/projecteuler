#!/Users/satinderjitsingh/anaconda3/bin/python
'''
Largest prime factor

Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

import math
number = 600851475143
#number = 13195
n = int(math.sqrt(number))
list_primes = []
for i in range(2,n+1):
    if number%i==0:
      list_primes.append(i)
      number=number/i

print(max(list_primes))
