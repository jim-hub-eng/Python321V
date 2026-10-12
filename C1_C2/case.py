a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

print("[+] Sumar: a + b")
print("[-] Restar: a - b")
print("[*] Multiplicar: a * b")
print("[/] Dividir: a / b")

simbolo = input("Ingrese la operacion: ")

match simbolo:
    case '+':
        print("Resultado:" , (a + b))
    case '-':
            print("Resultado:" , (a - b))
    case '*':
            print("Resultado:" , (a * b))
    case '/':
            if b != 0:
                print("Resultado:" , (a / b))
            else:
                print("No se puede dividir entre 0.")
    case _:
        print("valor no valido")
