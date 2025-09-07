año = int(input("Ingresa un año: "))

if año %400 == 0:
    print("El año es bisiesto")
elif año %100 == 0:
    print("El año no es bisiesto")
elif año %4 == 0:
    print("El año es bisiesto")