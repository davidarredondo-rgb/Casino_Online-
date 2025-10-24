import random
import os

def clear_screen() -> None:
    """Limpia la pantalla según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def obtener_carta() -> int:
    """Genera un número aleatorio entre 1 y 13 simulando una carta."""
    return random.randint(1, 13)

def valor_carta(carta: int, total: int) -> int:
    """Convierte la carta al valor de Blackjack. El As puede valer 1 u 11."""
    if carta == 1:  # As
        return 11 if total <= 10 else 1
    elif carta >= 2 and carta <= 10:
        return carta
    else:  # J, Q, K
        return 10

def imprimir_carta(carta: int) -> None:
    """Muestra la carta según el número generado."""
    if carta == 1:
        print("As", end="")
    elif carta == 11:
        print("J", end="")
    elif carta == 12:
        print("Q", end="")
    elif carta == 13:
        print("K", end="")
    else:
        print(carta, end="")

def jugar_blackjack(saldo: int) -> tuple[bool, int]:
    """
    Juego de Blackjack donde el jugador apuesta y juega contra el dealer.
    Args:
        saldo: Saldo actual del jugador.
    Returns:
        Tuple[bool, int]: (continuar_jugando, nuevo_saldo).
    """
    clear_screen()
    print("\n" + "="*50)
    print("        BIENVENIDO AL JUEGO DE BLACKJACK")
    print("="*50)
    print("   ¡Diviértete con nuestro juego de Blackjack!")
    print("="*50)

    while saldo > 0:
        print(f"\nSaldo actual: ${saldo}")
        try:
            apuesta = input("Ingrese su apuesta: ").strip()
            if not apuesta:
                print("Por favor, ingresa un número.")
                continue
            apuesta = int(apuesta)
            if apuesta <= 0 or apuesta > saldo:
                print("Apuesta inválida. Debe ser mayor que 0 y no exceder su saldo.")
                continue
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        saldo -= apuesta
        carta1_jugador = obtener_carta()
        carta2_jugador = obtener_carta()
        total_jugador = valor_carta(carta1_jugador, 0) + valor_carta(carta2_jugador, valor_carta(carta1_jugador, 0))
        carta1_dealer = obtener_carta()
        carta2_dealer = obtener_carta()
        total_dealer = valor_carta(carta1_dealer, 0) + valor_carta(carta2_dealer, valor_carta(carta1_dealer, 0))

        print("\nJUEGO DE BLACKJACK\n")
        print("Tus cartas son: ", end="")
        imprimir_carta(carta1_jugador)
        print(" y ", end="")
        imprimir_carta(carta2_jugador)
        print(f" [Total: {total_jugador}]")
        print("Cartas del dealer: ", end="")
        imprimir_carta(carta1_dealer)
        print(" y [carta oculta]")

        # Opción de doblar la apuesta
        if saldo >= apuesta:
            try:
                doble_apuesta = input("¿Desea doblar su apuesta? (s/n): ").lower().strip()
                while doble_apuesta not in ['s', 'n']:
                    print("Por favor, ingrese 's' o 'n'.")
                    doble_apuesta = input("¿Desea doblar su apuesta? (s/n): ").lower().strip()
                if doble_apuesta == 's':
                    saldo -= apuesta
                    apuesta *= 2
                    nueva_carta = obtener_carta()
                    total_jugador += valor_carta(nueva_carta, total_jugador)
                    print("Nueva carta del jugador: ", end="")
                    imprimir_carta(nueva_carta)
                    print(f" [Total: {total_jugador}]")
                    plantarse = True
                else:
                    plantarse = False
            except ValueError:
                print("Entrada inválida.")
                continue
        else:
            print("No tienes suficiente saldo para doblar la apuesta.")
            plantarse = False

        while not plantarse and total_jugador <= 21:
            try:
                decision = input("¿Desea plantarse? (s/n): ").lower().strip()
                while decision not in ['s', 'n']:
                    print("Por favor, ingrese 's' o 'n'.")
                    decision = input("¿Desea plantarse? (s/n): ").lower().strip()
                plantarse = decision == 's'
                if not plantarse:
                    nueva_carta = obtener_carta()
                    total_jugador += valor_carta(nueva_carta, total_jugador)
                    print("Nueva carta del jugador: ", end="")
                    imprimir_carta(nueva_carta)
                    print(f" [Total: {total_jugador}]")
            except ValueError:
                print("Entrada inválida.")
                continue

        if total_jugador > 21:
            print("Te pasaste de 21. Gana el dealer.")
        else:
            print("\nCartas del dealer: ", end="")
            imprimir_carta(carta1_dealer)
            print(" y ", end="")
            imprimir_carta(carta2_dealer)
            print(f" [Total: {total_dealer}]")
            while total_dealer < 17:
                nueva_carta = obtener_carta()
                total_dealer += valor_carta(nueva_carta, total_dealer)
                print("Nueva carta del dealer: ", end="")
                imprimir_carta(nueva_carta)
                print(f" [Total: {total_dealer}]")

            if total_dealer > 21:
                print("El dealer se pasó de 21. Gana el jugador.")
                saldo += apuesta * 2
            elif total_dealer > total_jugador:
                print("Gana el dealer.")
            elif total_dealer < total_jugador:
                print("Gana el jugador.")
                saldo += apuesta * 2
            else:
                print("Empate.")
                saldo += apuesta

        print(f"Fin de la ronda. Saldo actual: ${saldo}")
        if saldo <= 0:
            print("¡Te has quedado sin saldo!")
            input("\nPresiona Enter para volver al menú principal...")
            return (False, saldo)
        try:
            seguir = input("¿Desea jugar otra ronda? (s/n): ").lower().strip()
            while seguir not in ['s', 'n']:
                print("Por favor, ingrese 's' o 'n'.")
                seguir = input("¿Desea jugar otra ronda? (s/n): ").lower().strip()
            if seguir == 'n':
                input("\nPresiona Enter para volver al menú principal...")
                return (False, saldo)
        except ValueError:
            print("Entrada inválida.")
            continue

    input("\nPresiona Enter para volver al menú principal...")
    return (False, saldo)

if __name__ == "__main__":
    jugar_blackjack(1000)