# Casino_Online-
Proytecto de Programacion de Computadores 
⦁ Este proyecto implementa una sala de juegos interactiva en consola que incluye
cuatro juegos clásicos de casino y azar.
Juegos disponibles:
• Adivina el número: Un juego simple donde debes adivinar un número entre
1 y 1000.
• Blackjack: El clásico juego de cartas donde debes acercarte lo más posible
a 21 sin pasarte.
• Craps: Juego de dados donde se apuesta al resultado de los lanzamientos.
• Ruleta: Versión simplificada de la ruleta de casino con varias opciones de
apuesta.
Requisitos:
⦁ Python 3.8+
Estructura:
proyecto_juegos/
├── Juegos/
│ ├── adivina.py
│ ├── blackjack.py
│ ├── craps.py
│ └── ruleta.py
├── menu.py
└── README.md
¿Cómo jugar?:
⦁ Ejecuta el archivo principal:
python menu.py
⦁ Sigue las instrucciones en pantalla para navegar por el menú y seleccionar el
juego que deseas jugar.
Reglas de los juegos
Adivina el número
⦁ Se genera un número aleatorio entre 1 y 1000.
Estudiantes: David Arredondo Alcala – Paula Andrea Mera Mutis
Tu objetivo es adivinar el número con la menor cantidad de intentos posible.
Después de cada intento, recibirás una pista indicando si el número es mayor o
menor.
Blackjack
⦁ Tu objetivo es conseguir una mano con un valor más cercano a 21 que la del
dealer, sin pasarte.
Las cartas numéricas valen su valor nominal, las figuras (J, Q, K) valen 10.
Puedes pedir cartas adicionales o plantarte en cualquier momento.
También tienes la opción de doblar tu apuesta.
Craps
⦁ En el primer lanzamiento, ganas si obtienes 7 u 11, y pierdes si obtienes 2, 3
o 12.
Si obtienes cualquier otro número, ese se convierte en tu "punto".
Debes seguir lanzando hasta obtener tu punto (ganas) o un 7 (pierdes).
Ruleta
⦁ Puedes realizar diferentes tipos de apuestas:
1. Pleno: Apostar a un solo número (paga 36 a 1)
2. Color: Rojo o negro (paga 1 a 1)
3. Par/Impar: Números pares o impares (paga 1 a 1)
4. 1-18/19-36: Primera o segunda mitad (paga 1 a 1)
5. Docena: Grupos de doce números (paga 2 a 1)




Interfaces que se pueden encontrar en el codigo:
1. Para el primer menu del comienzo al inicializar el codigo:
Saldo actual: $1000

==================================================
        BIENVENIDO A LA SALA DE JUEGOS
==================================================
¡Diviértete con nuestros juegos de azar y casino!
==================================================
1. Adivina el número
2. Blackjack
3. Ruleta
5. Salir
==================================================
Seleccione una opción entre 1 y 4:


2. Para el menu del juego llamado adivina el numero:

==================================================
      BIENVENIDO A LA ADIVINANZA DE NÚMEROS
==================================================
       He pensado un número entre 1 y 1000.
      Tienes 15 intentos para adivinarlo.
==================================================

Intento #1: 

3. Para el menu dle juego llamado Blackjack:

   ==================================================
        BIENVENIDO AL JUEGO DE BLACKJACK
==================================================
   ¡Diviértete con nuestro juego de Blackjack!
==================================================

Saldo actual: $1000
Ingrese su apuesta: 

4. Para el menu del juego llamado ruleta:

   ==================================================
         BIENVENIDO AL JUEGO DE LA RULETA
==================================================
     ¡Diviértete con nuestro juego de ruleta!
==================================================
Tipos de apuestas disponibles:
1. Pleno - Apostar a uno o más números (0-36) - Paga 36 a 1 por número ganador
2. Rojo/Negro - Apostar al color - Paga 1 a 1
3. Par/Impar - Apostar a números pares o impares - Paga 1 a 1
4. 1-18/19-36 - Apostar a primera o segunda mitad - Paga 1 a 1
5. Docena - Apostar a una docena (1-12, 13-24, 25-36) - Paga 2 a 1

Saldo actual: $1000
Ingrese su apuesta ($): 

5. Para lo ultimo cuando el usiuario quiere salir solo sale un mensaje pequeño:
   Gracias por jugar. Saldo final: $1000. ¡Hasta luego!
