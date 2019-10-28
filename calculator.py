#scientific calculator
from sympy import*
def add(a,b):
      return(a+b)
def subs(a,b):
        return(a-b)
def multi(a,b):
        return(a*b)
def div(a,b):
        return(a/2)
def mod(a,b):
        return(a%b)
def pow(a,b):
    return(a**b)
x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
print("\n")
print("Action which can be performed by this calculator:-")
print(" 1-Addition \n 2-Substraction \n 3-Division \n 4-Multiplication \n 5-Modulus \n 6-Power \n")
k=int(input("Enter the action which you wish to perform"))
if(k==1):
    print("Addition of number is:",add(x,y))
if(k==2):
    print("Substraction of number is:",subs(x,y))
if(k==3):
    print("Division of number is:",div(x,y))
if(k==4):
    print("Multiplication of number is:",multi(x,y))
if(k==5):
    print("Modulus of number is:",mod(x,y))
if(k==6):
    print("Power of number is:",pow(x,y))
