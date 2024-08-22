#Program to find the sum of even(odd) digits in a number


num = int(input("Enter the number"))
even_sum = 0
while num>0:
    temp = num%10
    if temp%2==0:
        even_sum = even_sum + temp 
    num = num//10
print("Sum of even digits in number is:",int(even_sum))