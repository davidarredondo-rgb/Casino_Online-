import random
import os

def clear_screen() -> None:
    """Limpia la pantalla según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Ruleta:
    def __init__(self):
        self.numeros = list(range(37))
        self.rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        self.negros = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

    def girar_ruleta(self) -> int:
        """Simula el giro de la ruleta y devuelve un número aleatorio."""
        return random.choice(self.numeros)

    def obtener_color(self, numero: int) -> str:
        """Devuelve el color correspondiente al número."""
        if numero == 0:
            return "verde"
        return "rojo" if numero in self.rojos else "negro"

    def es_par(self, numero: int) -> bool:
        """Verifica si el número es par (excluye el 0)."""
        return numero != 0 and numero % 2 == 0

    def es_impar(self, numero: int) -> bool:
        """Verifica si el número es impar."""
        return numero % 2 == 1

    def obtener_docena(self, numero: int) -> int | None:
        """Devuelve la docena a la que pertenece el número."""
        if numero == 0:
            return None
        return 1 if 1 <= numero <= 12 else 2 if 13 <= numero <= 24 else 3

    def obtener_mitad(self, numero: int) -> str | None:
        """Devuelve la mitad a la que pertenece el número."""
        if numero == 0:
            return None
        return "primera" if 1 <= numero <= 18 else "segunda"

def jugar_ruleta(saldo: int) -> tuple[bool, int]:
    """
    Juego de Ruleta donde el jugador apuesta en diferentes opciones.
    En la apuesta 'Pleno', permite apostar a múltiples números (0-36).
    Args:
        saldo: Saldo actual del jugador.
    Returns:
        Tuple[bool, int]: (continuar_jugando, nuevo_saldo).
    """
    clear_screen()
    print("\n" + "="*50)
    print("         BIENVENIDO AL JUEGO DE LA RULETA")
    print("="*50)
    print("     ¡Diviértete con nuestro juego de ruleta!")
    print("="*50)
    print("Tipos de apuestas disponibles:")
    print("1. Pleno - Apostar a uno o más números (0-36) - Paga 36 a 1 por número ganador")
    print("2. Rojo/Negro - Apostar al color - Paga 1 a 1")
    print("3. Par/Impar - Apostar a números pares o impares - Paga 1 a 1")
    print("4. 1-18/19-36 - Apostar a primera o segunda mitad - Paga 1 a 1")
    print("5. Docena - Apostar a una docena (1-12, 13-24, 25-36) - Paga 2 a 1")

    ruleta = Ruleta()
    while saldo > 0:
        print(f"\nSaldo actual: ${saldo}")
        try:
            apuesta = input("Ingrese su apuesta ($): ").strip()
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

        try:
            tipo_apuesta = input("""
