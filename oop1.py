def take_value():
    p = int(input("enter the principal"))
    t = int(input("enter the time"))
    r = int(input("enter the rate"))
    return p,t,r

def calculate_value():
    a,b,c = take_value()
    cal = a*b*c/100

    print(f"The simple interest is {cal}")




def display_value():
    calculate_value()
print(calculate_value())

