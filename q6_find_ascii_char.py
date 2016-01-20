##Write a program q6_find_ascii_char.py that receives
##an ASCII code (an integer between 0 and 127)
##and displays its character.


x=True
while x:
    try:
        a=int(input("Please enter an integer between 0 and 127:"))
        c=chr(a)
        if 0<a<127:
            print("Your char is:",c)
            x=False

        else:
            print("This integer is not between 0 and 127!")

    except ValueError:
            print("This is not an integer! Please try again.")
