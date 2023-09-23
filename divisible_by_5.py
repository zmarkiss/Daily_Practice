#  Use the list numbers to create a new list in which all the integers are divisible by 5. 
#  Print it.


numbers = [i + 5 for i in range(0, 97)]
divisible_by_5 = [i for i in numbers if i % 5 == 0]
print(divisible_by_5)