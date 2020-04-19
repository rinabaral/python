"""1. Write a Python function that takes a sequence of numbers and determines
whether all the numbers are different from each other."""

def diff(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False;
print(diff([1,5,7,9]))
print(diff([2,4,5,5,7,9]))


"""2. Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once"""
from itertools import permutations
vowel = permutations(["a","e","i","o","u"])
for i in list(vowel):
  print(i)


"""3. Write a Python program to remove and print every third number from a list of numbers until the list becomes empty."""
def remove_nums(int_list):
  #list starts with 0 index
  position = 3 - 1 
  idx = 0
  len_list = (len(int_list))
  while len_list>0:
    idx = (position+idx)%len_list
    print(int_list.pop(idx))
    len_list -= 1
nums = [10,20,30,40,50,60,70,80,90]
remove_nums(nums)


"""4. Write a Python program to find unique triplets whose three elements gives the sum of zero from an array of n integers."""
def three_sum(nums):
  result = []
  nums.sort()
  for i in range(len(nums)-2):
    if i> 0 and nums[i] == nums[i-1]:
      continue
    l, r = i+1, len(nums)-1
    while l < r:
      s = nums[i] + nums[l] + nums[r]
      if s > 0:
        r -= 1
      elif s < 0:
          l += 1
      else:
        # found three sum
        result.append((nums[i], nums[l], nums[r]))
        # remove duplicates
        while l < r and nums[l] == nums[l+1]:
          l+=1
          while l < r and nums[r] == nums[r-1]:
            r -= 1
            l += 1
            r -= 1
          return result

x = [1, -6, 4, 2, -1, 2, 0, -2, 0 ]
print(three_sum(x))


"""5. Write a Python program to create the combinations of 3 digit combo"""
import random
numbers = range(10)
num = random.choice(numbers)
print(str(num)*3)


"""6. Write a Python program to print a long text, convert the string to a list
and print all the words and their frequencies."""

long_text= "I am very very bad at creating logics in programming"
l = long_text.split()
freq = [l.count(n) for n in l]
print("String: {} ".format(long_text))
print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(l,freq)))))


"""7. Write a Python program to count the number of each character of a given text of a text file. """
s="This is a dummy text to check the number of ecah characters present over here"

print(s)
d={}
for i in s:
  d[i]=s.count(i)
print(d)


"""8. Write a Python program to get the top stories from Google news. """
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
my_url = 'https://news.google.com/?hl=en-US&gl=US&ceid=US:en'




"""9. Write a Python program to get a list of locally installed Python modules."""
import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
for m in installed_packages_list:
    print(m)



"""10. Write a Python program to display some information about the OS where the script is running."""
import platform as pl

os_profile = [
        'architecture',
        'linux_distribution',
        'mac_ver',
        'machine',
        'node',
        'platform',
        'processor',
        'python_build',
        'python_compiler',
        'python_version',
        'release',
        'system',
        'uname',
        'version',
    ]
for key in os_profile:
  if hasattr(pl, key):
    print(key +  ": " + str(getattr(pl, key)()))


"""11. Write a Python program to check the sum of three elements (each from an
array) from three arrays is equal to a target value. Print all those
three-element combinations."""

X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
target = 70
list1=[]

for x in X:
  for y in Y:
    for z in Z:
      if x+y+z == target and (x,y,z) not in list1:
        list1.append((x,y,z))
        print(set(list1))

"""12. Write a Python program to create all possible permutations from a given collection of distinct numbers."""
import itertools
l =[1,2,3,4]

print(list(itertools.permutations(l)))


"""13. Write a Python program to get all possible two digit letter combinations
from a digit (1 to 9) string."""
def letter_combinations(digits):
    if digits == "":
        return []
    string_maps = {
        "1": "abc",
        "2": "def",
        "3": "ghi",
        "4": "jkl",
        "5": "mno",
        "6": "pqrs",
        "7": "tuv",
        "8": "wxy",
        "9": "z"
    }
    result = [""]
    for num in digits:
        temp = []
        for an in result:
            for char in string_maps[num]:
                temp.append(an + char)
        result = temp
    return result

digit_string = "47"
print(letter_combinations(digit_string))
digit_string = "29"
print(letter_combinations(digit_string))


