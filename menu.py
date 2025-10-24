import os
from typing import Callable, Tuple, Optional
try:
    from Juegos.adivina import adivinar_numero
    from Juegos.blackjack import jugar_blackjack
    from Juegos.craps import jugar_craps
    from Juegos.ruleta import jugar_ruleta
except ImportError as e:
    print(f"Error al importar módulos: {e}")
    exit(1)

def clear_screen() -> None:
    """Limpia la pantalla según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu(juegos: dict[str, Tuple[Callable[[Optional[int]], tuple[bool, Optional[int]]], str]]) -> None:
    """Muestra el menú de juegos disponible."""
    print("\n" + "="*50)
    print("        BIENVENIDO A LA SALA DE JUEGOS")
    print("="*50)
    print("¡Diviértete con nuestros juegos de azar y casino!")
    print("="*50)
    for key, (_, nombre) in juegos.items():
        print(f"{key}. {nombre}")
    print("5. Salir")
    print("="*50)

def main() -> None:
    """
    Función principal que ejecuta el menú interactivo de la sala de juegos.
    Mantiene un saldo global para los juegos que lo requieren y permite al usuario
    seleccionar un juego o salir.
    """
    saldo = 1000  # Saldo inicial para juegos con apuestas
    juegos = {
        '1': (adivinar_numero, "Adivina el número"),
        '2': (jugar_blackjack, "Blackjack"),
        '3': (jugar_craps, "Craps"),
        '4': (jugar_ruleta, "Ruleta")
    }

    while True:
        clear_screen()
        print(f"Saldo actual: ${saldo}")
        mostrar_menu(juegos)

        try:
            opc = input("Seleccione una opción entre 1 y 5: ").strip()
            if opc == '5':
                clear_screen()
                print(f"\nGracias por jugar. Saldo final: ${saldo}. ¡Hasta luego!")
                break
            if opc in juegos:
                clear_screen()
                try:
                    # Ejecutar el juego; devolverá (continuar, nuevo_saldo)
                    continuar, nuevo_saldo = juegos[opc][0](saldo if opc in ['2', '3', '4'] else None)
                    if nuevo_saldo is not None:
                        saldo = nuevo_saldo  # Actualizar saldo si el juego lo modifica
                    if not continuar:
                        print(f"\nJuego terminado. Saldo final: ${saldo}")
                        input("\nPresione Enter para continuar...")
                except Exception as e:
                    print(f"Error al ejecutar el juego: {e}")
                    input("\nPresione Enter para continuar...")
            else:
                print("\nOpción no válida. Intente de nuevo.")
                input("\nPresione Enter para continuar...")
        except KeyboardInterrupt:
            clear_screen()
            print(f"\nPrograma interrumpido. Saldo final: ${saldo}. ¡Adiós!")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")
            input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()