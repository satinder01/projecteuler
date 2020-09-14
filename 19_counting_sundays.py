#!/Users/satinderjitsingh/anaconda3/bin/python3

'''
Counting Sundays

Problem 19
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''

#Jan, Mar, May, Jul, Aug, Oct, Dec = 31
#Feb = 28 or 29 depending on leap year
#Apr, Jun, Sep, Nov = 30


## Year adder will add number to months so we can keep checking every year
year_adder = 0

## in year 1900 first sunday of the year is 7 Jan which is number 7 in 0 year.
sunday = 7
counter=-2

for year in range(1900, 2001, 1):
  if year%100==0 and not year%400==0:
    Feb_adder = 28
  elif year%4==0:
    Feb_adder = 29
  else:
    Feb_adder = 28

  Jan = 31 + year_adder
  Feb = Jan + Feb_adder
  Mar = Feb + 31
  Apr = Mar + 30
  May = Apr + 31
  Jun = May + 30
  Jul = Jun + 31
  Aug = Jul + 31
  Sep = Aug + 30
  Oct = Sep + 31
  Nov = Oct + 30
  Dec = Nov + 31
  
  
#if 01 Jan 1900 is Monday, print all Sundays in 1900
##print("Year...", year)

## counter starts from last sunday of previous year and jumps by 7 till last day of Dec this yearo
  for i in range(sunday, Dec, 7):
   if(i<=Jan and i-year_adder == 1):
     ##print("Jan: ", i-year_adder)
     counter += 1
   elif(i<=Feb and i-Jan == 1):
     ##print("Feb: ", i-Jan)
     counter += 1
   elif(i<=Mar and i-Feb==1):
     ##print("Mar: ", i-Feb)
     counter += 1
   elif(i<=Apr and i-Mar==1):
     ##print("Apr: ", i-Mar)
     counter += 1
   elif(i<=May and i-Apr==1):
     ##print("May: ", i-Apr)
     counter += 1
   elif(i<=Jun and i-May==1):
     ##print("Jun: ", i-May)
     counter += 1
   elif(i<=Jul and i-Jun==1):
     ##print("Jul: ", i-Jun)
     counter += 1
   elif(i<=Aug and i-Jul==1):
     ##print("Aug: ", i-Jul)
     counter += 1
   elif(i<=Sep and i-Aug==1):
     ##print("Sep: ", i-Aug)
     counter += 1
   elif(i<=Oct and i-Sep==1):
     ##print("Oct: ", i-Sep)
     counter += 1
   elif(i<=Nov and i-Oct==1):
     ##print("Nov: ", i-Oct)
     counter += 1
   elif(i<=Dec and i-Nov==1):
     ##print("Dec: ", i-Nov)
     counter += 1
  sunday=i
  year_adder = year_adder + 337 + Feb_adder
print(counter)
