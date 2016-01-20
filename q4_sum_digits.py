#summation of digits
x= False
while not x:
    try: 
        n=int(input("Enter a number between 0 and 1000 here:"))

        if 0<n<1000:

            a=n%10
            b=(n//10)%10
            c=n//100

            d=a+b+c

            print("The digits in {0} adds up to {1}.".format(n,d))

            x=True

        else:
            print("You have entered an invalid number. Please try again.")

    except ValueError:
        print("Please enter an integer!")
