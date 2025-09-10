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

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def contar_letra(palabra, letra):
    if not palabra:
        return 0
    else:
        return (1 if palabra[0] == letra else 0) + contar_letra(palabra[1:], letra)

def invertir_cadena(cadena):
    if not cadena:
        return ""
    else:
        return invertir_cadena(cadena[1:]) + cadena[0]

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

saludar()
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
            print("\n--Factorial--")
            numero = int(input("Ingrese el numero a calcular: "))
            print(factorial(numero))

        case "2":
            print("\n--Suma N numeros--")
            numero = int(input("Ingrese el numero a calcular: "))
            print(suma_n(numero))

        case "3":
            print("\n--FIBONACCI--")
            n = int(input("Ingrese un número entero positivo: "))
            print(f"Fibonacci({n}) =", fibonacci(n))

        case "4":
            print("\n--Calcular N-enesimo--")
            palabra = input("Ingrese una palabra: ").strip()
            letra = input("Ingrese la letra a buscar: ").strip()
            print(f"La letra '{letra}' aparece {contar_letra(palabra, letra)} veces.")

        case "5":
            print("\n--Invertir Cadena--")
            cadena = input("Ingrese una cadena de texto: ")
            print("Cadena invertida:", invertir_cadena(cadena))

        case "6":
            print("\n--Calcular Exponente--")
            base = int(input("Ingrese la base: "))
            exponente = int(input("Ingrese el exponente: "))
            print(f"{base}^{exponente} =", potencia(base, exponente))

        case "7":
            print("GRACIAS POR USAR EL PROGRAMA!!")
            break

        case _:
            print("Error vuelva a intentar con un caracter valido")

