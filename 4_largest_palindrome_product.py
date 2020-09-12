#!/Users/satinderjitsingh/anaconda3/bin/python

'''
Largest palindrome product

Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

list=[]
for i in range(999*999, 100*100-1, -1):
  stri = str(i)
  if stri[0] == stri[-1] and stri[1]==stri[-2] and stri[2]==stri[-3]:
    list.append(i)

for number in list:
   for i in range (999, 99, -1):
      ### have to check quotient is less than 999 so it still valid 3-digit number
      if number%i==0 and number/i<=999:
        print(number)
        exit()
