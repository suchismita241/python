Number = int(input("\nPlease Enter the Range Number: "))

i = 0
First_Value = 0
Second_Value = 1

while(i < Number):
           if(i <= 1):
                      Next = i
           else:
                      Next = First_Value + Second_Value
                      First_Value = Second_Value
                      Second_Value = Next
           print(Next)
           i = i + 1

import math

def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x
 

def isFibonacci(n):
 
    
    
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
    
lower = int(input("enter lower range: "))
upper = int(input("enter upper range: "))
for num in range(lower,upper + 1):
     if (isFibonacci(num) == True):
         print (num,"is a Fibonacci Number")
     else:
         print (num,"is not a Fibonacci Number")
         
           


