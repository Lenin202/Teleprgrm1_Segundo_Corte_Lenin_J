# Ejercicio 5.2..
valor1 = float(input("Ingrese el primer numero:"))       #
valor2 = float(input("Ingrese el segundo numero:"))      #  Se crean las tres variable para guardar su datos solicitado
valor3 = float(input("Ingre1se el tercer numero:"))      #

if valor1>=valor2 and valor1>=valor3:                # se utilia un ciclo "if" con operadores logico
    print(f"El numero mayor es {valor1}")
elif valor2>=valor1 and valor2>=valor3:
    print(f"El numero mayor es {valor2}")
elif valor3>=valor2 and valor3>=valor1:
    print(f"El numero mayor es {valor3}")
