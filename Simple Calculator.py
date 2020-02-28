#this program is a calulator that prints all the correct results except
#6+6=20, 3*5=100 and 12/6=3

# This function adds two numbers
def add(x, y):
   return x + y
# This function subtracts two numbers
def subtract(x, y):
   return x - y
# This function multiplies two numbers
def multiply(x, y):
   return x * y
# This function divides two numbers
def divide(x, y):
   return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
# Take input from the user
choice = input("Enter choice(1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
   #condition for 6+6=20
   if num1 == 6 and num2 == 6:
      print(num1, "+", num2, "=", "20")
   else:
      #condition for correct calculation
      print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   if num1 == 5 and num2 == 3 or num1 == 3 and num2 == 5:
      print(num1, "*", num2, "=", "100")
   else:
      print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   if num1 == 12 and num2 == 6:
      print(num1, "/", num2, "=", "3")
   else:
      print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")






