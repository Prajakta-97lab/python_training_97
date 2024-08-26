#Count the number of perfect squares in the list of numbers


def count_perfect_squares( numbers ):
    perfect_square = 0
    for  number in numbers:
        if int(number**0.5)**2 == number:
             perfect_square +=1
    return perfect_square
numbers = [1,2,3,4,5,6,7,8,9,10]
result = count_perfect_squares(numbers)
print(f'nmuner of customers eligible of discount :{result}')
    
    

