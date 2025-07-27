"""
#while loop
count = 1   # it means Iterator starts from 1
while count <= 100:
    print("hello") 
    count += 1

print(count)

"""
# print 5 to 1 using while loop

"""

i = 5
while i >= 1:
    print(i)
    i -=1
    
"""
"""
# infinite loop example
i = 5
while i <= 6:
    print(i)
    i -= 1
    print("loop ended")
    """
# practice of while loop

"""
i = 1
while i <= 100:
    print(i)
    i += 1

    """
"""
# print 100 to 1 using while loop
i = 100
while i >= 1:
    print(i)
    i-=1

 """
# print multiplication tables
"""
n = int(input("Enter a number for multiplication table: "))
i = 1
while i <= 10:
    print(n * i)
    i +=1

 """

"""
nums = [1 , 4 , 9 ,16 ,25, 36, 49, 64, 81, 100]

idx = 0
while idx <= 9:
    print(nums[idx])
    idx += 1

 # subtracting 1 from index
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 10
while idx > 0:
    idx -= 1
    print(nums[idx])

    """
# Searching for an element in a tuple using while loop

"""
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 64

idx =0
while idx <= 9:
    if (nums[idx]==x):
        print("found at index:", idx)
        print("finding")
        break
    idx += 1

    """
# Breaking out of a while loop

"""
i = 1 
while i <=5:
    print(i)
    if(i==4):
        print("Breaking the loop at 4")
        break
    i += 1
    """

# continue statement in while loop
"""
i = 0 
while i <= 5:
   
    if ( i==3):
        i+=1
        continue
    print(i)
    i += 1
    """



# For loop

"""
nums = [ 1 , 2 , 3 , 4 , 5]

for val in nums:
    print(val)
    """
# for with string
"""
str = "HelloWorld!"
for char in str:
    print(char)
    """
"""
str = "tejastagde"
for char in str:
    if ( char == "g"):
        print( "founded")
        break
    print(char)

 """
# print elemnts of the list

"""
list = [ 1 , 4 , 9 , 16 ,25, 36 , 49,64,81,100]
for num in list:
    print(num)
    """

# searching element in the list
"""
list = [1,4,9,16,25,36,49,64,81,100]
for num in list:
    if(num==49):
        print("found")
        break
    else:
        print("not found")

    """

# Range()

#print(range(5))
"""
seq = range(5)

for i in seq:
    print(i)
    """

"""
for i in range(2,10):   # range(start,stop)
    print(i)

for i in range(2,10,3):   # range(start,stop,step)
 print(i)

 """
# even no print
"""
for i in range(2 ,100,2):
    print(i)
    """

# practice Qus
"""
for i in range(1,100):
    print(i)
    

for i in range(100,0,-1):
    print(i)
    """
# practice Qus
"""
n = int(input("enter any number:"))

for i in range(1,11):
    print(n*i)
    """

#pass statement
"""
for i in range(5):
    pass

print(i)
"""

# Practice Qus
"""
n = 5 

sum = 0
for i in range(1,n+1):
    sum +=i
    print(sum)
    """

# Practice Qus
"""
#factorial
n = 3
fact =1
i = 1
while i <=n:
    fact *= i
    i +=1
    print(fact)
    """

# factorial using for loop 

n = 20
fact =1

for i in range(1,n+1):
    fact *=i
    print("factorial =",fact)
