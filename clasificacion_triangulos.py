lado1 = float(input("Ingresa la longuitud del primer lado: "))
lado2 = float(input("Ingresa la longuitud del segundo lado: "))
lado3 = float(input("Ingresa la longuitud del tercer lado: "))

if (lado1 == lado2) and (lado2 == lado3) and (lado3 == lado1):
    print("Equilátero")
elif (lado1 != lado2) and (lado2 != lado3) and (lado3 != lado1):
    print("Escaleno")
else:
    print("Isósceles")