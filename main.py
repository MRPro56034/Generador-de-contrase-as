import random

nombre = input("Introduce tu nombre:")

caracteres = str(nombre)

a = "Hola",nombre,"se generara una contraseña aleatoria,introuce el tamaño de la contraseña menor a",len(caracteres)
longitud = int(input(a))


contrasena = ""


for i in range(longitud):
    contrasena += random.choice(caracteres)

print("La contraseña generada es:", contrasena)
