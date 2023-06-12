# Write a function that takes a list of integers as input and returns the second highest integer in the list.
def find_second_highest(nums):
    # Remove duplicates and sort the list in descending order
    nums = sorted(list(set(nums)), reverse=True)
    
    # Check if there is a second highest number
    if len(nums) < 2:
        return None
    
    # Return the second highest number
    return nums[1]
nums=[2,3,5,6,7,8,9,8]
print(find_second_highest(nums))


# Write a function that takes two lists of integers as input and returns a list that contains only the elements that are common to both lists.
def common(list1,list2):
    newlist=[]
    for x in list1:
        if x in list2:
            newlist.append(x)
    return newlist
list1=["rita","prudence","kimm","alen","trishia","wendy"]
list2=["rita","kimm","Alen","trish","wen"]
print(common(list1,list2))        


# Write a function that takes a string as input and returns the longest substring without repeating characters.


# Write a function that takes a list of integers as input and returns the sum of the digits of all the integers in the list.
def integers_sum(integers):
    sum=0
        # Initialize the sum
    total_sum = 0
    
    # Loop through the list of integers
    for num in nums:
        # Convert the integer to a string and loop through its digits
        for digit in str(num):
            # Add the digit to the total sum
            total_sum += int(digit)
    
    # Return the total sum
    return total_sum
integers=[234,567,897]
print(integers_sum(integers))

       
    


# Write a function that takes a string as input and returns True if the string is a palindrome, and False otherwise.
def palindrome(string):
    strings="".join(reversed(string))
    print(strings)
    if strings==string:
        return"palindrome"
    else:
        return "not palindrome"
    
string="poop"
print(palindrome(string))    
     
    
    


# Write a function that takes a list of integers as input and returns the product of all the even integers in the list.
def product_even(integers):
    product=1
    for ints in integers:
        if ints %2==0:
            product*=ints
    return product
integers=[2,3,4,5]
print(product_even(integers))        



# Write a function that takes a list of integers as input and returns a new list that 
# contains only the unique elements in the original list, sorted in ascending order.
def unique_ascending(ints):
    unique=[]
    for x in ints:
        if x not in unique:
            unique.append(x)
    return sorted(unique)
ints=[57,7,89,3,4,4,90,5,5]
print(unique_ascending(ints))        


# Write a function that takes a string as input and returns the number of words in the string.
def stingnum(string):
    words=string.split()
    return len(words)
string="rita is a coding mania"
print(stingnum(string))


# Write a function that takes a list of integers as input 
# and returns a new list that contains only the prime numbers in the original list.

# Write a function that takes a list of integers as input and returns the difference 
# between the largest and smallest integers in the list.
def difference(lists):
    largest=max(lists)
    smallest=min(lists)
    return largest-smallest
lists=[2,3,4,5,6,7,8,9]
print(difference(lists))

# Write a Python function to find the second largest number in a list of integers.

# Write a Python function to check if a given number is prime or not.

# Write a Python function to calculate the area of a circle given its radius.
def area(radius):
    circle=3.14* radius*radius
    return circle
radius=3
print(area(radius))

# Write a Python function to calculate the sum of all even numbers in a list of integers.
def sum_even(ints):
    sum =0
    
# Write a Python function to find the length
#  of the longest consecutive sequence of a given list of integers.

# Write a Python function to find the minimum number of jumps required to reach the end of a given list of integers, where each element represents the maximum number of steps that can be taken forward from that position.
# Write a Python function to find the common elements between two lists of integers.
# Write a Python function to find the first non-repeated character in a given string.
# Write a Python function to generate all possible permutations of a given string.
# Write a Python function to find the maximum and minimum numbers in a list of numbers.

# Write a Python program to convert a list of integers into a single integer.




# Write a Python function to find the number of occurrences of a given element in a list.
def counting(ints,items):
    count=0
    for x in ints:
        if x ==items:
            count+=1
    return count
ints=[3,4,5,6,6,7,8,9]
items=6
total=counting(ints,items)
print((f"the number of ocurence of {items} is {total}") )       

# Write a Python program to sort a list of numbers using the bubble sort algorithm.

# Write a Python function to check if a given string is a palindrome or not.

# Write a Python program to find the median of a list of numbers.
# Write a Python function to find the factorial of a given number.

# Write a function named smallest that accepts a list of unsorted integers and returns the smallest number in the list.
def smallest(integers):
    small=integers[0]
    for ints in integers:
        if ints<small:
            small=ints
    return small
integers=[717,8998,4567,98,90,3]
print(smallest(integers))        


# Write a function that uses the range function and a for loop and returns 
# a list containing all the numbers between 100 and 200 that are divisible by 7
def divisble_by_7():
    divisible=[]
    values=range(100,200)
    for nums in values:
        if nums %7==0:
            divisible.append(nums)
    return divisible
print(divisble_by_7())        

# Write a program that takes two inputs(integers) from a user and adds the 2 numbers , 
# checks if the sum is greater than 10, less than 10 and equal to 10 and prints a 
# statement after each check.
def greater_than(int1,int2):
    sum=int1+int2
    if sum>10:
        print("the sum is greater than 10")
    elif sum <10:
        print("the sum is less than 10")
    elif sum ==10:
        print("sum is equal to 10")
    
int1=5
int2= 17
greater_than(int1,int2)                   
    
# Write a function that takes one argument which is a list of integers and returns True if 4 is present and False if not.
def present(ints):
    for i in ints:
        if 4 in ints:
            return True
        else:
            return False
ints=[2,3,5,4,6,7]
print(present(ints))        
        
# Write a function that takes one argument that is in a list of strings
#  ad removes the last element then returns a new list without the removed element

def remove_last_element(lst):
    lists.pop()
    return lst
  

lists=["rita","kim","wendy","hamadi"]
print(remove_last_element(lists))
#write a python program that takes a list of cars=['ford,'bmw','Volvo'] 
# and returns a sorted list 
def sorting(lists):
    lists.sort()
    return lists
lists=['ford','bmw','volvo'] 
print(sorting(lists))

def even_number():
    Number=0
    while Number<=50:
        if Number%2==0:
            Number+=1
            continue
        print(Number)
        Number+=1
even_number()        
    



