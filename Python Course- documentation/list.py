"""
marks = [ 45 , 67, 89, 23, 56, 78, 90, 34, 12, 45 ]
print("Original list:", marks)
print(type(marks))
print(len(marks))
print(marks[0])  # Accessing the first element
print(marks[1:5])  # Slicing the list from index 1 to 4

"""
# list operations
"""
list = [ " nagpur", 43, "maharastra" ]
print("Original list:", list)

"""
# modifying list
"""
list = [ " nagpur", 43, "maharastra" ]
print(list[0])  # Accessing the first element
list[0] = "pune"  # Modifying the first element
print("Modified list:", list)

"""
# slicing of list
"""
list = [ " nagpur", 43, "maharastra", "pune", 56, "mumbai" ]
print(" sliced list is :" , list[1:4])
print(" sliced list is :" , list[2:])  # Slicing from index 2 to end
print(" sliced list is :" , list[:3])  # Slicing from start to index 2 

"""

# list methods

"""
list = [ 1, 5 , 3, 4, 2 ]
list.append(6)  # Adding an element to the end
print("List after append:", list)
list.sort()
print("List after sort:", list) # Sorting the list
list.reverse()  # Reversing the list
print("List after reverse:", list)
list.remove(3) # Removing an element
print("List after remove:", list)
list.insert(2, 10)  # Inserting an element at index 2 
print("List after insert:", list)

"""

 # sortinh of string list

"""
list1 =[ "nagpur" , "pune" , "mumbai" ]
list1.sort( reverse=True)  # Sorting the list in reverse order
print("Sorted list:", list1)  # Sorting the list
list1.sort()
print("Sorted list:", list1)  # Sorting the list in ascending order

"""

# pop method in list

"""
list2 = [ 1, 2, 3, 4, 5 ]
list2.pop(2)  
print("list after pop:", list2)

"""
