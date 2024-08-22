#Program to find the second the smallest digit in a number


num = input("Enter the number:")
string = []
for i in str(num):
    if i not in string:
        string.append(i)

ascending_str = sorted(string)
print("The second smallest digit is:", ascending_str[1])