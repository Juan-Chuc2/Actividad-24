def saludar():
    return "----Bienvenido----"

while True:
    print("=MENU==")
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