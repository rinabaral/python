"""Question 1: Accept two numbers from the user and calculate multiplication"""
#defining a method with parameters
def multiply(x,y):
    return x*y
x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
print(multiply(x,y)) #printing valuse by calling multiply method


"""2: Display “My Name is James” as “My**Name**is**James”
using print() output formatting"""

str="My Name is James"
print('My','Name','is','James',sep='**')


"""Question 3: Convert decimal number to octal using print()
output formatting"""

n = int(input("enter a decimal number:"))
print("%o,"%n) #%o represents octal value

"""Question 4: Display float number with 2 decimal places using print()"""

num= float(input("Enter an float with more than two decimal places:"))
print("%.2f"%num)

"""Question 5: Accept list of 5 float numbers as a input from user"""
#initializing a blank list
list1=[]
n=int(input("Enter the number of items int the list:"))
for i in range(0,n):
    j= float(input())
    list1.append(j)
print(list1)

"""Question 6: Accept any three string from one input() call"""
str1,str2,str3 = input("enter any three strings").split()
print(str1,str2,str3)

