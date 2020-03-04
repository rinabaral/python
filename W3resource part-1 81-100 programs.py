"""81. Write a Python program to concatenate N strings."""
string= ["Hello", "I am", "No one"]
concat = " ".join(string)
print(concat)

"""82. Write a Python program to calculate the sum over a container."""
container =[40,20,30]
print("The sum of container is :",sum(container))


"""83. Write a Python program to test whether all numbers of a list is greater than a certain number."""
n= int(input("Enter a number to check:"))
list1 = [40,50,70]
print(all(i > n for i in list1))


"""84. Write a Python program to count the number occurrence of a specific character in a string. """
a = str(input("Enter the string: "))
b=str(input("Enter a character to count: "))
print(a.count(b))


"""85. Write a Python program to check whether a file path is a file or a directory."""
import os  
path = "abc.txt"
if os.path.isdir(path):
    print("\n It is a directory")
elif os.path.isfile(path):
    print("\n It is a file")
else:
    print("Cannot be recognized")



"""86. Write a Python program to get the ASCII value of a character"""
#ord prints the ascii value of a character
print(ord('A'))

"""87. Write a Python program to get the size of a file."""
import os
file = ("practice file.py")
print("\nThe size of "+file+" is :",os.path.getsize(file),"Bytes")


"""88. Given variables x=30 and y=20, write a Python program to print t "30+20=50"."""
x= 30
y=20
print("%i + %i= %i"%(x,y,x+y))


"""89. Write a Python program to perform an action if a condition is true.
Given a variable name, if the value is 1, display the string "First day of a
Month!" and do nothing if the value is not equal."""

a= int(input("Enter a number:"))
if a == 1:
    print("\nFirst day of a month")
print()


"""90. Write a Python program to create a copy of its own source code."""
with open(file="practice file.py", mode="r") as f:
    print(f.readlines())


"""91. Write a Python program to swap two variables."""
x = 30
y = 20
print("\nBefore swap x = %d and y = %d" %(x, y))
x, y = y, x
print("\nAfter swaping a = %d and b = %d" %(x, y))
print()


"""92. Write a Python program to define a string containing special characters in various forms."""
print()
print("\#{'}${\"}@/")
print("\#{'}${"'"'"}@/")
print(r"""\#{'}${"}@/""")
print('\#{\'}${"}@/')
print('\#{'"'"'}${"}@/')
print(r'''\#{'}${"}@/''')
print()


"""93. Write a Python program to get the identity of an object."""
object1 = 1
print(id(object1))


"""94. Write a Python program to convert a byte string to a list of integers."""
a= b 'Hello'
print(list(a))


"""95. Write a Python program to check whether a string is numeric. """
string = input("Enter a word or numbers: ")
if string.isdecimal():
    print("Yes it is Numeric.")  
else:
    print("It is not numeric.")


"""96. Write a Python program to print the current call stack."""
import traceback
print()
def f1():return abc()
def abc():traceback.print_stack()
f1()
print()


"""97. Write a Python program to list the special variables used within the language"""
s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
print()
print( '\n'.join(' '.join(s_var_names[i:i+8]) for i in range(0, len(s_var_names), 8)) )
print()


"""98. Write a Python program to get the system time.
Note : The system time is important for debugging, network information, random
number seeds, or something as simple as program performance."""

import time
print(time.ctime())


"""99. Write a Python program to clear the screen or terminal."""
import os
import time
# for windows
# os.system('cls')
os.system("ls")
time.sleep(2)


"""100. Write a Python program to get the name of the host on which the routine is running. """
import socket
print(socket.gethostname())






























