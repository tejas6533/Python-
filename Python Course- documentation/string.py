  # for next line we use \n to create a new line
"""
str1 = "hello world \nhow are you doing"
print(str1)

"""
 #space between two words we use \t
"""
str1 = "hello world \thow are you doing"
print(str1)

"""
# Concatenation of two strings
"""
str1 = "Nag"
str2 = "pur"
print("Concatenation of two strings is:", str1 + str2)

"""
# length of string
"""

str1 = "NamasteDuniya"
print("Length of string is:", len(str1))

str2 ="HelloWorld"
print("Length of string is:", len(str2))

final_str = str1 + str2
print("Length of final string is:", len(final_str)+5)


"""
# indexing of string
"""
str1 = "PokeMon pikachu"
seen = input("Enter the character to see its index: ")

if seen in str1:
    print("First index of character is:", str1.index(seen))
else:
    print("Character not found in the string.")

  """
# slicing of string
"""
str = "PokeMon pikachu"
print("Sliced string is:", str[0:5])  # Slicing from index 0 to 4

"""
"""
str = "PokeMon pikachu"
print ("Sliced string is:", str[7:])  # Slicing from index 5 to end
print ("Sliced string is:", str[:7])  # Slicing from index 5 to end

"""

# negative slicing of string
"""
str ="Postman"
print("Sliced string is:", str[-3:-1])  # Slicing from the third last character to the end

"""

"""
str = "Postman"
print(" enter end char  :" , str.endswith("an"))
print(" enter start char  :" , str.startswith("Po"))
print(" enter char  :" , str.find("t"))  # Find the index of character 't'
print(" enter char  :" , str.index("t"))  # Find the index of character 't'
print(" enter char  :" , str.count("o"))  # Count occurrences of character 'o'
print(" enter char  :" , str.isalpha())  # Check if all characters are alphabetic
print(" enter char :" , str.capitalize())  # Capitalize the first character
print(" enter char :" , str.replace("o" , "a"))  # replace 'o' with 'a'

"""
"""
str1 = input("Enter a string: ")
print("length of this is ",  len(str1))

"""

"""
str1 = (" hello$$$ worlds")
print(" count no of char", str1.count("$"))

"""