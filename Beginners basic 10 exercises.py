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


"""Given a range of numbers. Iterate from o^th number to the end number and
print the sum of the current number and previous number
"""
n= int(input("Enter the value up to which you want to print: "))
j=0
for i in range(n):
    sum = i+j;
    print(sum)
    j=i
    i=i+1

"""Question 3: Accept string from the user and display only those
characters which are present at an even index"""

sample =input("Enter a word you want: ")
print("Original string:",sample)
print("Printing only even index chars")
for i in range(0,len(sample),2):
    print("index[",i,"]", sample[i])
        
 
"""Question 4: Given a string and an int n, remove characters from a string
starting from zero up to n and return a new string"""    

def remove_from(str, n):
  return str[n:]

print("Removing n number of chars")
print(remove_from(input("Enter the string:"),
                  int(input("enter the number of index you want to remove:"))))

"""Question 5: Given a list of ints, return True if first
and last number of a list is same"""

l = [10, 20, 30, 40, 10]
if l[0] == l[-1]:
   print("True")
else:
    print("False")


         

