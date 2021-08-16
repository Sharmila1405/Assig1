

str1="hello This is Sharmila"
print(str1.capitalize()) #starting letter will be capitalized
print(str1.casefold()) # turns all characters to lower case
print(str1.center(20))  #make the string to come in middle
print(str1.center(20, "O"))
print(str1.index("i")) #returns the index
print(str1.isalnum()) #true if string is alphanumeric
print(str1.isalpha())# true if all characters in sting are alphabets
print(str1.isdecimal())#returns True if all the characters are decimals (0-9).
print(str1.isdigit()) #returns True if all the characters are digits, otherwise False.

print(str1.isidentifier())#method returns True if the string is a valid identifier, otherwise False.
"""
A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid 
identifier cannot start with a number, or contain any spaces."""


print(str1.islower())#method returns True if all the characters are in lower case, otherwise False.
print(str1.isnumeric())#Returns True if all characters in the string are numeric
print(str1.isprintable()) # method returns True if all the characters are printable, otherwise False.
tx="  "
print(tx.isspace()) #method returns True if all the characters in a string are whitespaces, otherwise False.
print(str1.istitle()) #method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
print(str1.isupper())    #method returns True if all the characters are in upper case, otherwise False.

print("$".join(str1))  #method takes all items in an iterable and joins them into one string.
myDict = {"name": "sharmi", "country": "India"}
Separator = "TE"

x = Separator.join(myDict)

print(x)  #return  values are keys not values
print(str1.ljust(20, "O"))  #method will left align the string, using a specified character (space is default) as the fill character.
print( str1.ljust(25),"is a student")
print(str1.lower())#method returns a string where all characters are lower case.Symbols and Numbers are ignored.







str2="Eat apple everyday,apple keeps doctor away"
print(str2.count("apple"))  #counts no. of times a specified value occurs in string
print(str2.count("apple", 10, 24))
print(str2.encode()) #encodes the string default UTF-8 is used
print(str2.endswith("apple"))  # returns true if string ends with specified value
print(str2.find("apple")) #first occurance of specified value
print(str2.find("e", 5, 10))

str3="S\ha\tj\sh"
print(str3)
print(str3.expandtabs())
print(str3.expandtabs(2))
print(str3.expandtabs(4))
print(str3.expandtabs(10))

txt1 = "My name is {fname}, I'm {age}".format(fname = "sai", age = 36)
txt2 = "My name is {0}, I'm {1}".format("sai",36)
txt3 = "My name is {}, I'm {}".format("sai",36)
print(txt1)
print(txt2)
print(txt3)







"""list methods"""

l1=["sai","india",1,2,3]
l1.append(4)
print(l1)#Adds an element at the end of the list

x = l1.copy()
print(x)
#copy() method returns a copy of the specified list.


x = l1.count("india")
print(x)

fruits=["apple","banana","cherry"]
l1.extend(fruits)
print(l1)

print(fruits.index("cherry"))

x=fruits.insert(0,"mango")
print(fruits)

fruits.pop(1)
print(fruits)

fruits.remove("banana")
print(fruits)

l1.reverse()
print(l1)

fruits.sort()
print(fruits)

l1.clear() #Removes all the elements from the list
print(l1)
