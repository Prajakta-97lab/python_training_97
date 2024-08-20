#Accept a number as input, say X and describe a logic to get the outut say Y. The Input can be only 0 or 1 and the Output must be 1 if input is 0 and viceversa.

X = int(input('Enter the input number(0 or 1 only):'))

Y = 1-X
print(f'Input number = {X}, Output number = {Y}')

if X == 0:
    Y = 1
elif X == 1:
    Y = 0