# Create a tuple with elements 1, 2, 3, and print the first and last elements of the tuple.
my_tuple=(1,2,3)
print(my_tuple[0])
print(my_tuple[-1])

# Create a tuple with elements "apple", "banana", "cherry",
#  and check if "banana" is present in the tuple.
fruits=("apple","banana","cherry")
if "apple" in fruits:
    print("yes")
else:
    print("not present")    

# Create a tuple with elements 1, 2, 3, 4, 5, and slice it 
# to get a new tuple with elements 2, 3, 4.
tuples=(1,2,3,4,5)
tuples1=tuples[1:4]
print(tuples1)

# Create two tuples with elements (1, 2, 3) and (4, 5, 6), and 
# concatenate them to get a new tuple with elements (1, 2, 3, 4, 5, 6).
def concatenation(tup1,tup2):
    new_tuple=tup1+tup2
    return new_tuple
tup1=(1,2,3)
tup2=(4,5,6)
print(concatenation(tup1,tup2))

# Create a tuple with elements "apple", "banana", "cherry",
#  and use the index method to find the index of "cherry" in the tuple.
def indexing(tuple):
    index=tuple.index("cherry")
    return index
tuple=("apple","banana","cherry")
print(indexing(tuple))

# Create a tuple with elements 1, 2, 3, and unpack it into three variables a, b, and c.
tuple1=(1,2,3)
a,b,c=tuple1
print(a)
print(b)
print(c)

# Create a tuple with elements 1, 2, 3, and convert it into a list.
mytuple=(1,2,3)
lists=list(mytuple)
print(lists)
# Create a tuple with elements 1, 2, 3, and use the count method 
# to count the number of occurrences of the element 2 in the tuple.
tuples3=(1,2,3)
print(tuples.count(2))
# Create a tuple with elements "apple", "banana", "cherry",
#  and use the len function to find the length of the tuple.
fruit=("apple","banana","cherry")
print(len(fruit))
# Create a tuple with elements "apple", "banana", "cherry", and use the sorted function 
# to get a new tuple with elements "apple", "banana", "cherry" in alphabetical order.
# Write a function that takes in a list of tuples, where each tuple contains a string and
#  an integer, and returns a new list of tuples where each tuple contains the string
#  from the original tuple repeated by the integer.

   

# Write a function that takes in a list of tuples, where each tuple contains two integers, and returns the sum of the first integer in each tuple multiplied by the second integer in each tuple.
# Write a function that takes in a list of tuples, where each tuple contains a string and a float, and returns a new list of tuples sorted by the float value in ascending order.
# Write a function that takes in two lists of tuples, where each tuple contains a string and an integer, and returns a new list of tuples that contains the elements from both lists, sorted by the integer value in ascending order.
# Write a function that takes in a list of tuples, where each tuple contains three integers, and returns a new list of tuples sorted by the sum of the integers in descending order.
# Write a function that takes in a list of tuples, where each tuple contains a string and a tuple of two integers, and returns a new list of tuples sorted by the second integer in the tuple within the original tuple, in descending order.
# Write a function that takes in a list of tuples, where each tuple contains a string and a boolean value, and returns a new list of tuples where the boolean value is inverted.
# Write a function that takes in a list of tuples, where each tuple contains a string and an integer, and returns the string with the highest integer value.
# Write a function that takes in a list of tuples, where each tuple contains a string and an integer, and returns a dictionary where the keys are the integers and the values are lists of strings that correspond to the integer.
# Write a function that takes in a list of tuples, where each tuple contains a string and a tuple of two integers, and returns a new list of tuples where each tuple contains the string from the original tuple and the sum of the two integers in the tuple within the original tuple.
# Write a Python program to create a tuple with different data types and print its length.
# Write a Python program to create a tuple and convert it into a list.
# Write a Python program to join two tuples.
# Write a Python program to slice a tuple.
# Write a Python program to find the index of an item in a tuple.
# Write a Python program to count the number of occurrences of an item in a tuple.
# Write a Python program to find the maximum and minimum values in a tuple.
# Write a Python program to reverse a tuple.
# Write a Python program to check if an element exists in a tuple.
# Write a Python program to convert a tuple to a string.
# Write a function that takes in two tuples of integers and returns a new tuple that contains the sum of each corresponding element in the two input tuples.
# Write a function that takes in a list of tuples, where each tuple contains a person's name and age. The function should return a new list of tuples, where each tuple contains the person's name and the number of years until they turn 100.
# Write a function that takes in a tuple of integers and returns a new tuple that contains only the even numbers from the input tuple.
# Write a function that takes in a tuple of integers and returns the index of the first occurrence of the number 5 in the tuple. If the number 5 is not in the tuple, the function should return -1.
# Write a function that takes in a tuple of strings and returns a new tuple where each string is reversed.
# Write a function that takes in a tuple of numbers and returns the product of all the numbers in the tuple.
# Write a function that takes in a list of tuples, where each tuple contains a student's name and their final exam score. The function should return a new list of tuples, where each tuple contains the student's name and their letter grade based on the following scale:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59
# Write a function that takes in two tuples of integers and returns a new tuple that contains the intersection of the two input tuples (i.e. the elements that are common to both input tuples).
# Write a function that takes in a tuple of integers and returns a new tuple that contains the cumulative sum of the elements in the input tuple.
# Write a function that takes in a list of tuples, where each tuple contains a student's name, their midterm exam score, and their final exam score. The function should return a new list of tuples, where each tuple contains the student's name and their overall grade based on the following formula:
# overall_grade = 0.4 * midterm_exam_score + 0.6 * final_exam_score


