edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print("ERROR, esa edad no existe")
elif edad >= 0 and edad < 12:
    print("El costo de entrada para el parque es de: $50")
elif edad >= 12 and edad <= 17:
    print("El costo de entrada para el parque es de: $80")
else:
    print("El costo de entrada para el parque es de: $120")