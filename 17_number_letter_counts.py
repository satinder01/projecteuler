#!/Users/satinderjitsingh/anaconda3/bin/python

'''
Number letter counts

Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

dict= {
   
    0:'',
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
    1000:'onethousand'
}


string=''
str_len=0
for i in range(1,1001):
  try:
    string = string+dict[i]
    str1=dict[i]
   
  except:
    if(i<100):
      number=((i//10)*10)
      remainder=i-number
      str1=dict[number]+dict[remainder]

    else:
      number=(i//100)
      remainder1 = i-number*100
     
      if(remainder1<=20):
        remainder2 = remainder1
        remainder3 = 0

      else:
        remainder2= remainder1 - remainder1%10
        remainder3 = remainder1%10

      if remainder2:
          and1="and"
      else:
          and1=""
      str1=dict[number]+"hundred"+and1+dict[remainder2]+dict[remainder3]
  str_len=str_len+len(str1)

print(str_len)