"""14. Write a Python program to add two positive integers without using the '+' operator.
Note: Use bit wise operations to add two numbers."""



"""15. Write a Python program to check the priority of the four operators (+, -, *, /)."""
from collections import deque
import re

__operators__ = "+-/*"
__parenthesis__ = "()"
__priority__ = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1,
}

def test_higher_priority(operator1, operator2):
    return __priority__[operator1] >= __priority__[operator2]

print(test_higher_priority('*','-'))
print(test_higher_priority('+','-'))
print(test_higher_priority('+','*'))
print(test_higher_priority('+','/'))
print(test_higher_priority('*','/'))

"""16. Write a Python program to get the third side of right angled triangle
from two given sides. """

def pythagoras(oppo,adj,h):
        if oppo == str("x"):
            return ("Opposite = " + str(((h**2) - (adj**2))**0.5))
        elif adj == str("x"):
            return ("Adjacent = " + str(((h**2) - (oppo**2))**0.5))
        elif h == str("x"):
            return ("Hypotenuse = " + str(((oppo**2) + (adj**2))**0.5))
        else:
            return "You know the answer!"
    
print(pythagoras(3,4,'x'))
print(pythagoras(3,'x',5))
print(pythagoras('x',4,5))
print(pythagoras(3,4,5))


"""17. Write a Python program to get all strobogrammatic numbers that are of
length n.A strobogrammatic number is a number whose numeral is rotationally
symmetric, so that it appears the same when rotated 180 degrees. In other
words, the numeral looks the same right-side up and upside down
(e.g., 69, 96, 1001).
For example,
Given n = 2, return ["11", "69", "88", "96"].
Given n = 3, return ['818', '111', '916', '619', '808', '101', '906', '609', '888', '181', '986', '689']"""



"""18. Write a Python program to find the median among three given numbers. """
x = input("Input the first number: ")
y = input("Input the second number: ")
z = input("Input the third number: ")
print("Median of the above three numbers is: ")

if y < x and x < z:
    print(x)
elif z < x and x < y:
    print(x)  
elif z < y and y < x:
    print(y)
elif x < y and y < z:
    print(y)
elif y < z and z < x:
    print(z)    
elif x < z and z:
  print(z)


    

"""19. Write a Python program to find the value of n where n degrees of number 2 are written sequentially in a line without spaces."""

def ndegrees(num):
  ans = True
  n, pown, i = 2, 2, 2
  while ans:
    if str(pown) in num:
      i += 1
      pown = pow(n, i)
    else:
      ans = False
  return i-1;
print(ndegrees("2481632"))
print(ndegrees("248163264128"))


"""20. Write a Python program to find the number of zeros at the end of a factorial of a given positive number. Go to the editor
Range of the number(n): (1 = n = 2*109).
"""
def factendzero(n):
  x = n // 5
  y = x 
  while x > 0:
    x /= 5
    y += int(x)
  return y
       
print(factendzero(5))
print(factendzero(12))
print(factendzero(100))


"""21. Write a Python program to find the number of notes
(Sample of notes: 10, 20, 50, 100, 200 and 500 ) against a given amount.
Range - Number of notes(n) : n (1 = n = 1000000)."""

def no_notes(a):
  Q = [500, 200, 100, 50, 20, 10]
  x = 0
  for i in range(6):
    q = Q[i]
    x += int(a / q)
    a = int(a % q)
  if a > 0:
    x = -1
  return x
print(no_notes(880))
print(no_notes(1000))



"""22. Write a Python program to create a sequence where the first four members
of the sequence are equal to one, and each successive term of the sequence is
equal to the sum of the four previous ones. Find the Nth member of the sequence"""
def new_seq(n):
    if n==1 or n==2 or n==3 or n==4:
        return 1
    return new_seq(n-1) + new_seq(n-2) + new_seq(n-3) + new_seq(n-4)
print(new_seq(5))
print(new_seq(6))
print(new_seq(7))



"""23. Write a Python program that accept a positive number and subtract from
this number the sum of its digits and so on. Continues this operation until the
number is positive."""
def repeat_times(n):
  s = 0
  n_str = str(n)
  while (n > 0):
    n -= sum([int(i) for i in list(n_str)])
    n_str = list(str(n))
    s += 1
  return s
