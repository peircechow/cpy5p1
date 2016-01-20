##q2_calc_cylinder_volume.py
#area = radius * radius * pi
#volume = area * length   
##x=True
##while x:
##    print("Cylinder volume calculator.")
##    pi=3.14159265359
##    r=float(input("Enter radius in m here:"))
##    l=float(input("Enter length in m here:"))
##    vol=r*2*pi*l
##    print("Volume of cylinder is {0:.2f}m (2d.p).".format(vol))

print("Cylinder volume calculator:D")
pi=3.14159265359
x=True
while x:
    try:
        r=float(input("Enter radius in m here:"))
        l=float(input("Enter length in m here:"))
        vol=r*r*pi*l
        if r>=0 and l>=0:#cannot be negative numbers!
            print("The volume of cylinder is {0:.2f}m^3 (2d.p).".format(vol))
            x=False
        else:
            print("Please enter a non-negative value.")
    except ValueError:
        print("Invalid value! Please try again.")
