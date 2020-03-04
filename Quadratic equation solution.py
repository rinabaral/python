#It contains the solution of quadratic equation

import math
print("To solve quadratic equation ax^2+bx+c = 0")
a= int(input("Enter the value of a ="))
b= int(input("Enter the value of b ="))
c= int(input("Enter the value of c ="))

d = b**2-4*a*c
if d < 0:
    print("This equation has no real solution")
elif d == 0:
    x = (-b+math.sqrt(b**2-4*a*c))/2*a
    print("This equation has one solution: ", x)
else:
    x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
    x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
    print("This equation has two solutions: ", x1, " and", x2)



