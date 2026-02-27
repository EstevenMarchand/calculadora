from calculator import sumar, restar, multiplicar, dividir

def leer_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Ingresa un número válido.")

def menu():
    print("\n=== CALCULADORA ===")
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Salir")

while True:
    menu()
    opcion = input("Elige una opción: ").strip()

    if opcion == "5":
        print("Bye")
        break

    if opcion not in {"1", "2", "3", "4"}:
        print("Opción inválida")
        continue

    a = leer_numero("Primer número: ")
    b = leer_numero("Segundo número: ")

    try:
        if opcion == "1":
            print("Resultado:", sumar(a, b))
        elif opcion == "2":
            print("Resultado:", restar(a, b))
        elif opcion == "3":
            print("Resultado:", multiplicar(a, b))
        elif opcion == "4":
            print("Resultado:", dividir(a, b))
    except ZeroDivisionError as e:
        print("Error:", e)