#!/Users/satinderjitsingh/anaconda3/bin/python

'''
Multiples of 3 and 5

Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

multiples_of_3_or_5={0}
i=1
multiple3=0
multiple5=0

while(i*3<1000):
  multiple3=i * 3
  multiples_of_3_or_5.add(multiple3)
  i=i+1

i=1
while(i*5<1000):
  multiple5=i * 5
  multiples_of_3_or_5.add(multiple5)
  i=i+1
  
print(sum(multiples_of_3_or_5))

