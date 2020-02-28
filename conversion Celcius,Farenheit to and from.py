#Formula : c/5 = f-32/9 [ where c = temperature in Celsius and f = temperature in Fahrenheit ]

print("1. Convert from celcius to Farenheit");
print("2. Convert from Farenheit to celcius");
#takes value from user
choice= int(input("Enter choice (1/2): "))
if choice == 1:
    C=float(input("Enter the celsius value you want to convert to Farenheit:"))
    #calculation part for celcius to farenheit conversion
    CF= 9/5*C+32;
    print("%d^Celcius = %d^Farenheit"%(C,CF))
elif choice == 2:    
    F= float(input("Enter the farenheit value you to convert to celcius: "))
    #calculation part for farenheit to celcius conversion
    FC= 5/9*(F-32);
    print("%d^Farenheit = %d^Celcius"%(F,FC))
else:
    print("Choose the right value");