print(repeat_times(9))
print(repeat_times(21))


"""24. Write a Python program to find the number of divisors of a given integer is even or odd."""
def divisor(n):
  for i in range(n):
    x = len([i for i in range(1,n+1) if not n % i])
  return x
print(divisor(15))
print(divisor(12))
print(divisor(9))
print(divisor(6))
print(divisor(3))


"""25. Write a Python program to find the digits which are absent in a given mobile number."""

mobile = input('Please enter a mobile number: ' )
all = '0123456789'
print('missing digits are ', set(all) - set(mobile))


"""26. Write a Python program to compute the summation of the absolute difference
of all distinct pairs in an given array (non-decreasing order).
Sample array: [1, 2, 3]
Then all the distinct pairs will be:
1 2
1 3
2 3 """

def sum_distinct_pairs(arr):
    result = 0
    i = 0
    while i<len(arr):
        result+=i*arr[i]-(len(arr)-i-1)*arr[i]
        i+=1
    return result
print(sum_distinct_pairs([1,2,3]))
print(sum_distinct_pairs([1,4,5]))


"""28. Write a Python program to print the length of the series and the series
from the given 3rd term, 3rd last term and the sum of a series. 
Sample Data:
Input third term of the series: 3
Input 3rd last term: 3
Sum of the series: 15
Length of the series: 5
Series:
1 2 3 4 5 """

tn = int(input("Input third term of the series:"))
tltn = int(input("Input 3rd last term:"))
s_sum = int(input("Sum of the series:"))
n = int(2*s_sum/(tn+tltn))
print("Length of the series: ",n)


if n-5==0:
  d = (s_sum-3*tn)//6
else:
  d = (tltn-tn)/(n-5)

a = tn-2*d
j = 0
print("Series:")
for j in range(n-1):
  print(int(a),end=" ")
  a+=d
print(int(a),end=" ")


"""29. Write a Python program to find common divisors between two numbers in a given pair."""
def ngcd(x, y):
    i=1
    while(i<=x and i<=y):
        if(x%i==0 and y%i == 0):
            gcd=i;
        i+=1
    return gcd;
def num_comm_div(x, y):
  n = ngcd(x, y)
  result = 0
  z = int(n**0.5)
  i = 1
  while( i <= z ):
    if(n % i == 0):
      result += 2 
      if(i == n/i):
        result-=1
    i+=1
  return result

print("Number of common divisors: ",num_comm_div(2, 4))
print("Number of common divisors: ",num_comm_div(2, 8))
print("Number of common divisors: ",num_comm_div(12, 24))


"""30. Write a Python program to reverse the digits of a given number and add it
to the original, If the sum is not a palindrome repeat this procedure. 
Note: A palindrome is a word, number, or other sequence of characters which reads
the same backward as forward, such as madam or racecar."""

def rev_number(n):
  s = 0
  while True:
    k = str(n)
    if k == k[::-1]:
      break
    else:
      m = int(k[::-1])
      n += m
      s += 1
  return n 

print(rev_number(1234))
print(rev_number(1473))


"""31. Write a Python program to count the number of carry operations for each
of a set of addition problems.According to Wikipedia " In elementary arithmetic,
a carry is a digit that is transferred from one column of digits to another
column of more significant digits. It is part of the standard algorithm to add
numbers together by starting with the rightmost digits and working to the left.
For example, when 6 and 7 are added to make 13, the "3" is written to the same
column and the "1" is carried to the left"."""

def carry_number(x, y):
  ctr = 0
  if(x == 0 and y == 0):
    return 0
  z = 0  
  for i in reversed(range(10)):
      z = x%10 + y%10 + z
      if z > 9:
        z = 1
      else:
        z = 0
      ctr += z
      x //= 10
      y //= 10
      
  if ctr == 0:
    return "No carry operation."
  elif ctr == 1:
    return ctr
  else:
    return ctr
print(carry_number(786, 457))
print(carry_number(5, 6))

"""32. Write a python program to find heights of the top three building in
descending order from eight given buildings.
Input:
0 = height of building (integer) = 10,000
Input the heights of eight buildings:
25
35
15
16
30
45
37
39
Heights of the top three buildings:
45
39
37
"""
print("Input the heights of eight buildings:")
l = [int(input()) for i in range(8)]
print("Heights of the top three buildings:")
l = sorted(l)
print(*l[:4:-1], sep='\n')



