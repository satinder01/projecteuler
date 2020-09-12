#!/Users/satinderjitsingh/anaconda3/bin/python

'''
Sum square difference

Problem 6
The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + 3^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is, (1 + 2 + 3 + ... + 10)^2 = 55^2 = 3052

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

'''
Using following equations to solve
1^2 + 2^2 + 3^2 + ..... = n(n+1)(2n+1)/6
(1 + 2 + 3 + ..... )^2 = (n(n+1)/2)^2
'''

n = 100
sum_of_squares = n * (n+1) * (2 * n + 1) / 6
sum_of_numbers_squared = (n * (n + 1) / 2 ) ** 2 

print(sum_of_numbers_squared - sum_of_squares)


