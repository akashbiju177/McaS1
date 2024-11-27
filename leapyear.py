day=int(input("enter the day"))
month=int(input("enter the month"))
year=int(input("enter the year"))
print(f"entered date: {day:02d}/{month:02d}/{year}")
if (year % 4 ==0 and year % 100 !=0) or (year % 400 ==0):
    print(f"the year is {year} is a leap year")
else:
    print(f"the year is {year} is not a leap year")



