 # Basic tuple creation and type checking

"""
tup = (1, 2, 3, 4, 5)
print(type(tup))

"""

# Accessing elements in a tuple

"""
tup = (1, 2, 3, 4, 5)
print(tup[3])

# empty tuple
tuple =()
print("Empty tuple:", tuple)

# 
tr = (1)
print("Single element tuple:", tr)

"""
# tuple Methods

"""
tup = (1, 2, 3, 4, 5 , 4 ,4)
print(" original tuple:", len(tup))
print("First element of tuple:", tup[0])  # Accessing the first element
print("Sliced tuple:", tup[1:4])  # Slicing the tuple from index 1 to 3
print(" index of element 3 in tuple:", tup.index(3))  # Finding the index of element 3
print("Count of element 4 in tuple:", tup.count(4))  # Counting occurrences of element 4

"""

# practiceing 

# Addinng movies to a list

"""
mov = [ ]
movie1 = input("enter first movie name: ")
movie2 = input("enter Second movie name: ")
movie3 = input("enter Third movie name: ")

print( mov.append(movie1))  # This will raise an error because tuples do not have an append method
print( mov.append(movie2))  # This will also raise an error
print( mov.append(movie3))  # This will also raise an error 

print("Movies in list:", mov)

"""

# palindrome check using tuple

"""
list1 = [ 1 ,2 , 1]
list2 = [1 , 2 , 3]

palindrome = list1.copy()
palindrome.reverse()  # Reversing the list to check for palindrome

if list1 == palindrome:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")  

palindrome2 = list2.copy()
palindrome2.reverse()  # Reversing the second list to check for palindrome
if list2 == palindrome2:
    print("The second list is a palindrome.")
else:
    print("The second list is not a palindrome.")

 """
"""
tuple1 = ["A" , "B", "C", "A", "A" ,"D", "B", "C"]
print( tuple1.count("A"))
print("Count of 'A' in tuple1:", tuple1.count("A"))  # Counting occurrences of 'A'

"""


tuple1 = ["A" , "B", "C", "A", "A" ,"D", "B", "C"]
print(tuple1.sort())
print("Sorted tuple1:", sorted(tuple1))  # Sorting the tuple

