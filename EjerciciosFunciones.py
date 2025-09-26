#🔧 Ejercicios (Funciones)
#8. Escribir `es_palindromo(cadena)` que devuelva `True` si la cadena se lee igual al derecho y al revés (ignorar espacios y mayúsculas/minúsculas).
print("-------EJERCICIO 8-------")
cadena=input("Ingrese una palabra: ")

def es_palindromo(cadena):
    cadena=cadena.lower()
    cadena=cadena.replace("","")
    if cadena ==cadena[::-1]: #comparo la cadena si se lee igual del derecho al revés(el -1 hace ir para atrás y los :: lee) 
        print("es palíndromo ")  
        return True 
    else: 
        print("no es palíndromo ")
        return False

es_palindromo(cadena)

#9. Escribir `contar_vocales(cadena)` que retorne un diccionario con la cuenta de cada vocal.
print("-------EJERCICIO 9-------")
def contar_vocales(cadena):    
    vocales="aeiou"
    cuentas = {ch: cadena.lower().count(ch) for ch in vocales} #cuenta cuántas veces aparece esa vocal en la cadena en minúsculas
    # recorre la lista de vocales y cuenta para cada una cuantas hay  
    return cuentas #retorno diccionario

print(contar_vocales(cadena)) #informo el informo de la funcion

#10. Escribir `normalizar_palabras(frase)` que retorne una **lista** de palabras sin signos de puntuación y en minúsculas.
print("-------EJERCICIO 10-------")
import re

def normalizar_palabras(frase):
    frase= frase.lower() #paso todo a minúsculas
    frase = re.sub(r'[^a-záéíóúüñ0-9\s]', '', frase) #lista sin signos de puntuación
    palabras=frase.split()  #separo las palabras de la frase
    return palabras #retorno lista
 
frase=input("Ingrese una frase: ")

print(normalizar_palabras(frase))  #informo el resultado de la funcion 
