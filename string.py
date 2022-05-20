# Ejercicio 5.4..

def leer_frase():                     # leemos la frase
    global txt
    txt = (input("   Ingrese un texto:  "))   # guardamos la frase en la variable txt

    def centrar_texto(tira, cantidad):                     # se calcula la longitud del texto
        longitud = int((cantidad - len(tira)) / 2)
        print(f"{tira:^{cantidad}}")
        print("Numero de espacios agrear para centrar:" + str(longitud))

    centrar_texto(txt, 40)

def contar_letras():                  # realiza el conteo de las letras
    conta=0
    for i in txt:
        if(i.isalpha()):
            conta+=1
    print("la cantidad de letra:", conta)

leer_frase()
contar_letras()
