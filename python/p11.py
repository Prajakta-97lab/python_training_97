#Find the sum of digits of a number


num  = int(input("Enter the number whose sum of digits should be calculated:"))
t = num
sum  = 0
while num!=0:
    j = num%10
    sum = sum+j
    num = num//10
print(sum,"is the sum of digit in ", t)  