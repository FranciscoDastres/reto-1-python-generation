MAYOR_EDAD = 18

edad = input("Ingrese su edad: ")

if int(edad) > MAYOR_EDAD: # si es verdadero
    print("Eres mayor de edad")
elif int(edad) == MAYOR_EDAD:
    print("Eres mayor de edad, tienes exactamente 18 años")
else:
    print("Eres menor de edad")
