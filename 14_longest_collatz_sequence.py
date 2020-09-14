#!/Users/satinderjitsingh/anaconda3/bin/python
'''
Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

'''

longest_array=[]
for i in range(2,1_000_000):
  n=i
  array=[n]
  while(n!=1):
    if(n%2==0):
      n = n / 2
    else:
      n = 3 * n + 1
    array.append(n)
  if len(longest_array) < len(array):
    longest_array=array 
    store_num=i
print(store_num)
#print("longest_array: ", longest_array)