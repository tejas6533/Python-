# how to create a function
"""
def calc_sum(a,b):
    sum = a + b
    
    print(sum)
    return sum

calc_sum(5,6)

calc_sum(55,45)

"""
# function defination
"""
def calc_sum(a,b):  # parameter
    return a+b
sum=calc_sum(178,2221) #function call , argument
print(sum)

"""
"""
def calc_avarge(a,b,c):
    sum = a + b + c  
    avg = sum/3
    print(avg)
    return avg

calc_avarge(10,20,30)
"""
# types of function

#print("hello","how are you?") # build in function

"""
#mulitpation of two no

def multi_calc(a,b):
    multi = a*b
    print(multi)
    return a*b

multi_calc(5,7)

"""
"""
cities =["nagpur", "wardha", "chandrapur", "katol"]
fruit = ["orange","apple","banana"]

def print_len(cities):
    print(len(cities))
    print(len(fruit))

    return cities , fruit
    


print_len(cities)
print_len(fruit)
"""

"""
cities =["nagpur", "wardha", "chandrapur", "katol"]
fruit = ["orange","apple","banana"]



def show_list(cities,fruit):
    for i in cities :
        print( i , end="")

        show_list(fruit)
        show_list(cities)
"""
# calculate factorial using function calling

"""
def fact_no(n):
    fact = 1
    for i in range(1,n+1):
        fact *=i
        print(fact)

fact_no(5)

"""

# USD to INR 
"""
def converter(usd_val):
    inr_value = usd_val*86.46
    print(usd_val,"usd =", inr_value,"inr")

converter(100)

"""
# Recursion

#recursive function

"""
def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)
show(5)

"""

# recursion using factorial

"""
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return fact(n-1)*n
print(fact(5))

"""
"""
def cal_sum(n):
 
    if n==0:
        return 0
   
    return cal_sum(n-1)+n

sum=cal_sum(5)
print(sum)
"""

def list_n(list,idx=0):
    if(idx==len(list)):
     return 
    print(list[idx])
    list_n(list,idx+1)

fruit =["mango","banana", "apple"]
list_n(fruit)
