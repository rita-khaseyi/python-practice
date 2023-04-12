          #STRING INDEXING
#Given the string "Hello, world!", how would you access the first character?
string="hello world"
print(string[0])
#Given the string "Hello, world!", how would you access the last character?
string1="Hello world"
print(string1[-1])
#Given the string "Hello, world!", how would you access the characters from index 2 to index 5?
string2="Hello world"
print(string2[2:5])
#Given the string "Hello, world!", how would you access the characters from index 7 to the end of the string?
string="Hello world"
print(string[7:])
#Given the string "Hello, world!", how would you access every second character?
string="Hello world"
print(string[::2])
#Given the string "hello", what is the substring starting at index 1 and ending at index 3?
string="hello"
print(string[1:3])
#Given the string "hello", what is the substring starting at index 2 and ending at the end of the string?
string="hello"
print(string[2:])
#Given the string "hello", what is the substring starting at index -3 and ending at index -1?
strings="hello"
print(strings[-3:-1])
#Given the string "Hello, world!", what is the substring starting at index 7 and ending at index 11
string="Hello world!"
print(string[7:11])
#Given the string "Hello, world!", what is the substring starting at index -6 and ending at index -1?
string="Hello world!"
print(string[-6:-1])
        #STRING METHODS
#Given the string "hello", what is the length of the string?
string="hello"
print(len(string))

#Given the string "Hello, world!", how can you replace the letter "o" with the letter "e" in the string?
string="hello world"
rep=string.replace("o","e")
print(rep)
#Given the string "Hello, world!", how can you check if the string starts with the substring "Hello"?
string="Hello world!"
print(string.startswith("Hello")) 
#  Given the string "Hello, world!", how can you check if the string ends with the substring "world!"?
string="Hello world!"
print(string.endswith("world!"))  
#Given the string "Hello, world!", how can you find the index of the first occurrence of the letter "o" in the string?
string="Hello world!"
word=string.index("o")
print(word)   
#Given the string "Hello, world!", how can you count the number of times the letter "o" appears in the string?
word="Hello world!"
words=word.count("o")
print(words)
#Given the string "Hello, world!", how can you split the string into a list of words?
string="Hello world!"
word=string.split()
print(word)
#Given the string "hello", how can you reverse the order of the characters in the string?
sting="Hello"
strs=sting[::-1] #this slice the original string starting from the end and moving backwards through the string with a step of -1
print(strs)
#Given the string "Hello, world!", how would you convert it to uppercase?
string="hello world"
print(string.upper())
#Given the string "Hello, world!", how would you split it into a list of words?
string="Hello world"
print(string.split())
#Given the string "Hello, world!", how would you replace the word "world" with "Python"?
string="Hello world!"
word=string.replace("world","python")
print(word)
#Given the string "Hello, world!", how would you check if it contains the substring "world"?
string="Hello world!"
star=string.find("world")
print(star)
#Given the string "Hello, world!", how would you check if it ends with the string "!"?
string="Hello world!"
ends=string.endswith("!")
print(ends)
#Given the string " hello ", how can you remove the leading and trailing whitespace characters from the string?
string="   hello   "
print(string.strip())
#Given the string "hello", how can you check if all the characters in the string are letters?
string="Hello"
print(string.isalpha())
#Given the string "hello", how can you check if all the characters in the string are lowercase?
string="hello"
print(string.islower())
    #STRING FORMATTING
 
#Given the variables name and age, how can you format a string to print "My name is John and I am 30 years old."?
age=30
name="John"
string=f"My name is {name} and i am {age} years old"
print(string)
#Given the variables num1, num2, and result, how can you format a string to print "The result of adding 5 and 10 is 15."?
num1=5
num2=10
result=num1+num2
string=f"The result of adding {num1} to {num2} is {result}"
print(string)
#Given the variable pi, how can you format a string to print "The value of pi is 3.14159."?
pi = 3.14159
ans=f"The value of pi is {pi}"
print(ans)
#Given the variables item and price, how can you format a string to print "The price of a banana is $0.99."?
item="Banana"
price=0.99
output=f"The price of a {item} is ${price:.2f}"#:.2f syntax is used inside the curly braces {} to format the price value as a float with two decimal place
print(output)
#Given the variables first_name, last_name, and city, how can you format a string to print
#  "My name is John Smith and I live in New York City."?
first_name="John"
last_name="Smith"
city="New York"
sentence=f"My name is {first_name} {last_name} and I live in {city}"
print(sentence)
#Given the variables num1, num2, and result, how can you format a string to print 
# "The result of dividing 10 by 3 is 3.33." with a precision of 2 decimal places?
num1=10
num2=3
result=10/3
solution=f"The result of dividing {num1} by {num2} is {result:.2f}"
print(solution)
#Given the variable num, how can you format a string to print 
# "The number is 5." with a minimum field width of 10 characters?
num=5
wording=f"The number is {num:>{10}}" #Here, the > character is used to right-align the string
#and the 10 specifies the minimum field width of the string to be 10 
print(wording)
#Given the variable num, how can you format a string to print "The number is 5.00." with a precision of 2 decimal places?
num=5.00
value=f"The number is {num:.2f}"
print(value)
#Given the variable sentence, how can you format a string to print "The quick brown fox jumped over the lazy dog." 
# with the first letter of each word capitalized?
sentence="The quick brown fox jumped over the lazy dog"
sen=sentence.title()
print(sen)
#Given the variables price = 49.99 and discount = 0.15, 
# how can you format a string to say "The price after a 15% discount is $42.49"?
price=49.99
discount=0.15
newprice=price-(price*discount)
total=f"The price after a 15% discount is {newprice:.2f} "
print(total)
#Given the variables num1 = 10 and num2 = 5, how can you format a string to say "10 divided by 5 is 2"?
num1=10
num2=5
result=num1//num2
response=f"{num1} divide by {num2} is {result}"
print(response)
#Given the variables first_name = "John" and last_name = "Doe", how can you format a string to say "Doe, John"?
first_name = "John"
last_name = "Doe"
print(f"{last_name} {first_name}")



