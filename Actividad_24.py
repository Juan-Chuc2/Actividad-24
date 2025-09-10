def saludar():
    return "----Bienvenido----"

def factorial(numero):
    if numero ==0 or numero==1:
        return 1
    else:
        return numero * factorial(numero-1)

def suma_n(numero):
    if numero ==0:
        return 0
    else:
        return numero+suma_n(numero-1)

def contar_letra(palabra, letra):
    if not palabra:
        return 0
    else:
        return (1 if palabra[0] == letra else 0) + contar_letra(palabra[1:], letra)
while True:
    print("MENU")
    print("1. Calcular Factorial")
    print("2. Suma de N numeros")
    print("3. Calcular n-enesimo")
    print("4. Contar Letra")
    print("5. Invertir una cadena")
    print("6. Calcular la potencia")
    print("7. Salir")

    option = input("Ingrese una opcion (1-7): ")
    match option:
        case "1":
            print("--Factorial--")
            numero = int(input("Ingrese el numero a calcular: "))
            print(factorial(numero))

        case "2":
            print("--Suma N numeros--")
            numero = int(input("Ingrese el numero a calcular: "))
            print(suma_n(numero))

        case "4":
            print("--Calcular N-enesimo--")
            palabra = input("Ingrese una palabra: ").strip()
            letra = input("Ingrese la letra a buscar: ").strip()
            print(f"La letra '{letra}' aparece {contar_letra(palabra, letra)} veces.")

