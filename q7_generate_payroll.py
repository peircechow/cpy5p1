##q7_generate_payroll.py


boolean=True
while boolean:
    a=input("Enter name:")
    b=input("Enter no. of hours worked weekly:")
    c=input("Enter hourly pay rate($)")
    d=input("Enter CPF contribution rate(%):")
    
    def check_input(b,c,d):
        try:
            int(b)  
            float(c)
            float(d)
            return True
        except ValueError:
            return False

    if check_input(b,c,d):
        b=int(b)  
        c=float(c)
        d=float(d)
        print("Payroll statement for",a)
        print("No. of hours worked in a week:",b)
        print("Hourly pay rate: $",c)
        gp=b*c
        print("Gross pay =$",gp)
        cpf=gp/100*d
        print("CPF contribution at {0}%:${1:.2f}".format(d,cpf))
        np=gp-cpf
        print("Net pay =$",np)
        boolean=False

    else:
        print("Please try again!")
