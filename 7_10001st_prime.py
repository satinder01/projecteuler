#!/Users/satinderjitsingh/anaconda3/bin/python

'''Find 10001st prime'''

# starting with seed list
list_of_prime_numbers = [2, 3, 5, 7, 11, 13]


# making j the last known prime number
j = 13

# number of prime numbers
i = 6

while i < 10001:
  j = j + 1
  cond=True

# divide new number by already found prime numbers
  for number in list_of_prime_numbers:
    if j % number == 0:
       cond=False
       break
# if number cannot be divided by any prime numbers already found, add to the list as new prime number

  if cond:
    list_of_prime_numbers.append(j)
    i = i + 1

print(list_of_prime_numbers[-1])
  
