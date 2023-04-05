a=int(input("Enter the principal value"))
b=int(input("Enter the years:"))
d=input("The person is senior citizen or not:")
c=input("The person is male/female:")
print(c)
x=b*12
if d==("yes" or "y"):
    if c== "male":
        m_simple_intrest=(a*12/100)*x
        print("The simple interest is",m_simple_intrest)
    elif c=="female":
         f_simple_intrest=(a*15/100)*x
         print("The simple intrest is",f_simple_intrest)
    else:
        print("Enter the correct character")
else:
    n_simple_intrest=(a*10/100)*x
    print("The simple intrest is",n_simple_intrest)
