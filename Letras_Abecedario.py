#1.-Que en un bucle infinito solicite al usuario una letra (debes especificar al usuario 
    #la condición para terminar el programa. Por ejemplo, para salir, escriba alto, 
    #presione 0 o cualquier otra que se te ocurra).
#2. Harás una función que imprima en la pantalla la letra siguiente en el alfabeto y
    # la letra anterior a la ingresada.
#3. El programa debe continuar en el bucle hasta que el usuario decida salir del programa

import string

def abc(x):

    alfabeto = list(string.ascii_lowercase) #Trae el alfabeto en letras minusculas
#print(alfabeto) # Imprime el alfabeto
# print(alfabeto.index('n')) Imprime el indice de la letra en el parentesis
    print("letra ingresada: " + x)
    print("Letra anterior: " + alfabeto[alfabeto.index(x)-1])
    if x == "z":
        print("Letra siguiente a")
    else:
        print("letra siguiente: " + alfabeto[alfabeto.index(x)+1])
 
while True:  # Aqui indica como salir con una tecla en este caso es 0 
    try:
        x = input("Ingresa una letra del abecedario o 0 para salir: ")
        if x == "0" :
            break
        else:
            abc(x.lower()) #Aqui manda llamar la función
    except ValueError:
        print("Ingrese un caracter válido")

