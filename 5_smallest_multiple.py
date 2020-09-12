#!/Users/satinderjitsingh/anaconda3/bin/python

'''
Smallest multiple

Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

condition=True
i=0
divisor = 20

while condition:
  condition = False 
  i=i+1

  ## keeping prime numbers, without it the program runs for long time
  number = 19 * 17 * 13 * 11 * 7 * 5 * 3 * 2 * i

  for j in range(divisor, 1, -1):
    if(number%j) != 0:
      condition = True
      break

print(number)
