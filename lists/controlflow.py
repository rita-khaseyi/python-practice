 # Write a program that asks the user for their age 
#and prints "You are an adult" if their age is 18 or older, and "You are not an adult" if their age is under 18.   

age = int(input("What is your age? "))
if age >= 18:
    print("You are an adult")
# def age(ages):
#     if(ages<=18):
#         print("`you are not an adult")
#     else:
#         print("you are an adult")
# ages=19
# age(ages) 
#  Write a function called larger_number that takes two numbers as arguments 
# and returns the larger of the two.
def larger_number(num1,num2):
    if(num1>num2):
        return f"larger number is {num1}"
    else:
        return f"larger number is {num2}"
num1=7
num2=14
print(larger_number(num1,num2)) 

#Write a program that takes a list of numbers as input 
# and prints the sum of all the even numbers in the list.
def even_number(numbers):
    sum=0
    for i in numbers:
        if(i%2==0):
            sum+=i
    return f"sum of even numbers is {sum}"

# def even(list):
#     sum=0
#     for l in list:
#         if(l %2==0):
#             sum+=l
#     return sum
# list=[1,2,3,4,5,6,7,8,9,10]
# print(even(list)) 

#Write a program that takes a list of strings as input and
#  prints the length of the longest string in the list.
def longer_string(lists):
    
    largest=0
    for s in lists:
        if(len(s)>largest):
            largest=len(s)
    return largest
lists=["rita","trish","melvin","florence","nataliaimani"] 
print(longer_string(lists))  
#Write a program that takes a list of integers as input and prints
#  the sum of all even numbers in the list.
def even_sum(list):
    total=0
    for nums in list:
        if nums %2==0:
            total+=nums
    return f"the sum of even numbers is {total}"
list=[1,2,3,4,5,6]
print(even_sum(list))

#write a program that takes a list of numbers as input 
# and prints the average of all the numbers in the list.

def averages(numbers):
    sum=0
    for number in numbers:
        sum +=number
    return sum/len(numbers)
numbers=[10,20,30,40,50,60]
print(averages(numbers))

#Write a program that takes a list of integers as input
#  and prints the largest number in the list.
def largest_number(integers):
    largest=integers[0]
    for ints in integers:
        if ints>largest:
            largest=ints
    return f"the largest number in {integers} is {largest}"
integers=[1,2,3,4,5,6,7,905,1304]
print(largest_number(integers))

#Write a program that takes a list of integers as input and prints
#  the sum of all the numbers that are divisible by 3 or 5.
def evenSum(number):
    even=0
    for n in number:
        if n %3==0 or n %5==0:
            even+=n
    return even
number=[12,15] 
print(evenSum(number)) 

# Write a Python function called unique_chars that
#  takes a string as input and returns a new string 
# with all the duplicate characters removed. The order
#  of the characters in the resulting string should be 
# the same as the original string.
def unique_chars(string):
    lists=[]
    for char in string:
        if char not in lists:
            lists.append(char)
    return ''.join(lists)   
string="rita khaseyi"
print(unique_chars(string))  

# 

     
        


