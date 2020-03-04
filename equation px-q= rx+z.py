print("To solve equation px-q = rx+z ")
p= int(input("Enter the value of p ="))
q= int(input("Enter the value of q ="))
r= int(input("Enter the value of r ="))
z= int(input("Enter the value of z ="))
if (p-r) == 0:
    print("The value is infinite")
else:
    x=(q+z)/(p-r)
    print("The value of x is: ",x)
