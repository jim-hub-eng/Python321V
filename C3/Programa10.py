def hola(nombre, apellido):
    print("Hola que tal: ")
    print(f"Bienvenido {nombre.capitalize()} {apellido.capitalize()}")

#hola("jim", "gonzalez")
#hola("david", "mesas")

#def suma(a, b, c, d):
#   print(a+b+c+d)

#suma(3, 6, 4, 10)

def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(2, 3, 10, 72)