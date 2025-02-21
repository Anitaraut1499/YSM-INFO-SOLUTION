#Write a program that prints the grade based on the score input using if-else statements (A for 90-100, B for 80-89, etc.).
sub1=61
sub2=62
sub3=74
sub4=65
sub5=40
n=(sub1+sub2+sub3+sub4+sub5)/5
if(n>=90):
 print("Grade: A")
elif(n>=80 and n<89):
 print("Grade: B")
elif(n>=70 and n<79):
 print("Grade: C")
elif(n>=60 and n<69):
 print("Grade: D")
else:
 print("Grade: E") 


sub01=int(input("Enetr the marks : "))
sub02=int(input("Enetr the marks : "))
sub03=int(input("Enetr the marks : "))
sub04=int(input("Enetr the marks : "))
sub05=int(input("Enetr the marks : "))
n=(sub01+sub02+sub03+sub04+sub05)/5
if(n>=90):
 print("Grade: A")
elif(n>=80 and n<89):
 print("Grade: B")
elif(n>=70 and n<79):
 print("Grade: C")
elif(n>=60 and n<69):
 print("Grade: D")
else:
 print("Grade: E")