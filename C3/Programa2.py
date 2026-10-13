#Imprimir elementos de una lista con for
lista = [2,3,4,5]

print("Lista De Numeros")
for iterador in lista:
    print(iterador)

print("Lista De String")
lista_texto = ["hola", "como", "estas", "?"]

for valor in lista_texto:
    print(valor)

print("Lista De Numeros de 0 a 9")
for it in range(9):
    print(it)

print("Lista De Numeros Pares impares y multiplos")
collecion = [2, 4, 5, 7, 8, 9, 3, 4]

for e in collecion:
    #if e % 2 != 0:
    if e % 4 != 0:
        continue
    print(e)