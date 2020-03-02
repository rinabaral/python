#This file contains the questions and solutions of first 20 programs given in https://www.w3resource.com/python-exercises/python-basic-exercises.php 

"""1. Write a Python program to print the following string in a specific format (see the
output).
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :
Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are"""

#\n prints the line in next line \t prints the tab equals space
print("Twinkle, twinkle, little star, \n\t How I wonder what you are! \n\t\t Up above the worls so high, \n\t\t Like a diamond in the sky. \n Twinkle, twinkle, little star, \n\t How I wonder what you are")


"""2. Write a Python program to get the Python version you are using."""       
import sys
print("Python Version: ",sys.version, "\n Version info: ", sys.version_info)

"""3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14"""

import datetime

current = datetime.datetime.now()
print("Current date and time: ")
print(current.strftime("%Y-%m-%d %H:%M:%S"))


"""4. Write a Python program which accepts the radius of a circle from the user and
compute the area.
Sample Output :
r = 1.1
Area = 3.8013271108436504"""

radius= float(input("Enter the radius of a circle:"))
Area = 22/7*radius**2
print("Radius =",radius)
print("Area = ",Area)

"""5. Write a Python program which accepts the user's first and last name and print them
in reverse order with a space between them"""

fname = input("Enter your first name:")
lname = input("Enter your last name:")
print(lname,"", fname)

"""6. Write a Python program which accepts a sequence of comma-separated numbers from
user and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')"""


num = input("Enter some comma separated numbers: ")
a = num.split(",")
print("Lict: ",a)
print("Tuple: ",tuple(a))

"""7. Write a Python program to accept a filename from the user and print the extension
of that.
Sample filename : abc.java
Output : java"""

filename = input("Enter your file name:")
a= filename.split(".")
print("The extension of this file is :",a[-1])

"""8. Write a Python program to display the first and last colors from the following list.""" Go to the editor
color_list = ["Red","Green","White" ,"Black"]
print("The first colour of the list is :",color_list[0],"\n The last colour of the list is :",color_list[-1]) 


"""9. Write a Python program to display the examination schedule.
(extract the date from exam_st_date).
Sample Output : The examination will start from : 11 / 12 / 2014"""
exam_st_date = (11, 12, 2014)
print("The examination will start from : %i / %i / %i"%exam_st_date)

"""10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615"""

num = int(input("Input an integer : "))
n1 = int( "%s" % num )
n2 = int( "%s%s" % (num,num) )
n3 = int( "%s%s%s" % (num,num,num) )
print ("The output is:",n1+n2+n3)

"""11. Write a Python program to print the documents (syntax, description etc.) of Python
built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument."""

print(abs.__doc__)

"""12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module."""

import calendar

year = int(input("Enter the year:"))
month = int(input("Enter the month:"))
print(calendar.month(year,month))

"""13. Write a Python program to print the following here document.
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example"""

print("""a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example""")


"""14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days"""

import datetime

from datetime import date
fdate = date(2014, 7, 2)
ldate = date(2014, 7, 11)
result = ldate - fdate
print(result.days)

"""15. Write a Python program to get the volume of a sphere with radius 6."""

r = float(input("Enter the radius:"))
pi = 22/7
print("The volume of a sphere with radius "+str(r)+" is :", 4/3*pi*r**3)

"""16. Write a Python program to get the difference between a given number and 17, if the
number is greater than 17 return double the absolute difference."""

def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2 
n=int(input("Enter a number:"))
print(difference(n))


"""17. Write a Python program to test whether a number is within 100 of 1000 or 2000."""
#abs() function returns the absolute value of a number
def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

n = int(input("Enter a number:"))    
print(near_thousand(n))

"""18. Write a Python program to calculate the sum of three given numbers, if the values
are equal then return three times of their sum"""

def sum_of(a,b,c):
    sum= a+b+c;
    if a==b==c:
        sum =sum*3
    return sum    
a=int(input("Enter first value:"))
b=int(input("Enter second value:"))
c=int(input("Enter third value:"))
print(sum_of(a,b,c))


"""19. Write a Python program to get a new string from a given string where "Is" has been
added to the front. If the given string already begins with "Is" then return the string
unchanged."""

Str =input("Enter a string : ")
if len(Str)>=2 and Str[:2] == "Is":
    print(Str)
else:
    print("Is" , Str)

"""20. Write a Python program to get a string which is n (non-negative integer) copies of a given string"""

n= int(input("Enter the number of copies you want to print: "))
Str = input("Enter the string value:") 
print(Str * n)

#using function
def print_str(str, n):
    result = ""
    for i in range(n):
        result = result + str
    return result

n= int(input("Enter the number of copies you want to print: "))
str = input("Enter the string value:")
print(print_str(str,n))






