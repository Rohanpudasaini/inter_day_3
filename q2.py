# 2. Write an if statement to determine whether a variable holding a year
# is a leap year.


year = int(input("year in number: ")) 

if year %4 != 0 or (year%100 == 0 and year%400 != 0):
    print("Not Leap year")
else:
    print("Leap year")