my_list =[]
list2 = [2,5,8,9]
list3= list(list2)
print(list3)

list4 = [2,3,4,5,6,]
list5 = [1,2,3,4,5,6,7,8,9,10]

if list4>list5:
    print("list4 is big")
else:
    print("list 5 is big")


print(f"Max = ",max(list2))
print(f"Min = ",min(list2))
print(f"Length = ",len(list2))
print(f"Sum = ",sum(list2))
print(f"Count of 2 = ", list2.count(2))

list6 = ['abc', 5, 'xyz', 10]
print(list6)
list2.sort()
print(list6)

list7 = [element for element in range(10,30,2)]
print(list7)


list7 = [element for element in input().split()]
print(list7)

list = 