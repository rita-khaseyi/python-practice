#Create a list of integers and print out the sum of all the numbers in the list.
list1=[2,4,6,8,10]
addition=sum(list1)
print(addition)

#Write a function that takes a list of integers and returns the largest number in the list.
def largests(lists2):
    largest=list2[0]
    for lis in list2:
      if lis>largest:
          largest=lis
    return largest      
list2=[2,4,5,6,7,8,9]
large=largests(list2)
print(large)

#Write a program that takes a list of integers and returns a new list with only the even numbers from the original list.

def evenNumbers(numbers):
    even=[]
    for number in numbers:
        if number %2==0:
            even.append(number)
    return even
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = evenNumbers(my_list)
print(even)

#Create a program that takes a list of strings and returns a new list with only the strings that have more than 5 characters.
def strings(strings):
    newlist=[]
    for string in strings:
        if len(string)>5:
            newlist.append(string)
    return newlist
list=["rita","alen","aliyah","trishia"]
newlist=strings(list)
print(newlist) 

#Write a function that takes a list of integers and returns 
# a new list with the squares of each number in the original list.
def multiplication(lists):
    multiply=[]
    for lis in lists:
        multiply.append(lis*lis)
    return multiply
lists=[2,4,6,8,10]
multiply=multiplication(lists)  
print(multiply)  

#Create a program that takes two lists and returns a new list that contains only the elements that are common to both lists.
def similar(list1,list2):
    common=[]
    for element in list1:
        if element in list2 and element not in common:
            common.append(element)
    return common
list1=[1,3,4,5,6]
list2=[7,8,3,6,4]
added=similar(list1,list2)
print(added) 

#Write a program that takes a list of numbers and returns a new list with the same numbers in reverse order.
def reversed(lists):
    
   
    return lists[::-1]#works byslicing the original list with a step of -1
lists=[1,2,3,4,5]
reversal=reversed(lists)
print(reversal)  

#Write a Python program to find the smallest number in a list.
def smallest(lists):
    small=lists[0]
    for l in lists:
        if l<small:
            small=l
    return small
lists=[74,3,4,2,3,1]
smallValue=smallest(lists)
print(smallValue) 

#Write a Python program to remove duplicates from a list.
def removeduplicate(lists):
    removed=[]
    for l in lists:
        if l not in removed:
            removed.append(l)
    return removed
lists=[3,3,4,4,5,5,6,6,7,7,8,8,9,9,7] 
removes=removeduplicate(lists)
print(removes)   

#Write a Python program to count the number of occurrences of an item in a list.
def counting(lists):


    return lists.count("riri")
lists=["rita","riri","ree","rit","ray","kimmy","riri","riri","riri","riri"]
newlists=counting(lists)
print(newlists)

#Create an empty list and append the numbers 1, 2, 3 to it.
empty=[]
empty.append(1)
empty.append(2)
empty.append(3)
print(empty)

#Given a list of numbers [1, 2, 3, 4, 5], create a new list with only the even numbers.
lists=[1,2,3,4,5]
z=[ ]
for l in lists:
    if l %2==0:
        z.append(l)
print(z)  

#Given two lists [1, 2, 3] and [4, 5, 6], concatenate them into a single list.
list1=[1,2,3]
list2=[4,5,6]
list3=list1+list2
print(list3)

#Given a list of strings ['cat', 'dog', 'bird'], sort the list in alphabetical order.
animals=['cat','dog','bird']
animals1=animals.sort()
print(animals)

#Given a list of numbers [1, 2, 3, 4, 5], reverse the order of the list.
number=[1,2,3,4,5]
number.reverse()
print(number)


#Given a list of numbers [1, 2, 3, 4, 5], find the sum of all the numbers in the list.
my_list=[1,2,3,4,5]
news=sum(my_list)

    
print(news)

#Given a list of numbers [1, 2, 3, 4, 5], find the largest number in the list.
lists=[1,2,3,4,5]
largest=lists[0]
for l in lists:
    if l >largest:
        largest=l
print(largest) 


#Given a list of strings ['cat', 'dog', 'bird'], create a new list with the length of each string.
lists=['cat','dog','bird','pig']
lengths=[]
for l in lists:
    lengths.append(len(l))
print(lengths)    

#Given a list of numbers [1, 2, 3, 4, 5], create a new list with each number squared.
lists=[1,2,3,4,5]
z=[l*l for l in lists]
print(z)

#Write a Python program to find the common elements between two lists.
def common_elements(list1,list2):
    common=[]
    for l in list1:
        if l in list2 :
            common.append(l)
    return common
list1=["rita","riri","ree","kimmy","ray"]
list2=["rita","riri","kim","ree","rita"]
newlist=common_elements(list1,list2)
print(newlist)

#Write a Python program to find the length of a list.
def list_length(lists):

    return(len(lists))
lists=["ree","rita","ray","kimmy","rakeem"]
lengths=list_length(lists)
print(lengths)


#Write a Python program to insert an element at a specific position in a list.
def inserting(lists):
    index=1
    word="ryan"
    lists.insert(index,"ryan")

    return lists
lists=["rita","ree","riri","roy"]
new=inserting(lists)
print(new)


#Write a Python program to count the number of occurrences of a specified element in a list.
def counting(lists):
   
   news=lists.count("rita")

   return news 


lists=["riri","ree","ryan","rita","rita"]
newlist=counting(lists)
print(newlist)

#Write a Python program to find the intersection of two lists
def intersection(list1,list2):
    comon=[]
    for x in list1:
        if x in list2:
            comon.append(x)
    return comon
list1=["ree","riri","roy","rita","ray"]
list2=["roy","ray","rakeem","kimmy"]
added=intersection(list1,list2)
print(added)
        










  



        

       
