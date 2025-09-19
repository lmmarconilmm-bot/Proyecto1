#🔧 Ejercicios (Listas)
#11. Ingresar notas hasta `-1`, calcular el **promedio** y cuántos están **por debajo**.

notas=[]
totalnotas=0
sumarnotas=0
nota=int(input("Ingrese una nota: "))

while nota!=-1:
    notas.append(nota)
    totalnotas=totalnotas+1
    sumarnotas+=nota
    nota=int(input("Ingrese una nota: (termina en -1)"))

print(notas)

prom=sumarnotas/totalnotas
print(f"El promedio es: {prom}")

pordebajo=0

for n in range(totalnotas):
    if notas[n]<prom:
        print(n)
        pordebajo+=1

print(f"La cantidad de notas por debajo del promedio son: {pordebajo}")

#12. Dada una lista de palabras, construir otra con las que tengan **más de 5** letras.

palabras=["gato", "perro", "loro", "lobo", "tigre", "elefante", "caballo"]
ListaP2=[]

for p in palabras:
    if len(p)>5:
        ListaP2.append(p)

print(f"Los animales con mas de 5 letras son: {ListaP2}")
