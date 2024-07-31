try:
    x=int(input("enter a number:",))
    y=int(input("enter another number:"))
    z=x/y
    print("Z:",z)
except (ValueError,ZeroDivisionError,KeyboardInterrupt):
    print("error occured")
