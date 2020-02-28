#getting input in list and concatenation

#initializing two empty lists
x=[]
y=[]
#to get number of elements in first list
xinput=int(input("Enter the number elements for first list:"))

for i in range(0,xinput):
    #taking elements input for the list
    j= int(input())
    #append the empty list to the input inserted
    x.append(j)
    
#repeat the process for the second list    
yinput=int(input("Enter the number of elements for second list:"))    
for i in range(0,yinput):
    j=int(input())
    y.append(j)
print(x+y)
    


