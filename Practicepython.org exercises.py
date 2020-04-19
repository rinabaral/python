
""Create a program that asks the user to enter their name and their age. Print out
a message addressed to them that tells them the year that they will turn 100
years old.
Extras:Add on to the previous program by asking the user for another number and
printing out that many copies of the previous message. (Hint: order of operation
s exists in Python)
Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)"""

Name= input("Enter your name:")
Age = int(input("Enter your age:"))
Age1= 100-Age
current_year = 2020
print("In the year %d you will turn 100 years old"%(current_year+Age1))
n= int(input("Enter the number of lines you want to print:"))
for i in range(n):
    print("In the year %d you will turn 100 years old"%(current_year+Age1))
    print()
    i=i+1


"""Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. Hint: how does an even / odd
number react differently when divided by 2?
Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number
to divide by (check). If check divides evenly into num, tell that to the user.
If not, print a different appropriate message."""

num = int(input("Enter a number"))
if num%2 == 0:
    print("The provided number is an even number")
elif num%4 == 0:
    print("The provided number is a multiple of 4")
else:
    print("The provided number is an odd number")


check = int(input("Enter a number to divide by:"))            
if num%check == 0:
    print("%d is evenly divided by %d"%(num,check))
else:
    print("%d is not evenly divided by %d"%(num,check))


"""Take a list, say for example this one:
and write a program that prints out all the elements of the list that are less
than 5.
Extras:
Instead of printing the elements one by one, make a new list that has all the
elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from
the original list a that are smaller than that number given by the user."""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]
c=[]
for i in a:
    if i<=5:
        b.append(i)
print(b)
n= int(input("Enter a number that you want list items less than:"))
for j in a:
    if j<=n:
        c.append(j)
print(b)

"""Create a program that asks the user for a number and then prints out a list
of all the divisors of that number. (If you don’t know what a divisor is, it is
a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)"""

num = int(input("Enter a number:"))
a=[]
for i in range(1,num+1):
    if num%i == 0:
        a.append(i)
print(a)   

"""Take two lists and write a program that returns a list that contains only the
elements that are common between the lists (without duplicates). Make sure your
program works on two lists of different sizes.
Extras:
Randomly generate two lists to test this
Write this in one line of Python """

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
x= []
for i in a:
    if i in b and i not in x:
        x.append(i)
print(x)

"""Ask the user for a string and print out whether this string is a palindrome
or not. (A palindrome is a string that reads the same forwards and backwards.)"""
        
Str = input("Enter a string:")

if Str[:]==Str[::-1]:
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")

"""Let’s say I give you a list saved in a variable:
Write one line of Python that takes this list a and makes a new list that has
only the even elements of this list in it"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b=[]
for i in a:
    if i%2 == 0:
        b.append(i)
print(b)        
# b = [i for i in a if i % 2 == 0] one line code for the above

"""Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays
(using input), compare them, print out a message of congratulations to the
winner, and ask if the players want to start a new game)

Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock"""

while True:
    print("Type the rock, scissors or paper you want")
    player1 = input("Player 1: ")
    player2 = input("Player 2: ")
    if player1==player2:
        print("draw")
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif (player1 == "rock" and player2 == "scissors") or(player1 =="scissors" and player2 =="paper") or (player1 =="paper" and player2 =="rock") :
        print("Player 1 wins")
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif (player1 == "rock" and player2 == "paper") or(player1 =="scissors" and player2 =="rock") or (player1 =="paper" and player2 =="scissors") :
        print("player 2 wins")
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    else:
        print("Enter the correct value")


"""Generate a random number between 1 and 9 (including 1 and 9). Ask the user
to guess the number, then tell them whether they guessed too low, too high, or
exactly right. (Hint: remember to use the user input lessons from the very
first exercise)
Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends,
print this out."""

import random

number = random.randint(1,9)
guess = 0
count = 0


while guess != number and guess != "exit":
    guess = input("What's your guess?")
    
    if guess == "exit":
        break
    
    guess = int(guess)
    count += 1
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You got it!")
        print("And it only took you",count,"tries!")


"""write a program that returns a list that contains only the elements that are
common between the lists (without duplicates). Make sure your program works on
two lists of different sizes. Write this using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).
Extra:
Randomly generate two lists to test this"""

a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
c=[i for i in a if i in b]

print(c)


"""Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.)
Take this opportunity to practice using functions, described below."""

num =int(input("Enter a number to check:"))

for i in range(2,num):
    if num%i == 0:
        print("The number is not a prime number")
        break;
    else:
        print("The number is a prime number")\



"""Write a program that takes a list of numbers and makes a new list of only the
first and last elements of the given list. For practice, write this code inside
a function."""

def list_element(sample_list):
    return [sample_list[0], sample_list[-1]]
print(list_element([5, 10, 15, 20, 25]))


"""Write a program that asks the user how many Fibonnaci numbers to generate and
then generates them. Take this opportunity to think about how you can use
functions. Make sure to ask the user to enter the number of numbers in the
sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers
where the next number in the sequence is the sum of the previous two numbers
in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)"""

def Fibonnaci():
    num = int(input("How many fibonacci numbers would you like to generate? "))
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1

    return fib
print(Fibbonnaci())

"""Write a program (function!) that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.
Extras:
Write two different functions to do this - one using a loop and constructing a
list, and another using sets."""

#two methods
#1st method 
def new_list(x):
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return y

#2nd method uses sets
def remove_dup(x):
    return list(set(x))

a = [1,2,3,4,3,2,1]
print(a)
print(new_list(a))
print(remove_dup(a))


"""Write a program (using functions!) that asks the user for a long string
containing multiple words. Print back to the user the same string, except with
the words in backwards order. For example, say I type the string:
for ex:
"I am a sentence" outout is "sentence a am I"."""

multi_string =input("Enter multiple string character")
a= multi_string.split()
print(a[::-1])


"""Use the BeautifulSoup and requests Python packages to print out a list of
all the article titles on the New York Times homepage."""
                   
import requests
from bs4 import BeautifulSoup
 
Url = 'http://www.nytimes.com'
r = requests.get(Url)
soup = BeautifulSoup(r.text)
 
for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())        
         


















