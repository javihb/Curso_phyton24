#Variables
var = 4

#Se pueden generar variables en cadena: 
nombre, apellidos = "Javier" , "holgado" 

#Funciones fáciles:
#Cuenta cadenas (solo string)
len("Esto es una cadena")

#Tipear variables (no tiene ninguna restriccion):
dirr: str = "La ladera"

# Operaciones matemáticas.
# + - * / %....
#Division aproximada "floor division"
10 // 3
#Exponentes 
2 ** 3


# "+" Tambien sirve para concatenar.
#print("Buenos" + "dias")
# El '*' tambien multiplica el string.
#print("Hola" * 5)

#Operaciones comparativos.
#print(3 <= 4)  
3 != 3

# Comparadores logicos
# AND OR y NOT 

# Para intenacionalizar o para incluir variables en texto lo mas recomendable es usar formateo.
#nombre = input("¿Cual es tu nombre?")

#cadena = "Hola {}".format(nombre)
#print(cadena)
#Otra manera. 
#cadena2 = "Hola %s" %(nombre)
#print(cadena2)

#Mas sencilla.
#print(f"Hola {nombre}")

#Desenpaquetado de caracteres:
idioma = "Python"
#idioma_split = idioma[1:3]
#print(idioma_split)

# UN PUNTO TRAS LA VARIABLE NOS INFORMA LAS FUNCIONES QUE PODEMOS USAR: 
if idioma.isnumeric():
    print("Es numerico")

