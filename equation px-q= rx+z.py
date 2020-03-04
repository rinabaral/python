import sympy as sym
print("To solve equation px-q = rx+z ")
p= int(input("Enter the value of p ="))
q= int(input("Enter the value of q ="))
r= int(input("Enter the value of r ="))
z= int(input("Enter the value of z ="))

x = sym.symbols('x')
eq1 = sym.Eq(p*x-q*x-z-q)
sol = sym.solve(eq1)
print("The value of x is :",sol)