"""33. Write a Python program to compute the digit number of sum of two given integers. Go to the editor
Input:
Each test case consists of two non-negative integers x and y which are separated by a space in a line.
0 = x, y = 1,000,000
Input two integers(a b):
5 7
Sum of two integers a and b.:
2 """
print("Input two integers(a b): ")
a,b = map(int,input().split(" "))
print("Number of digit of a and b.:")
print(len(str(a+b)))



"""34. Write a Python program to check whether three given lengths (integers) of
three sides form a right triangle. Print "Yes" if the given sides form a right
triangle otherwise print "No".
Input:
Integers separated by a single space.
1 = length of the side = 1,000
Input three integers(sides of a triangle)
8 6 7
No """

print("Input three integers(sides of a triangle)")
int_num = list(map(int,input().split()))
x,y,z = sorted(int_num)
if x**2+y**2==z**2:
    print('Yes')
else:
    print('No')

"""35. Write a Python program which solve the equation: Go to the editor
ax+by=c
dx+ey=f
Print the values of x, y where a, b, c, d, e and f are given.
Input:
a,b,c,d,e,f separated by a single space.
(-1,000 = a,b,c,d,e,f = 1,000)
Input the value of a, b, c, d, e, f:
5 8 6 7 9 4
Values of x and y:
-2.000 2.000 """

print("Input the value of a, b, c, d, e, f:")
a, b, c, d, e, f = map(float, input().split())
n = a*e - b*d
print("Values of x and y:")
if n != 0:
    x = (c*e - b*f) / n
    y = (a*f - c*d) / n
    print('{:.3f} {:.3f}'.format(x+0, y+0))


"""36. Write a Python program to compute the amount of the debt in n months.
The borrowing amount is $100,000 and the loan adds 5% interest of the debt and
rounds it to the nearest 1,000 above month by month. 
Input:
An integer n (0 = n = 100)
Input number of months:
7 Amount of debt: $144000
"""


"""37. Write a Python program which reads an integer n and find the number of
combinations of a,b,c and d (0 = a,b,c,d = 9) where (a + b + c + d) will be
equal to n.
Input:
n (1 = n = 50)
Input the number(n):
15
Number of combinations: 592 """

import itertools
n=int(input("Enter the number: "))
result=0
for (i,j,k) in itertools.product(range(10),range(10),range(10)):
    result+=(0<=n-(i+j+k)<=9)
print("Number of combinations:",result)


"""38. Write a Python program to print the number of prime numbers which are
less than or equal to a given integer.
Input:
n (1 = n = 999,999)
Input the number(n):
35
Number of prime numbers which are less than or equal to n.: 11"""

primes = [1] * 500000
primes[0] = 0
 
