# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.
x = str(input('Enter the month of the year (Jan - Dec): '))
y = int(input('Enter the day of the month: '))
date = x + ' ' + str(y)
if x in 'Jan Feb':
  print(f'{date} is in Winter')
elif x in 'Mar' and y <= 19:
  print(f'{date} is in Winter')
elif x in 'Mar' and y > 19:
  print(f'{date} is in Spring')
elif x in 'Apr May':
  print(f'{date} is in Spring')
elif x in 'Jun' and y <= 20:
  print(f'{date} is in Spring')
elif x in 'Jun' and y > 20:
  print(f'{date} is in Summer')
elif x in 'Jul Aug':
  print(f'{date} is in Summer')
elif x in 'Sep' and y <= 21:
  print(f'{date} is in Summer')
elif x in 'Sep' and y > 21:
  print(f'{date} is in Fall')
elif x in 'Oct Nov':
  print(f'{date} is in Fall')
elif x in 'Dec' and y <= 20:
  print(f'{date} is in Fall')
elif x in 'Dec' and y > 20:
  print(f'{date} is in Winter')
else:
  print('you ended up here by probably giving the date and month at the same time. try again and read he questions precisely')
