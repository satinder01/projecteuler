#!/Users/satinderjitsingh/anaconda3/bin/python

'''
Amicable numbers

Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import math

def sum_of_divisors(n):
  set_of_divisors={1}
  max_divisor = int(math.sqrt(n)) + 1
  for i in range(2, max_divisor):
      if(n%i==0):
         set_of_divisors.add(i)
         set_of_divisors.add(n/i)
  return sum(set_of_divisors)

amicable_number={0}
for a in range(2, 10000):
    b = sum_of_divisors(a)
    if (sum_of_divisors(b) == a) and (a!=b):
        amicable_number.add(a)
        amicable_number.add(b)
       
print(sum(amicable_number))
