#🔧 Ejercicios (Funciones)
#8. Escribir `es_palindromo(cadena)` que devuelva `True` si la cadena se lee igual al derecho y al revés (ignorar espacios y mayúsculas/minúsculas).

cadena=input("ingrese una palabra ")

def es_palindromo(cadena):
    if cadena ==cadena[::-1]:
        print("es palíndromo ")  
        return True 
    else: 
        print("no es palíndromo ")
        return False

es_palindromo(cadena)

#9. Escribir `contar_vocales(cadena)` que retorne un diccionario con la cuenta de cada vocal.

def contar_vocales(cadena):
    vocales="aeiou"
    cuentas = {ch: cadena.lower().count(ch) for ch in vocales}
    return cuentas
    
print(contar_vocales(cadena))
    

#10. Escribir `normalizar_palabras(frase)` que retorne una **lista** de palabras sin signos de puntuación y en minúsculas.

import re
frase=input("Ingrese una frase: ")

def normalizar_palabras(frase):
    palabras=frase.split()  
    resultado=[
        re.sub(r'[^\wáéíóúüñ]', '', p.lower())
        for p in palabras if p
        ]
    return resultado

print(normalizar_palabras(frase))  





