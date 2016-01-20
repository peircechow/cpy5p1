#q3_miles_to_kilometre
##x=True
##while x:
##    
##    miles=float(input("Enter distance in miles here:"))
##    km=miles*1.60934
##    if km>=0:
##        print("{0} miles is equals to {1:.3f} km.".format(miles,km))
##    else:
##        print("Invalid value. Please enter a non-negative number.")

#    miles=input("Enter distance in miles here:")
##
##    if type(miles)==int:
##        km=int(miles)*1.60934
##        print("{0} miles is equals to {1:.3f} km.".format(miles,km))
##    else:
##        print("Invalid value. Please enter a non-negative number.")

##miles=input("Enter miles here:")
##
##if type(miles)==int or type(miles)==float:
##    print("good")
##
##else:
##    print("baddd")
##                
x=True
while x:
    
    try:#to check whether it is a number 
        miles=float(input("Enter distance in miles here:"))
        km=miles*1.60934
        if km>=0:
            print("{0} miles is equals to {1:.3f} km.".format(miles,km))
            x=False
        else:
            print("Invalid value. Please enter a non-negative number.")
    except ValueError: #when user enters non-numbers
        print("You did not enter a non-negative number.")
