""" 1. write a python program to find those numbers which are divisible by 7 and
multiple of 5,between 1500 and 2700(both included)"""

for i in range(1500,2701):
    if i%7==0 or i%5==0:
        print(i)
        i=i+1


"""2. Write a Python program to guess a number between 1 to 9. 
 Note: User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit. 
"""

#defining the range to get the guessed number
for i in range(1,10):
    i= int(input("Please guess a number between 1 to 9:"))
    if i== 7:
        print("WOW! Well Guessed")
        break;
    i=i+1


'''3. Write a Python program to construct the following pattern, using a nested for loop.'''

#defining range for rows
for i in range(1,6):
#defining range for columns
    for j in range(1,i+1):
        print("*", end="")
    print()
for i in range(4,0,-1):
    for i in range(0,i):
        print("*", end="")
    print()    


'''4. Write a Python program that accepts a word from the user and reverse it.'''

#::]slices the string and [::-1] is used to reverse or slice from backwards
word = str(input("Enter a word :"))[::-1]
print(word)


'''5. Write a Python program to count the number of even and odd numbers from a series of numbers. 
 Sample numbers: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4 
'''

numbers=(1,2,3,4,5,6,7,8,9)
#defining variable to assign result
even = 0
odd = 0
for i in numbers:
    if i%2 == 0:
       even = even+1
    else:
        odd = odd+1
print("Number of even numbers :", even)
print("Number of even numbers :", odd)


'''6. Write a Python program that prints each item and its corresponding type from the following list.
Sample List : datalist = [1452, 11.23, 1+2j, True, 'Hawkeye', (0, -1), [5, 12], {"class":'V', "section":'A'}] '''

datalist = [1452, 11.23, 1+2j, True, 'Hawkeye', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for sample in datalist:
    print(sample,type(sample))


"""7. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note: Use 'continue' statement.
Expected Output: 0 1 2 4 5 
"""

for i in range(0,7):
    if i == 3 or i==6:
        continue
    print(i)
  
"""8. Write a Python program to get the Fibonacci series between 0 to 50
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34 
"""

#initialize the value of a and b
a,b=0,1
while b<50:
    print(b)
    #increasing the value of a and b as
    a,b= b,a+b   


"""9. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
Sample Output:
fizzbuzz
1
2
fizz
4
buzz 
"""

for i in range(1,51):
    if i%5 == 0 and i%3 == 0:
        print("FizzBuzz")
        continue
    elif i%3==0:
        print("Fizz")
    elif i%5== 0:
         print("Buzz")
         continue
    print(i)

"""10. Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. 
 Note :
i = 0,1.., m-1
j = 0,1, n-1.
Test Data: Rows = 3, Columns = 4
Expected Result: [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]] 
"""
i= int(input("enter the number of rows:"))
j= int(input("enter the number of columns:"))
k= [[0 for col in range(j)]for row in range(i)]

for row in range(i):
    for col in range(j):
        k[row][col]= row*col
    print(k)

"""11. Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case)."""    
  
lines = []
while True:
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break;
for l in lines:
    print(l)

