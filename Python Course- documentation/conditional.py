 # Apply license based on age

"""
age = input("Enter your age: ")
age = int(age)

if age >= 18:
    print(" you can apply license")
elif ( age <= 18):
    print(" you can not apply license")
else:
    print("Invalid age")

"""
# marks based conditional statements

"""
marks = int(input("Enter your marks: "))
if marks >= 45:
    print("You are pass")
elif marks < 45 and marks >= 20:
    print("You are fail")
else:
    print("Invalid marks")

"""

# nesting of if-else statements 
"""
age = int(input(" enter your age :"))
if  age >= 18:
   if age >=60 :
         print("You are senior citizen not drive")
   else:
      
      print(" you can drive")
else:
    print("You are not eligible to drive")
"""

# To check if a number is even or odd

"""

num = int(input("enter any number :"))
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

"""

# Greatest of three numbers

"""
num1 = int(input(" Enter first number: "))
num2 = int(input(" Enter first number: "))
num3 = int(input(" Enter first number: "))
if num1 > num2 and num1 > num3:
    print("First number is greatest")
elif num2 > num1 and num2 > num3 :
    print("Second number is greatest")
else:
    print("Third number is greatest") 

 """
# To check if a number is multiple of 7 or not

num = int(input("Enter a number: "))
if num % 7 == 0:
    print("Number is a multiple of 7")
else:
    print("Number is not a multiple of 7")