# Question 1: Write a function that takes a tuple of strings and 
# returns a new tuple with the lengths of each string.
      
def lengths(tuples):
    tuple1 = ()
    for item in tuples:
        tuple1 += (len(item),)  # Add a comma to create a tuple with a single element
    print(tuple1)

tuples = ("rita", "kim", "wendy", "alicia", "kamau", "wesh")
lengths(tuples)
       


# Question 2: Given two sets, write a program to find the difference
#  between the sets (elements present in the first set but not in the second set).
def diff(tup1,tup2):
    return tup1.difference(tup2)
tup1={"rita","aliyah","kimmy","mwangi"}
tup2={'wesh',"kamau","rita","kimmy"}
print(diff(tup1,tup2))




# Question 3: Write a function that takes a list of tuples, 
# each containing a name and an age, and returns a dictionary 
# where the name is the key and the age is the value.
def create_age_dictionary(tuples_list):
    age_dict = {}
    for name, age in tuples_list:
        age_dict[name] = age
    return age_dict

my_list = [("John", 25), ("Alice", 30), ("Bob", 35)]
age_dictionary = create_age_dictionary(my_list)
print(age_dictionary)


# Question 4: Write a program that takes a set of numbers and 
# returns a new set with only the prime numbers from the original set.


# Question 5: Given a tuple of numbers, write a program to find 
# the product of all the numbers in the tuple.
def product(tuples):
    prod=1
    for item in tuples:
        prod *=item
    return prod
tuples=(30,20,10)
print(product(tuples))    


# Question 6: Write a function that takes two sets as parameters
#  and returns a new set containing the elements that are common to both sets.
def common(tup3,tup4):
    return tup3.intersection(tup4)
tup3={2,3,4,5,6,7,8,9,10}
tup4={2,7,8,9,10,17,19}
print(common(tup3,tup4))

# Question 7: Write a program that takes a set of strings
#  and returns a new set with the lengths of each string.
def string_length(strings):
    tup5=set()
    for x in strings:
        tup5.add (len(x))
    return tup5
tup5={"rita","kimmy","lizzie","monique","loke"}
print(string_length(tup5))  



# Question 8: Given a list of tuples representing coordinates (x, y),
#  write a program to find the distance of each coordinate from the origin (0, 0) 
# and return a list of distances.

# Question 9: Write a function that takes a tuple of integers and 
# returns a new tuple with the numbers sorted in ascending order.

# Question 10: Given two sets, write a program to check if one set is a subset of the other.

# Question 11: Write a program that takes a set of strings and returns a new set with only the strings that start with a vowel.

# Question 12: Given a list of tuples representing (student name, subject), write a program to find the number of unique subjects.

# Question 13: Write a function that takes two tuples of numbers and returns a new tuple containing the element-wise sum of the tuples.

# Question 14: Given a set of numbers, write a program to find the average of all the elements in the set.

# Question 15: Write a program that takes a set of strings and returns a new set with only the strings in uppercase.

# Question 16: Given a list of tuples representing (name, age), write a program to find the oldest person(s) from the list.

# Question 17: Write a function that takes a tuple of integers and returns a new tuple with the numbers sorted in descending order.

# Question 18: Given two sets, write a program to find the symmetric difference between the sets (elements present in either set, but not in both).

# Question 19: Write a program that takes a set of strings and returns a new set with only the strings that are palindromes.

# Question 20: Given a list of tuples representing (student name, subject, score), write a program to find the subject(s) with the highest average score.

# Question 21: Write a function that takes two tuples of strings and returns a new tuple containing the element-wise concatenation of the tuples.

# Question 22: Given a set of numbers, write a program to find the maximum and minimum values in the set.

# Question 23: Write a program that takes a set of strings and returns a new set with the strings sorted in alphabetical order.

# Question 24: Given a list of tuples representing (name, salary), write a program to find the total salary of all employees.

# Question 25: Write a function that takes a tuple of numbers and returns a new tuple with the numbers squared.

# Question 26: Given two sets, write a program to check if they are disjoint (i.e., they have no common elements).

# Question 27: Write a program that takes a set of strings and returns a new set with only the strings that have more than 5 characters.

# Question 28: Given a list of tuples representing (name, age), write a program to find the average age of all the individuals.

# Question 29: Write a function that takes two tuples of numbers and returns a new tuple containing the element-wise multiplication of the tuples.

# Question 30: Given a set of strings, write a program 
# to find the longest string in the set.
def find_longest_string(string_set):
    longest_string = ""
    for string in string_set:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string

# Example usage
my_set = {"apple", "banana", "orange", "kiwi"}
longest = find_longest_string(my_set)
print(longest)