for i in range(3, 1000, 2):
    if primes[i // 2]:
        primes[(i * i) // 2::i] = [0] * len(primes[(i * i) // 2::i])
 
print("Input the number(n):")
n=int(input())
if n < 4:
    print("Number of prime numbers which are less than or equal to n.:",n - 1)
else:
    print("Number of prime numbers which are less than or equal to n.:",sum(primes[:(n + 1) // 2]) + 1)



"""39. Write a program to compute the radius and the central coordinate (x, y)
of a circle which is constructed by three given points on the plane surface.
Input:
x1, y1, x2, y2, x3, y3 separated by a single space.
Input three coordinate of the circle:
9 3 6 8 3 6
Radius of the said circle:
3.358
Central coordinate (x, y) of the circle:
6.071 4.643 """

print("Input three coordinate of the circle:")
x1, y1, x2, y2, x3, y3 = map(float, input().split())
c = (x1-x2)**2 + (y1-y2)**2
a = (x2-x3)**2 + (y2-y3)**2
b = (x3-x1)**2 + (y3-y1)**2
s = 2*(a*b + b*c + c*a) - (a*a + b*b + c*c) 
px = (a*(b+c-a)*x1 + b*(c+a-b)*x2 + c*(a+b-c)*x3) / s
py = (a*(b+c-a)*y1 + b*(c+a-b)*y2 + c*(a+b-c)*y3) / s 
ar = a**0.5
br = b**0.5
cr = c**0.5 
r = ar*br*cr / ((ar+br+cr)*(-ar+br+cr)*(ar-br+cr)*(ar+br-cr))**0.5
print("Radius of the said circle:")
print("{:>.3f}".format(r))
print("Central coordinate (x, y) of the circle:")
print("{:>.3f}".format(px),"{:>.3f}".format(py))


"""40. Write a Python program to check whether a point (x,y) is in a triangle or
not. There is a triangle formed by three points."""

print("Input x1,y1,x2,y2,x3,y3,xp,yp:")
x1,y1,x2,y2,x3,y3,xp,yp = map(float, input().split())
c1 = (x2-x1)*(yp-y1)-(y2-y1)*(xp-x1)
c2 = (x3-x2)*(yp-y2)-(y3-y2)*(xp-x2)
c3 = (x1-x3)*(yp-y3)-(y1-y3)*(xp-x3)
if (c1<0 and c2<0 and c3<0) or (c1>0 and c2>0 and c3>0):
    print("The point is in the triangle.")
else:
    print("The point is outside the triangle.")


"""41. Write a Python program to compute and print sum of two given integers
(more than or equal to zero). If given integers or the sum have more than 80
digits, print "overflow". 
Input first integer:
25
Input second integer:
22
Sum of the two integers: 47 """

x= int(input("Input first integer:"))
y = int(input("Input second integer:"))
if x >= 10 ** 80 or y >= 10 ** 80 or x + y >= 10 ** 80:
    print("Overflow!")  
else:
    print("Sum of the two integers: ",x + y)



"""42. Write a Python program that accepts six numbers as input and sorts them
in descending order.
Input:
Input consists of six numbers n1, n2, n3, n4, n5, n6 (-100000 = n1, n2, n3, n4, n5, n6 = 100000). The six numbers are separated by a space.
Input six integers:
15 30 25 14 35 40
After sorting the said integers:
40 35 30 25 15 14 """

print("Input six integers:")
nums = list(map(int, input().split()))
nums.sort()
nums.reverse()
print("After sorting the said ntegers:")
print(*nums)


"""43. Write a Python program to test whether two lines PQ and RS are parallel. The four points are P(x1, y1), Q(x2, y2), R(x3, y3), S(x4, y4). Go to the editor
Input:
x1,y1,x2,y2,x3,y3,xp,yp separated by a single space
Input x1,y1,x2,y2,x3,y3,xp,yp:
2 5 6 4 8 3 9 7
PQ and RS are not parallel """

print("Input x1,y1,x2,y2,x3,y3,xp,yp:")
x1, y1,x2, y2, x3, y3, x4, y4 = map(float, input().split())
print('PQ and RS are parallel.' if abs((x2 - x1)*(y4 - y3) - (x4 - x3)*(y2 - y1)) < 1e-10 else 'PQ and RS are not parallel')



"""44. Write a Python program to find the maximum sum of a contiguous
subsequence from a given sequence of numbers a1, a2, a3, ... an. A subsequence
of one element is also a continuous subsequence. Go to the editor
Input:
You can assume that 1 = n = 5000 and -100000 = ai = 100000.
Input numbers are separated by a space.
Input 0 to exit.
Input number of sequence of numbers you want to input (0 to exit):
3
Input numbers:
2
4
6
Maximum sum of the said contiguous subsequence:
12 Input number of sequence of numbers you want to input (0 to exit):
0 """

while True:
    print("Input number of sequence of numbers you want to input (0 to exit):")
    n = int(input())
    if n == 0:
        break
    else:
        A = []
        Sum = []
        print("Input numbers:") 
        for i in range(n):
            A.append(int(input()))
        Wa = 0
        for i in range(0,n):
            Wa += A[i]
            Sum.append(Wa)
        for i in range(0 , n):
            for j in range(0 , i):
                Num = Sum[i] - Sum[j]
                Sum.append(Num)
        print("Maximum sum of the said contiguous subsequence:")
        print(max(Sum))


"""45. There are two circles C1 with radius r1, central coordinate (x1, y1) and C2 with radius r2 and central coordinate (x2, y2). Go to the editor

Write a Python program to test the followings -

"C2 is in C1" if C2 is in C1
"C1 is in C2" if C1 is in C2
"Circumference of C1 and C2 intersect" if circumference of C1 and C2 intersect, and
"C1 and C2 do not overlap" if C1 and C2 do not overlap.
Input:
Input numbers (real numbers) are separated by a space.
Input x1, y1, r1, x2, y2, r2:
5 6 4 8 7 9
C1 is in C2 """

import math
print("Input x1, y1, r1, x2, y2, r2:")
x1,y1,r1,x2,y2,r2 = [float(i) for i in input().split()]
d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
if d < r1-r2:
    print("C2  is in C1")
elif d < r2-r1:
    print("C1  is in C2")
elif d > r1+r2:
    print("Circumference of C1  and C2  intersect")
else:
    print("C1 and C2  do not overlap")



"""46. Write a Python program to that reads a date (from 2016/1/1 to 2016/12/31)
and prints the day of the date. Jan. 1, 2016, is Friday. Note that 2016 is a leapyear. Go to the editor
Input:
Two integers m and d separated by a single space in a line, m ,d represent the
month and the day.
Input month and date (separated by a single space):
5 15
Name of the date: Sunday """

from datetime import date
print("Input month and date (separated by a single space):")
m, d = map(int, input().split())
weeks = {1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}
w = date.isoweekday(date(2016, m, d))
print("Name of the date: ",weeks[w])


"""47. Write a Python program which reads a text (only alphabetical characters
and spaces.) and prints two words. The first one is the word which is arise
most frequently in the text. The second one is the word which has the maximum
number of letters. Go to the editor
Note: A word is a sequence of letters which is separated by the spaces.

Input:
A text is given in a line with following condition:
a. The number of letters in the text is less than or equal to 1000.
b. The number of letters in a word is less than or equal to 32.
c. There is only one word which is arise most frequently in given text.
d. There is only one word which has the maximum number of letters in given text.
Input text: Thank you for your comment and your participation.
Output: your participation. """

import collections
print("Input a text in a line.")
text_list = list(map(str, input().split()))
sc = collections.Counter(text_list)
common_word = sc.most_common()[0][0]
max_char = ""
for s in text_list:
    if len(max_char) < len(s):
        max_char = s
print("\nMost frequent text and the word which has the maximum number of letters.")
print(common_word, max_char)


"""48. Write a Python program that reads n digits (given) chosen from 0 to 9 and
prints the number of combinations where the sum of the digits equals to another
given number (s). Do not use the same digits in a combination.
Input:
Two integers as number of combinations and their sum by a single space in a line.
Input 0 0 to exit.
Input number of combinations and sum, input 0 0 to exit:
5 6
2 4
0 0
2  """

import itertools
print("Input number of combinations and sum, input 0 0 to exit:")
while True:
  x, y = map(int, input(). split())
  if x == 0 and y == 0:
    break
  s = list(itertools.combinations(range(10), x))
  ctr = 0
  for i in s:
    if sum(i) == y:
            ctr += 1
 
print(ctr)


"""49. Write a Python program which reads the two adjoined sides and the diagonal of a parallelogram and check whether the parallelogram is a rectangle or a rhombus. Go to the editor
Input:
Two adjoined sides and the diagonal.
1 = ai, bi, ci = 1000, ai + bi > ci
Input two adjoined sides and the diagonal of a parallelogram (comma separated):
3,4,5
This is a rectangle. """

print("Input two adjoined sides and the diagonal of a parallelogram (comma separated):")
a,b,c = map(int, input().split(","))
if c**2 == a**2+b**2 :
    print("This is a rectangle.")
if a == b:
    print("This is a rhombus.")


"""50. Write a Python program to replace a string "Python" with "Java" and "Java"
with "Python" in a given string. Go to the editor
Input:
English letters (including single byte alphanumeric characters, blanks, symbols)
are given on one line. The length of the input character string is 1000 or less.
Input a text with two words 'Python' and 'Java'
Python is popular than Java
Java is popular than Python"""

txt = 'Python is more popular than Java'
txt = txt.split()

py_index = txt.index('Python')
ja_index = txt.index('Java')

txt[py_index] = 'Java'
txt[ja_index] = 'Python'

print(' '.join(txt))






































































































