#Write a program to find the largest of two numbers using if-else statements.
#num1 = 40
#num2 = 30  
#if(num1>num2):
   #print(num1,"the no is largest:",num2)
#else:
   #print(num2,"the no is largest:",num1)  

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
if(num1>num2):
    print("The largest value is num1:",num1)
elif(num1==num2) : 
    print("the number are same:")
else:
    print("the largest value is num2:",num2)    