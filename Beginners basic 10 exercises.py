"""Question 1: Accept two int values from the user and return their product.
If the product is greater than 1000, then return their sum"""
#defining a multiplication method
def multiply(x,y):
    product = x*y
    if (product <1000): #to match the requirement of value> 1000
        return product
    else:
        return x+y
#taking input from user
x= int(input("Enter first number:"))
y= int(input("Enter second number:"))

result = multiply(x,y)
print(result)


"""Question 2: Given a range of numbers. Iterate from o^th number to the end number and
print the sum of the current number and previous number
"""
#getting number range
n= int(input("Enter the value up to which you want to print: "))
j=0 #initializing value
for i in range(n):
    sum = i+j;
    print(sum)
    j=i
    i=i+1

"""Question 3: Accept string from the user and display only those
characters which are present at an even index"""

#input from user
sample =input("Enter a word you want: ")
print("Original string:",sample)
print("Printing only even index characters")
for i in range(0,len(sample),2):
    print("index[",i,"]", sample[i])
        
 
"""Question 4: Given a string and an int n, remove characters from a string
starting from zero up to n and return a new string"""    

def remove_from(str, n):
  return str[n:]

print("Removing n number of charcters")
print(remove_from(input("Enter the string:"),
                  int(input("enter the number of index you want to remove:"))))

"""Question 5: Given a list of ints, return True if first
and last number of a list is same"""

l = [10, 20, 30, 40, 10]
if l[0] == l[-1]: #l[0] is first element and l[-1] is last element
   print("True")
else:
    print("False")


"""Question 6: Given a list of numbers,
Iterate it and print only those numbers which are divisible of 5"""

#initializing empty list
list1=[]
n = int(input("Enter the number of elements for the list:"))
for i in range(0,n):
    j= int(input())
    list1.append(j) #adds the value of j to list1

for k in list1:
    if (k%5 == 0):
        print(k)
    k= k+1


"""Question 7: Return the number of times that the string “Emma”
appears anywhere in the given string """

str ="Emma is a talent girl. Emma loves coding."
i= str.count("Emma") #counts the number of occurence of substring Emma
print("Emma occured",i, "times in above string")


"""Question 8: Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 """

#for rows
for i in range(1,6):
    for j in range(i): #for columns
        print(i,end =" ") #prints the number
    print() #for next line after every iteration

"""Question 9: Reverse a given number and return true
if it is the same as the original number """

#defining a method
def reverseCheck(num):
  originalNum = num
  reverseNum=0
  while(num > 0):
    reminder = num % 10
    reverseNum  = (reverseNum *10) + reminder
    num = num // 10 #gives the nearest whole number
  if(originalNum  == reverseNum):
    return True
  else:
    return False
    
print(" To check orignal and reverse number is equal")
print(reverseCheck(int(input("Enter a number you want to check:"))))


"""Question 10: Given a two list of ints create a third list such that should contain
only odd numbers from the first list and even numbers from the second list"""

def new_list(list1, list2):
    thirdList = []
    for num in list1:
        if(num % 2 != 0):
            thirdList.append(num)
    for num in list2:
        if(num % 2 == 0):
            thirdList.append(num)
    return thirdList
    
print("Merged List is")
list1 = [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]

print(new_list(list1, list2))    
    

