##Write a program q5_upper_to_lower.py that converts an uppercase letter from 
##standard input to a lowercase letter by making use of its ASCII value.



x=True
while x:
    a=input("Hello! Please enter a letter in upper case:")
    av=ord(a)
    y=chr(ord(a)+ 32) 
    if len(a)!=1 or av>90 or av<65:
        print("Invalid character. Please try again!")
        a
        
    else:
        print("The letter is converted to letter", y)
        x=False
    
