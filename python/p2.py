#Read a number from the user and check if it's an Even no. or not.

#To read data from the console we can use input().However the input() always reads a string as usual with other languages.

#We must first cast a string into a no. [specifically an int()]

#The input(), not only reads a string but also can print a string 

my_number = int(input('Enter a number to check if it is Even or not: '))
print(type(my_number))

if my_number % 2 == 0:
    