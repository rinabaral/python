"""61. Write a Python program to convert the distance (in feet) to inches, yards, and miles."""
ft = int(input("Input distance in feet: "))
inches = ft * 12
yards = ft / 3.0
miles = ft / 5280.0

print("The distance in inches is %i inches." % inches)
print("The distance in yards is %.2f yards." % yards)
print("The distance in miles is %.2f miles." % miles)


"""62. Write a Python program to convert all units of time into seconds."""
days = int(input("Input days: ")) * 3600 * 24
hours = int(input("Input hours: ")) * 3600
minutes = int(input("Input minutes: ")) * 60
seconds = int(input("Input seconds: "))
time = days + hours + minutes + seconds
print("The  amounts of seconds", time)


"""63. Write a Python program to get an absolute file path."""
import os
print(os.path.abspath('path_fname'))


"""64. Write a Python program to get file creation and modification date/times."""
import os.path, time
print("Last Modified : %s" %time.ctime(os.path.getmtime("abc.txt")))
#define path for abc.txt if it is not found
print("Created at: %s" %time.ctime(os.path.getctime("abc.txt")))


"""65. Write a Python program to convert seconds to day, hour, minutes and seconds."""
time = float(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("days:hr:min:sec-> %d:%d:%d:%d" % (day, hour, minutes, seconds))

"""66.Write a python program to convert body mass index."""
height =float(input("Enter height in meters:"))
weight = float(input("Enter your weight in kg:"))
BMI = round(weight/(height**2),2)
print(BMI)

"""67. Write a Python program to convert pressure in kilopascals to pounds per
square inch, a millimeter of mercury (mmHg) and atmosphere pressure."""

kpa = float(input("Input pressure in in kilopascals> "))
psi = kpa / 6.89475729
mmhg = kpa * 760 / 101.325
atm = kpa / 101.325
print("The pressure in pounds per square inch: %.2f psi"  % (psi))
print("The pressure in millimeter of mercury: %.2f mmHg" % (mmhg))
print("Atmosphere pressure: %.2f atm." % (atm))


"""68. Write a Python program to calculate the sum of the digits in an integer. """
num = int(input("Input a four digit numbers: "))
x = num //1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10
print("The sum of digits in the number is", x+x1+x2+x3)


"""69. Write a Python program to sort three integers without using conditional statements and loops."""
x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))

a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z) - a- c
print("Numbers in sorted order: ", a, b, c)


"""70. Write a Python program to sort files by date."""
import os
import glob
files = glob.glob(".py")
files.sort(key= os.path.getmtime)
print("\n".join(files))


"""71. Write a Python program to get a directory listing, sorted by creation date."""
import os
import time

print('\n'.join(["%s %s" % (time.ctime(t),f) for t,f in
sorted([(os.path.getctime(x),x) for x in os.listdir(".")])]))

"""72. Write a Python program to get the details of math module."""
import math
print(dir(math))


"""73. Write a Python program to calculate midpoints of a line."""
x1=float(input("Enter the value of x of first line:"))
y1=float(input("Enter the value of y of first line:"))
x2=float(input("Enter the value of x of second line:"))
y2=float(input("Enter the value of y of second line:"))
xm = (x1+x2)/2
ym = (y1+y2)/2
print("The midpoints of a given line are: (%.2f, %.2f)"%(xm,ym))


"""74. Write a Python program to hash a word."""
soundex=[0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]
 
word=input("Input the word be hashed: ")
 
word=word.upper()
 
coded=word[0]
 
for a in word[1:len(word)]:
    i=65-ord(a)
    coded=coded+str(soundex[i])
print() 
print("The coded word is: "+coded)
print()



"""75. Write a Python program to get the copyright information. """

import sys
print("\nPython Copyright Information")
print(sys.copyright)
print()


"""76. Write a Python program to get the command-line arguments (name of the
script, the number of arguments, arguments) passed to a script."""

import sys
print("This is the name/path of the script:"),sys.argv[0]
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))


"""77. Write a Python program to test whether the system is a big-endian platform or little-endian platform. """
import sys
print()
if sys.byteorder == "little":
    #intel, alpha
    print("Little-endian platform.")
else:
    #motorola, sparc
    print("Big-endian platform.")
print()


"""78. Write a Python program to find the available built-in modules."""
import sys
print(sys.builtin_module_names)


"""79. Write a Python program to get the size of an object in bytes."""
import sys
Str = input("Enter a string:")
print("The memory size of "+ Str+" is:"+str(sys.getsizeof(Str))+ "bytes")


"""80. Write a Python program to get the current value of the recursion limit."""
import sys
print()
print("Current value of the recursion limit:")
print(sys.getrecursionlimit())
print()

