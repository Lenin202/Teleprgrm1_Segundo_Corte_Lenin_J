#Ejercicio 5.3...

cantidad= int(input("Ingrese la cantida de numero de la lista:"))
suma=0
par=0
impar=0

for i in range(1,cantidad+1):
    num=int(input(f"digite el numero {i}:"))

    if num%2==0:
        par=par+num
    else:
        impar=impar+num

print("la suma de los numeros impares:",impar)



