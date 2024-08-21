#Program to check if user given year is a leap year


year = int(input("Enter the year:"))
if year % 4 == 0:
    print("The user given year is leap year")
else :
    print("The user given year is not a leap year")