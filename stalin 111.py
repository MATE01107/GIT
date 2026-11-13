def cajero_automatico():
    saldo = 1000.0  # Saldo inicial de la cuenta
    salir = False

    while not salir:
        print("\n--- Bienvenido al Cajero Automático ---")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            print(f"\nTu saldo actual es: ${saldo:.2f}")

        elif opcion == "2":
            try:
                monto = float(input("Ingresa la cantidad a depositar: $"))
                if monto > 0:
                    saldo += monto
                    print(f"Has depositado ${monto:.2f}. Nuevo saldo: ${saldo:.2f}")
                else:
                    print("El monto a depositar debe ser mayor a cero.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

        elif opcion == "3":
            try:
                monto = float(input("Ingresa la cantidad a retirar: $"))
                if monto > 0:
                    if monto <= saldo:
                        saldo -= monto
                        print(f"Has retirado ${monto:.2f}. Nuevo saldo: ${saldo:.2f}")
                    else:
                        print("Fondos insuficientes para realizar el retiro.")
                else:
                    print("El monto a retirar debe ser mayor a cero.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

        elif opcion == "4":
            print("\nGracias por usar nuestro cajero automático. ¡Hasta luego!")
            salir = True

        else:
            print("Opción inválida. Por favor, selecciona una opción del 1 al 4.")

if __name__ == "__main__":
    cajero_automatico()
