"""101. Write a Python program to access and print a URL's content to the console."""
import urllib.request

url = urllib.request.urlopen("http://www.google.com")
data = url.read()
print(data)


"""103. Write a Python program to extract the filename from a given path."""
import os
print(os.path.basename('/Python/Python38/example.py'))


"""104. Write a Python program to get the effective group id, effective user id,
real group id, a list of supplemental group ids associated with the current
process. 
Note: Availability: Unix."""

import os
print("\nEffective group id: ",os.getegid())
print("Effective user id: ",os.geteuid())
print("Real group id: ",os.getgid())
print("List of supplemental group ids: ",os.getgroups())
print()


"""105. Write a Python program to get the users environment."""

import os
print(os.environ)


"""106. Write a Python program to divide a path on the extension separator. """
import os.path
for path in [ 'test.txt', 'filename', '/user/system/test.txt', '/', '' ]:
    print('"%s" :' % path, os.path.splitext(path))
	

"""107. Write a Python program to retrieve file properties."""
import os.path
import time

print('File         :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))


"""108. Write a Python program to find path refers to a file or directory when
you encounter a path name."""
import os.path

for file in [os.path.dirname('/Python')]:
    print('File        :', file)
    print('Absolute    :', os.path.isabs(file))
    print('Is File?    :', os.path.isfile(file))
    print('Is Dir?     :', os.path.isdir(file))
    print('Is Link?    :', os.path.islink(file))
    print('Exists?     :', os.path.exists(file))
    print('Link Exists?:', os.path.lexists(file))


"""109. Write a Python program to check if a number is positive, negative or zero."""
num = float(input("Input a number: "))
if num > 0:
   print("It is positive number")
elif num == 0:
   print("It is Zero")
else:
   print("It is a negative number")


"""110. Write a Python program to get numbers divisible by fifteen from a
list using an anonymous function."""

num_list = [35,30,40,45]
# using anonymous function to filter
result = list(filter(lambda x: (x % 15 == 0), num_list))
print("Numbers divisible by 15 are",result)


"""111. Write a Python program to make file lists from current directory using a wildcard."""
import glob
file_list = glob.glob('*.*')
print(file_list)


"""112. Write a Python program to remove the first item from a specified list."""
list1= [1,2,3,4]
print("\n Original List: ",list1)
del list1[0]
print("After removing the first element: ",list1)
print()

"""113. Write a Python program to input a number, if it is not a number generate an error message."""
while True:
    try:
        a = int(input("Input a number: "))
        break
    except ValueError:
        print("\nThis is not a number. Try again...")
        print()

"""114. Write a Python program to filter the positive numbers from a list."""

num_list = [35,30,40,-45]
result = list(filter(lambda x: (x > 0), num_list))
print("Numbers divisible by 15 are",result)


"""115. Write a Python program to compute the product of a list of integers (without using for loop)."""
from functools import reduce
nums = [10, 20, 30,]
nums_product = reduce( (lambda x, y: x * y), nums)
print("Product of the numbers : ",nums_product)


"""116. Write a Python program to print Unicode characters."""
#u converts the unicode into alphabets
str = u'\u0050\u0079\u0074\u0068\u006f\u006e \u0045\u0078\u0065\u0072\u0063\u0069\u0073\u0065\u0073 \u002d \u0077\u0033\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065'
print()
print(str)
print()


"""117. Write a Python program to prove that two string variables of same value
point same memory location"""

str1 = "Python"
str2 = "Python"
 
print("\nMemory location of str1 =", hex(id(str1)))
print("Memory location of str2 =", hex(id(str2)))
print()


"""118. Write a Python program to create a bytearray from a list."""
nums = [10, 20, 56, 35, 17, 99]
# Create bytearray from list of integers.
values = bytearray(nums)
for x in values: print(x)


"""119. Write a Python program to display a floating number in specified numbers."""
float_num = 212.374
print('\nThe total order amount comes to %f' % float_num)
print('The total order amount comes to %.2f' % float_num)
print()


"""120. Write a Python program to format a specified string to limit the number of characters to 6."""
str_num = "1234567890"
print('%.6s' % str_num)


"""121. Write a Python program to determine whether variable is defined or not."""
try:
  x = 1
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")
try:
  y
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")


"""122. Write a Python program to empty a variable without destroying it.
Sample data: n=20
d = {"x":200}
Expected Output : 0
{}  """

n = 20
d = {"x":200}
l = [1,3,5]
t= (5,7,8)
print(type(n)())
print(type(d)())
print(type(l)())
print(type(t)()) 


"""123. Write a Python program to determine the largest and smallest integers, longs, floats. """
import sys
print("Float value information: ",sys.float_info)
print("\nInteger value information: ",sys.int_info)
print("\nMaximum size of an integer: ",sys.maxsize)


"""124. Write a Python program to check whether multiple variables have the same value. """
x,y,z= 20,20,20
if x == y == z == 20:
    print("All variables have same value!")


"""125. Write a Python program to sum of all counts in a collections"""
import collections
num = [2,2,4,6,6,8,6,10,4]
print(sum(collections.Counter(num).values()))


"""126. Write a Python program to get the actual module object for a given object."""
from inspect import getmodule
from math import sqrt
print(getmodule(sqrt))


"""127. Write a Python program to check whether an integer fits in 64 bits. """
int_val = 30
if int_val.bit_length() <= 63:
    print((-2 ** 63).bit_length())
    print((2 ** 63).bit_length())


"""128. Write a Python program to check whether lowercase letters exist in a string."""
str1 = 'A8238i823acdeOUEI'
print(any(c.islower() for c in str1))


"""129. Write a Python program to add leading zeroes to a string."""
































