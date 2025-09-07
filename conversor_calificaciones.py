calificacion = float(input("Ingresa una calificación: "))

if calificacion >= 90 and calificacion <= 100:
    print("La calificaión en letra es: A")
elif calificacion >= 80 and calificacion < 90:
    print("La calificaión en letra es: B")
elif calificacion >= 70 and calificacion < 80:
    print("La calificaión en letra es: C")
elif calificacion >= 60 and calificacion < 70:
    print("La calificaión en letra es: D")
elif calificacion >= 0 and calificacion < 60:
    print("La calificaión en letra es: F")
else:
    print("ERROR, la calificación ingresada no existe")