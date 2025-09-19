#🔧 Ejercicios (Recorridos)

#5. Pedir una palabra y contar cuántas vocales tiene.
print("----EJERCICIO 5----")
palabra=input("Ingrese una palabra: ")
vocales=0

for i in range(len(palabra)):
    if palabra[i]=='a' or palabra[i]=='e' or palabra[i]=='i' or palabra[i]=='o' or palabra[i]=='u':
        vocales=vocales+1

print(f"La cantidad de vocales de la palabra {palabra} es: {vocales}")

#6. Ingresar 4 palabras y mostrar únicamente las que contengan la letra 'r'.
print("----EJERCICIO 6----")
p1=input("Ingrese una palabra: ")
p2=input("Ingrese una palabra: ")
p3=input("Ingrese una palabra: ")
p4=input("Ingrese una palabra: ")

if 'r' in p1:
    print(f"{p1} contiene la letra r")

if 'r' in p2:
    print(f"{p2} contiene la letra r")

if 'r' in p3:
   print(f"{p3} contiene la letra r")

if 'r' in p4:
    print(f"{p4} contiene la letra r")

#7. Ingresar palabras hasta escribir `FIN`; imprimir las que **empiecen y terminen** con la misma letra.
print("----EJERCICIO 7----")
palabrasmismaletra=[]
p5=input("Ingrese una palabra: ")
while p5!="fin":
    if p5[-1]==p5[0]:
        palabrasmismaletra.append(p5)
        print("Empieza y termina con MISMA letra ")
    else:
        print("Empieza y termina con DISTINTA letra ")  
    p5=input("Ingrese una palabra (termina con 'fin'): ")      

print(f"Las palabras que empiezan y terminan con la misma letra son: {palabrasmismaletra}")