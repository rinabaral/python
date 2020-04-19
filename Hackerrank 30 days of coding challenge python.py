"""Day 0: Hello World! """
input_string = input()
print('Hello, World.')
print(input_string)


"""Day 1: Data Types """
i = 4
d = 4.0
s = 'HackerRank '
a = int(input())
b = float(input())
c = input()
print((i+a),(d+b),(s+c), sep = "\n")


"""Day 2:Operators """
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * tip_percent/100
    tax = meal_cost * tax_percent/100
    print(round(meal_cost+tip+tax))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)

"""Day 3: Intro to conditional statements """
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    if (N%2==0) and (N in range(2,5) or (N>20)):
        print("Not Weird")
    elif (N%2==0) and N in range(6,20):
       print("Weird")
    else:
        print("Weird")

"""Day 4: Class Vs. Instance """
class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        # Increment the age of the person in here

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")


    
"""Day 5: Loops """
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    for i in range(1,11):
        print("%d x %d = %d"%(n,i,n*i))



"""Day 6: Let's Review """

for i in range(int(input())):
    S = input()
    print(S[::2],S[1::2])


"""Day 7:Arrays """
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))



"""Day 8: Dictionaries and Maps"""
import sys

#To get number of entries in a dictionary
n = int(input())
phoneBook = {}
for i in range(n):
    contact = input().split(' ')
    phoneBook[contact[0]] = contact[1]

# Process Queries
lines = sys.stdin.readlines()
for i in lines:
    name = i.strip()
    if name in phoneBook:
        print(name + '=' + str( phoneBook[name] ))
    else:
        print('Not found')


"""Day 9: Recusrsion 3"""
import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    factorial = 1
    if n>1:
        for i in range(1,n+1):
            factorial = i * factorial
    return factorial  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()