Seleccione el tipo de apuesta:
1. Pleno (uno o más números)
2. Color (rojo/negro)
3. Par/Impar
4. 1-18/19-36
5. Docena
Opción: """).strip()
            if not tipo_apuesta or tipo_apuesta not in ['1', '2', '3', '4', '5']:
                print("Opción inválida. Debe ser un número entre 1 y 5.")
                continue
            tipo_apuesta = int(tipo_apuesta)
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        apuesta_data = None
        if tipo_apuesta == 1:
            try:
                entrada_numeros = input("Ingrese los números a apostar (0-36, separados por comas): ").strip()
                if not entrada_numeros:
                    print("Por favor, ingresa al menos un número.")
                    continue
                # Dividir la entrada en una lista de números
                numeros_apostados = [num.strip() for num in entrada_numeros.split(',')]
                # Convertir a enteros y validar
                numeros_apostados = [int(num) for num in numeros_apostados if num]
                if not numeros_apostados:
                    print("Por favor, ingresa al menos un número válido.")
                    continue
                if any(num < 0 or num > 36 for num in numeros_apostados):
                    print("Todos los números deben estar entre 0 y 36.")
                    continue
                if len(numeros_apostados) > 36:
                    print("No puedes apostar a más de 36 números.")
                    continue
                # Eliminar duplicados, si los hay
                numeros_apostados = list(set(numeros_apostados))
                apuesta_por_numero = apuesta // len(numeros_apostados)  # Dividir la apuesta entre los números
                if apuesta_por_numero == 0:
                    print("La apuesta es demasiado baja para dividir entre tantos números.")
                    continue
                apuesta_data = (numeros_apostados, apuesta_por_numero)
            except ValueError:
                print("Por favor, ingrese números válidos separados por comas.")
                continue
        elif tipo_apuesta == 2:
            color_apostado = input("¿Rojo o Negro? (r/n): ").lower().strip()
            if color_apostado not in ['r', 'n']:
                print("Entrada inválida. Debe ser 'r' para rojo o 'n' para negro.")
                continue
            apuesta_data = color_apostado
        elif tipo_apuesta == 3:
            paridad = input("¿Par o Impar? (p/i): ").lower().strip()
            if paridad not in ['p', 'i']:
                print("Entrada inválida. Debe ser 'p' para par o 'i' para impar.")
                continue
            apuesta_data = paridad
        elif tipo_apuesta == 4:
            mitad = input("¿Primera mitad (1-18) o Segunda mitad (19-36)? (1/2): ").strip()
            if mitad not in ['1', '2']:
                print("Entrada inválida. Debe ser '1' para 1-18 o '2' para 19-36.")
                continue
            apuesta_data = mitad
        elif tipo_apuesta == 5:
            try:
                docena = input("¿Qué docena? (1: 1-12, 2: 13-24, 3: 25-36): ").strip()
                if not docena:
                    print("Por favor, ingresa un número.")
                    continue
                docena = int(docena)
                if docena < 1 or docena > 3:
                    print("Docena inválida. Debe ser 1, 2 o 3.")
                    continue
                apuesta_data = docena
            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue

        print("\n¡La ruleta gira...!")
        resultado = ruleta.girar_ruleta()
        color_resultado = ruleta.obtener_color(resultado)
        print(f"¡La bola cae en el {resultado} {color_resultado}!")

        gano = False
        ganancia = 0
        if tipo_apuesta == 1:
            numeros_apostados, apuesta_por_numero = apuesta_data
            if resultado in numeros_apostados:
                gano = True
                ganancia = apuesta_por_numero * 36  # Pago 36 a 1 por el número ganador
            apuesta_total = apuesta_por_numero * len(numeros_apostados)  # Total apostado
        else:
            apuesta_total = apuesta
            if tipo_apuesta == 2:
                if (apuesta_data == 'r' and color_resultado == "rojo") or \
                   (apuesta_data == 'n' and color_resultado == "negro"):
                    gano = True
                    ganancia = apuesta * 2
            elif tipo_apuesta == 3:
                if (apuesta_data == 'p' and ruleta.es_par(resultado)) or \
                   (apuesta_data == 'i' and ruleta.es_impar(resultado)):
                    gano = True
                    ganancia = apuesta * 2
            elif tipo_apuesta == 4:
                mitad_resultado = ruleta.obtener_mitad(resultado)
                if (apuesta_data == '1' and mitad_resultado == "primera") or \
                   (apuesta_data == '2' and mitad_resultado == "segunda"):
                    gano = True
                    ganancia = apuesta * 2
            elif tipo_apuesta == 5:
                docena_resultado = ruleta.obtener_docena(resultado)
                if docena_resultado == apuesta_data:
                    gano = True
                    ganancia = apuesta * 3

        if gano:
            saldo += ganancia - apuesta_total
            print(f"¡Felicidades! Has ganado ${ganancia - apuesta_total}")
        else:
            saldo -= apuesta_total
            print(f"Lo siento, has perdido ${apuesta_total}")

        print(f"Tu saldo actual es: ${saldo}")
        if saldo <= 0:
            print("¡Te has quedado sin saldo!")
            input("\nPresiona Enter para volver al menú principal...")
            return (False, saldo)

        try:
            continuar = input("\n¿Desea seguir jugando? (s/n): ").lower().strip()
            while continuar not in ['s', 'n']:
                print("Por favor, ingrese 's' o 'n'.")
                continuar = input("\n¿Desea seguir jugando? (s/n): ").lower().strip()
            if continuar != 's':
                input("\nPresiona Enter para volver al menú principal...")
                return (False, saldo)
        except ValueError:
            print("Entrada inválida.")
            continue

    input("\nPresiona Enter para volver al menú principal...")
    return (False, saldo)

if __name__ == "__main__":
    jugar_ruleta(1000)