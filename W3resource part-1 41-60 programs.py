"""41. Write a Python program to check whether a file exists."""

import os.path
open('abc.txt', 'w')
print(os.path.isfile('abc.txt'))

"""42. Write a Python program to determine if a Python shell is executing in
32bit or 64bit mode on OS"""

# For 32 bit it will return 32 and for 64 bit it will return 64
import struct
print(struct.calcsize("P") * 8)

"""43. Write a Python program to get OS name, platform and release information."""
import platform
import os
print("OS name:",os.name, "\n Platform:", platform.system(),"\n Release:", platform.release())


"""44. Write a Python program to locate Python site-packages."""
import site; 
print(site.getsitepackages())

"""45. Write a python program to call an external command in Python."""
from subprocess import call
call(["ls", "-l"])


"""46. Write a python program to get the path and name of the file that is
currently executing"""

import os.path
print("Current File Name : ",os.path.realpath(__file__))

"""47. Write a Python program to find out the number of CPUs using."""
import multiprocessing
print(multiprocessing.cpu_count())

"""48. Write a Python program to parse a string to Float or Integer."""
n = "222.33"
print(float(n))
print(int(float(n)))


"""49. Write a Python program to list all files in a directory in Python. """

import os
print(os.listdir('C:\Python'))

"""50. Write a Python program to print without newline or space."""
for i in range(0, 10):
    print('*', end="")
print("\n")


"""51. Write a Python program to determine profiling of Python programs.
Note: A profile is a set of statistics that describes how often and for how long
various parts of the program executed.
These statistics can be formatted into reports via the pstats module."""

import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')


"""52. Write a Python program to print to stderr. """

from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

eprint("abc", "efg", "xyz", sep="--")


"""53. Write a python program to access environment variables."""
import os
# Access all environment variables 
print('*----------------------------------*')
print(os.environ)
print('*----------------------------------*')
# Access a particular environment variable 
print(os.environ['HOME'])
print('*----------------------------------*')
print(os.environ['PATH'])
print('*----------------------------------*')


"""54. Write a Python program to get the current username."""
import getpass
print(getpass.getuser())

"""55. Write a Python to find local IP addresses using Python's stdlib"""
import socket
print(socket.gethostbyname(socket.gethostname()))

"""56. Write a Python program to get height and width of the console window."""
import shutil
wh = shutil.get_terminal_size()
print("terminal size is %d x %d" % wh)

"""57. Write a program to get execution time for a Python method."""
import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time
n = 5
print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))


"""58. Write a python program to find the sum of the first n positive integers"""
def sum_integers(n):
    sum =0 
    for i in range(n+1):
        sum= sum+i
    return sum
n= int(input("Enter the no. of integers:"))
print(sum_integers(n))


"""59. Write a Python program to convert height (in feet and inches) to centimeters."""
foot =float(input("Enter your height in feet:"))
inch = float(input("Enter inches:"))
f= foot*30.48
i = 2.45
print("Your height in cm is :", round(f+i))

"""60. Write a Python program to calculate the hypotenuse of a right angled triangle."""
from math import sqrt
print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))

c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is", c )

