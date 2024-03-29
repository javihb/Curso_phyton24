### LISTAS ###

#Instancia
#Ejemplo 1
lista_uno = list()
#Ejemplo 2 
lista_dos = ["La ladera", 37]

lista_uno  = [ "Javier", "Holgado" ,27 , 27]
print(lista_uno)

print(lista_uno[2])
print(lista_uno[-1]) # OJO podemos aceder en el orden opuesto con negativos.
print(lista_uno.count(27))

nombre = lista_uno[0]
print(nombre)

#Se pueden concatenar listas de una manera muy facil. 
lista_tres = lista_uno + lista_dos
print(lista_tres)

lista_tres.append("Ubrique")
lista_tres.insert(0, "DATOS:")
#lista_tres.remove(27) #Indicamos el valor
#lista_tres.pop(1) #Indicamos el indice. (no es necesario indicarlo se eliminara el ultimo)
#del lista_tres[1] #como el POP pero es obligatorio el indice.

print(lista_tres)

#Ordenación ( mas detalle!!)
lista_tres.sort()
