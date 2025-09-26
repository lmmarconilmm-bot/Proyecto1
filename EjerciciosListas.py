#🔧 Ejercicios (Listas)
#11. Ingresar notas hasta `-1`, calcular el **promedio** y cuántos están **por debajo**.
print("-------EJERCICIO 11-------")
notas=[]
totalnotas=0
sumarnotas=0
nota=float(input("Ingrese una nota: "))

while nota!=-1: #mientras la nota sea distinta a -1
    if (nota<1 or nota>10): #verifico que la nota sea entre 1 y 10
        print("nota no válida ") 
    else:
        notas.append(nota) #agrego la nota a la lista
        totalnotas=totalnotas+1 #cuento las notas para calcular el promedio
        sumarnotas+=nota #sumo las notas
    nota=float(input("Ingrese una nota (termina con -1):"))

print(notas) #imprimo lista

prom=sumarnotas/totalnotas #calculo promedio
print(f"El promedio es {prom}")

pordebajo=0

for n in range(totalnotas): #recorro lista para verificar si el promedio es mayor que la nota
    if notas[n]<prom:
        pordebajo+=1 #si se cumple, sumo uno en la variable 

print(f"La cantidad de notas por debajo del promedio son: {pordebajo}") #informo 

#12. Dada una lista de palabras, construir otra con las que tengan **más de 5** letras.
print("-------EJERCICIO 12-------")
palabras=["gato", "perro", "loro", "lobo", "tigre", "elefante", "caballo"] #armo lista de palabras
ListaP2=[] #declaro lista de palabras con más de 5 letras

for p in palabras: #recorro la lista dada
    if len(p)>5:
        ListaP2.append(p) #uso el len para preguntar la cantidad de letras, si es verdadero, agrego la palabra a listaP2

print(palabras)

print(f"Los animales con mas de 5 letras son: {ListaP2}") #informo ambas listas
