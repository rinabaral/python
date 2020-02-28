"""1: Print the following pattern
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 """

for i in range(1,6): #for row in range
    for j in range(1,i+1): #for column in range of (1,row+1)
        print(j, end = " ")
    print()    

"""2: Accept n number from user and calculate the sum of
all number between 1 and n including n. """

n= int(input("Enter a range:"))
sum= 0
for i in range(1,n+1,1):
    sum = sum + i
print(sum)

"""Question 3: Given a list iterate it and display numbers which are divisible
by 5 and if you find number greater than 120 stop the loop iteration"""

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for i in list1:
    if(i > 120):
        break;
    if i%5==0:
        print(i)

"""Question 4: Display a message “Done” after successful execution of for loop"""
n=int(input("Enter the number of range:"))
for i in range(n):
    print(i)
else:
    print("Done!")


"""Question 5: Print the following pattern using for loop
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1     """

x=5
y=5
for i in range(0,x+1):
    for j in range(y-i,0,-1):
        print(j,end =' ')
    print()    

"""Question 6: Display -10 to -1 using for loop"""
for i in range(-10,0):
    print(i)
 
