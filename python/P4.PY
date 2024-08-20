#Program to Accept 3 distict numbers and find smallest among them.
num_1 = int(input('Enter first number:'))
num_2 = int(input('Enter second number:'))
num_3 = int(input('Enter third number:'))
if  num_1<num_2 and num_1<num_3:
     print(f'{num_1} is the smallest')
elif num_2<num_3:
     print(f'{num_2} is smallest')
else:
     print(f'{num_3} is smallest')