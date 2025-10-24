import random
import os

def clear_screen() -> None:
    """Limpia la pantalla según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def adivinar_numero(_: None) -> tuple[bool, None]:
    """
    Juego de adivinar un número entre 1 y 1000.
    El usuario tiene un número limitado de intentos para adivinar el número generado aleatoriamente.
    Args:
        _: Ignorado (para compatibilidad con otros juegos que usan saldo).
    Returns:
        Tuple[bool, None]: (continuar_jugando, None) ya que no maneja saldo.
    """
    numero_aleatorio = random.randint(1, 1000)
    intentos = 0
    max_intentos = 15

    clear_screen()
    print("\n" + "="*50)
    print("      BIENVENIDO A LA ADIVINANZA DE NÚMEROS")
    print("="*50)
    print("       He pensado un número entre 1 y 1000.")
    print(f"      Tienes {max_intentos} intentos para adivinarlo.")
    print("="*50)

    adivinado = False
    while not adivinado and intentos < max_intentos:
        try:
            intento_usuario = input(f"\nIntento #{intentos + 1}: ").strip()
            if not intento_usuario:
                print("Por favor, ingresa un número.")
                continue
            intento_usuario = int(intento_usuario)
            if intento_usuario < 1 or intento_usuario > 1000:
                print("El número debe estar entre 1 y 1000.")
                continue
            intentos += 1

            if intento_usuario == numero_aleatorio:
                print(f"\n¡FELICIDADES! Has adivinado el número en {intentos} intentos.")
                adivinado = True
            else:
                print("El número es MAYOR." if intento_usuario < numero_aleatorio else "El número es MENOR.")
                print(f"Te quedan {max_intentos - intentos} intentos.")
                if intentos < max_intentos:
                    rendirse = input("¿Quieres rendirte? (s/n): ").lower().strip()
                    while rendirse not in ['s', 'n']:
                        print("Por favor, ingresa 's' o 'n'.")
                        rendirse = input("¿Quieres rendirte? (s/n): ").lower().strip()
                    if rendirse == 's':
                        print(f"\nEl número era: {numero_aleatorio}")
                        break
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

    if not adivinado and intentos >= max_intentos:
        print(f"\n¡Se agotaron tus intentos! El número era: {numero_aleatorio}")

    input("\nPresiona Enter para volver al menú principal...")
    return (True, None)

if __name__ == "__main__":
    adivinar_numero(None)