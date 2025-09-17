#### 🔧 Ejercicios (Strings)

#1. Pedir una palabra y mostrarla en mayúsculas, minúsculas y *title case*.
palabra=input("ingrese una palabra ")
print(palabra.upper())
print(palabra.lower())
print(palabra.title())

#2. Pedir una frase y contar cuántas veces aparece cada vocal.
frase=input("ingrese una frase ")
vocales="aeiou"

for vocal in vocales:
    print(f"La vocal '{vocal}' aparece {frase.count(vocal)} veces")

#3. Dada una frase, mostrar las 3 primeras y las 3 últimas letras usando *slicing*.
frase2=input("ingrese una frase ")
print(frase2[:3])  
print(frase2[-3:])    

#4. Verificar si una palabra **contiene** la letra `'r'`. (Tip: `in`)
palabra2=input("ingrese una palabra ")
print('r' in palabra2)