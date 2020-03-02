"""21. Write a Python program to find whether a given number (accept from the
user) is even or odd, print out an appropriate message to the user. """

num = int(input("Enter the number you want to check: "))
if num%2 ==0:
    print("The given number is an even number")
else:
    print("The given number is an odd number")


"""22. Write a Python program to count the number 4 in a given list."""
def list(n):
    count = 0
    for i in n:
        if i == 4:
            count = count+1
    return count
n =[0,1,2,3,4,4,5]
print("The number of 4 in the given list is :",list(n))


"""23. Write a Python program to get the n (non-negative integer) copies of the
first 2 characters of a given string. Return the n copies of the whole string
if the length is less than 2."""

Str = input("Enter the string:")
n = int(input("Enter the  number of copies you want to print: "))
if len(Str)<2:
    print(n*Str)
else:
    print(n*Str[:2])


"""24. Write a Python program to test whether a passed letter is a vowel or not."""

def vowel(x):
    vowels = 'aeiou'
    return x in vowels
x= input("Enter a letter to check:")
print(vowel(x))

"""25. Write a Python program to check whether a specified value is contained in
a group of values. 
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False"""

def is_contained(n,x):
    return x in n
print(is_contained([1, 5, 8, 3],3))
print(is_contained([1, 5, 8, 3],-1))


"""26. Write a Python program to create a histogram from a given list of integers"""
def histogram( items ):
    for n in items:
        output = ''
        times = n
        while(times>0):
            output += '@'
            times = times - 1
        print(output)
histogram([2,6,9])          


"""27. Write a Python program to concatenate all elements in a list into a string and return it. """
def concatenate(list):
    result = ''
    for n in list:
        result = result + str(n)
    return result

print(concatenate([1,2,3,4,5]))
     

"""28. Write a Python program to print all even numbers from a given numbers list
in the same order and stop the printing if any numbers that come after 237 in
the sequence.
Sample numbers list :"""
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

result =[]

for n in numbers:
    if n == 237:
        print(n)
        break;
    elif n % 2 == 0:
        print(n)


"""29. Write a Python program to print out a set containing all the colors from
color_list_1 which are not present in color_list_2. 
Expected Output :
{'Black', 'White'}"""

x = set(["White", "Black", "Red"])
y = set(["Red", "Green"])
result=[]
for i in x:
    if i not in y:
        result.append(i)
print(result) 


"""30. Write a Python program that will accept the base and height of a triangle
and compute the area."""

base = float(input("Enter the base of a triangle:"))
height = float(input("Enter the height of a triangle:"))
area = 1/2*base*height
print("area =",area)

or
def area(b,h):
    area = 1/2*b*h
    return area
b = float(input("Enter the base of a triangle:"))
h = float(input("Enter the height of a triangle:"))
print("area =",area(b,h))


"""31. Write a Python program to compute the greatest common divisor (GCD) of
two positive integers"""

def g_common(x, y):
    result = 1
    if x % y == 0:
        return y
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            result = k
            break  
    return result
x= int(input("Enter first number:"))
y= int(input("Enter second number:"))
print(g_common(x, y))


"""32. Write a Python program to get the least common multiple (LCM) of two positive integers"""

def LCM(a,b):
    if a > b:
        x= a
    else:
        x=b
    while(True):
        if(x%a == 0) and (x%b ==0):
            lcm = x
            break
        x  +=1
     return lcm   
a= int(input("Enter first number:"))
b= int(input("Enter second number:"))
print(LCM(a,b))


"""33. Write a Python program to sum of three given integers. However, if two
values are equal sum will be zero."""

def sum(a,b,c):
    if (a==b) or (b==c) or (c==a):
        sum = 0
    else:
        sum = a+b+c
    return sum
a= int(input("Enter first number:"))
b= int(input("Enter second number:"))
c= int(input("Enter third number:"))
print(sum(a,b,c))


"""34. Write a Python program to sum of two given integers. However, if the sum
is between 15 to 20 it will return 20."""

def sum(a,b):
    sum = a+b
    if sum in range(15,21):
        sum = 20
    else:
         sum = sum
    return sum
print(sum(9,9))
print(sum(9,5))


"""35. Write a Python program that will return true if the two given integer
values are equal or their sum or difference is 5."""
def sum(a,b):
    s = a+b
    d = abs(a-b)
    if (a==b) or (d ==5) or (s==5):
        return True
    else:
        return False
print(sum(2,4))
print(sum(2,3))


"""36. Write a Python program to add two objects if both objects are an integer type."""

def add_int(a, b):
    if type(a) == int and type(b) == int:
        return (a + b)
    else:
        return "The both numbers are not integers"
print(add_int(4,2))
print(add_int("hello",1))
print(add_int(3, 4.4))


"""37. Write a Python program to display your details like name, age, address
in three different lines."""

def my_details():
    name, age = "Rina", 23
    address = "Kathmandu, Nepal"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))
my_details()


"""38. Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49"""

a,b = 4,3
result = a**2 +  2*a*b + b**2
print("({} + {}) ^ 2) = {}".format(a, b, result))
    

"""39. Write a Python program to compute the future value of a specified
principal amount, rate of interest, and a number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79"""

amt = 10000
int = 3.5
years = 7

future_value  = amt*((1+(0.01*int)) ** years)
print(round(future_value,2))

"""40. Write a Python program to compute the distance between the points
(x1, y1) and (x2, y2). """

import math
p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

print(distance)





        







        























