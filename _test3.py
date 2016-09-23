def quadratic():
    a = float(input("Input first coefficient: "))
    b = float(input("Input second coefficient: "))
    c = float(input("Input third coefficient: "))
    x = (-b+(b**2-4*a*c)**.5)/(2*a)
    print(float(x))
    return(float(x))

while True:
    quadratic()
    
