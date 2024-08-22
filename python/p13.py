#Program to find the biggest and smallest digits in a number


num = int(input("Enter the number whose  biggest and smallest digits in a number is to be calculated:"))
t = num
digit = []
while num!= 0:
    i = num % 10
    digit.append(i)
    num = num//10
digit.sort()
print(digit[0],'is the smallest digit in ',t)
print(digit[-1],'is the biggest digit in ',t)

