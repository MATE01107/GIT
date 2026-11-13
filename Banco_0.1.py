def cajero_automatico():
    saldo = 1000.00  # Saldo inicial de ejemplo

    while True:
        print("\n=== BIENVENIDO AL BANCO ===")
        print("1. Ver saldo")
        print("2. Depósito")
        print("3. Retiro")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            print(f"\nTu saldo actual es: ${saldo:.2f}")

        elif opcion == "2":
            try:
                monto = float(input("\nIngresa el monto a depositar: $"))
                if monto > 0:
                    saldo += monto
                    print(f"Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
                else:
                    print("Error: El monto debe ser mayor a 0.")
            except ValueError:
                print("Error: Por favor ingresa un número válido.")

        elif opcion == "3":
            try:
                monto = float(input("\nIngresa el monto a retirar: $"))
                if monto <= 0:
                    print("Error: El monto debe ser mayor a 0.")
                elif monto > saldo:
                    print("Error: Fondos insuficientes.")
                else:
                    saldo -= monto
                    print(f"Retiro exitoso. Nuevo saldo: ${saldo:.2f}")
            except ValueError:
                print("Error: Por favor ingresa un número válido.")

        elif opcion == "4":
            print("\nGracias por usar nuestro banco. ¡Hasta luego!")
            break

        else:
            print("\nOpción no válida. Por favor elige un número del 1 al 4.")

# Ejecutar el programa
if __name__ == "__main__":
    cajero_automatico()