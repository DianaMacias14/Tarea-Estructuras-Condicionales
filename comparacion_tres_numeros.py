num1 = float(input("Ingresa un número: "))
num2 = float(input("Ingresa otro número: "))
num3 = float(input("Ingresa otro número: "))

if num1 > num2 and num1 > num3:
    print("El número ", num1,"es el mayor")
    print("Los números ", num2,"y", num3,"son menores")
elif num2 > num1 and num2 > num3:
    print("El número ", num2,"es el mayor")
    print("Los números ", num1,"y", num3,"son menores")
elif num3 > num1 and num3 > num2:
    print("El número ", num3,"es el mayor")
    print("Los números ", num1,"y", num2,"son menores")
elif num1 == num2 and num1 > num3:
    print("Los números con el valor de ", num1,"son mayores que el número: ", num3)
elif num2 == num3 and num2 > num1:
    print("Los números con el valor de ", num2,"son mayores que el número: ", num1)