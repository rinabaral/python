"""51. Write a Python program to find the difference between the largest integer and the smallest integer which are created by 8 numbers from 0 to 9. The number that can be rearranged shall start with 0 as in 00135668. Go to the editor
Input:
Input an integer created by 8 numbers from 0 to 9.:
2345
Difference between the largest and the smallest integer from the given integer:
3087 """
print("Input an integer created by 8 numbers from 0 to 9.:")
num = list(input())
print("Difference between the largest and the smallest integer from the given integer:")
print(int("".join(sorted(num,reverse=True))) - int("".join(sorted(num))))


"""52. Write a Python program to compute the sum of first n given prime numbers. Go to the editor
Input:
n ( n = 10000). Input 0 to exit the program.
Input a number (n=10000) to compute the sum:(0 to exit)
25
Sum of first 25 prime numbers:
1060 """

MAX = 105000
print("Input a number (n≤10000) to compute the sum:(0 to exit)") 
is_prime = [True for _ in range(MAX)]
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX ** (1 / 2)) + 1):
  if is_prime[i]:
    for j in range(i ** 2, MAX, i):
      is_prime[j] = False 
primes = [i for i in range(MAX) if is_prime[i]] 
while True:
  n = int(input())
  if not n:
    break
  print("Sum of first",n,"prime numbers:")
  print(sum(primes[:n]))


"""53. Write a Python program that accept an even number (>=4, Goldbach number) from the user and create a combinations that express the given number as a sum of two prime numbers. Print the number of combinations. Go to the editor
Goldbach number: A Goldbach number is a positive even integer that can be expressed as the sum of two odd primes.[4] Since four is the only even number greater than two that requires the even prime 2 in order to be written as the sum of two primes, another form of the statement of Goldbach's conjecture is that all even integers greater than 4 are Goldbach numbers.
The expression of a given even number as a sum of two primes is called a Goldbach partition of that number. The following are examples of Goldbach partitions for some even numbers:
6 = 3 + 3
8 = 3 + 5
10 = 3 + 7 = 5 + 5
12 = 7 + 5
...
100 = 3 + 97 = 11 + 89 = 17 + 83 = 29 + 71 = 41 + 59 = 47 + 53
Input an even number (0 to exit):
100
Number of combinations:
6"""
import sys
from bisect import bisect_right
from itertools import chain, compress
print("Input an even number (0 to exit):") 
ub = 50000
is_prime = [0, 0, 1, 1] + [0]*(ub-3)
is_prime[5::6] = is_prime[7::6] = [1]*int(ub/6)
primes = [2, 3]
append = primes.append
 
for n in chain(range(5, ub, 6), range(7, ub, 6)):
    if is_prime[n]:
        append(n)
        is_prime[n*3::n*2] = [0]*((ub-n)//(n*2))
primes.sort()

for n in map(int, sys.stdin):
    if not n:
        break
    if n%2:
        print("Number of combinations:")  
        print(is_prime[n-2])
    else:
        print("Number of combinations:")  
        print(len([1 for p in primes[:bisect_right(primes, n/2)] if is_prime[n-p]]))


"""54. if you draw a straight line on a plane, the plane is divided into two regions. For example, if you pull two straight lines in parallel, you get three areas, and if you draw vertically one to the other you get 4 areas.
Write a Python program to create maximum number of regions obtained by drawing n given straight lines. Go to the editor
Input:
(1 = n = 10,000)
Input number of straight lines (o to exit):
5
Number of regions:
16 """
def maxRegions(n): 
    num = n * (n + 1) // 2 + 1
    return num
n = 10  
print(maxRegions(n)) 
















