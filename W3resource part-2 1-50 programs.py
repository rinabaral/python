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


"""21. Write a Python program to find the number of notes (Sample of notes: 10, 20, 50, 100, 200 and 500 ) against a given amount. Go to the editor
Range - Number of notes(n) : n (1 = n = 1000000)."""























