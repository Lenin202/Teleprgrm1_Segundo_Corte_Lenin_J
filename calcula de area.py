# Ejercicio 5.1...

print("CALCULO DE AREA DE UN CIRCULO")                               # imprimer en pantalla
2
Radio = float(input( "Inserte el Radio: "))                  # aqui se guarda el valor insertado en la variable Radio

while Radio<0:                                                           # ciclo while, si me ingresa una dato menor que
    print("Dato errado, tiene que ser un numero mayor igual que cero")   # cero me vuelve a preguntar insertar el Radio.
    Radio = float(input( "Inserte el Radio: "))
Pi = 3.14                                                              # le cargamos el valor de 3.14 a la variable Pii.

Area = Pi * Radio * Radio                                     # se realiza la multiplicacion de los tres datos

print(Area)                                                  # se manda imprimir el Area



