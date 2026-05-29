# AyED 2026 - TP 1 - ISI 111
# Integrantes:
# - Fabrizio Fontanarrosa
# - Clemente Giorgi
# - Santiago Marchionatti
# - Lautaro Casagrande

# Bibliotecas
import os
import random

# Constantes de colores
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"  # orange on some systems
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
WHITE = "\033[97m"

RESET = "\033[0m"

# Definición de funciones


def limpiarPantalla():
    os.system(comandoLimpiar)


def cartelInicio():
    limpiarPantalla()
    print("")
    print(
        "----------------------------------------------------------------------------------------------------------"
    )
    print("")
    print(
        "Los juegos de apuestas están"
        + RED
        + " prohibidos "
        + RESET
        + "para los menores de 18 años, y son"
        + RED
        + " perjudiciales "
        + RESET
        + "para la salud."
    )
    print("")
    print("Juegue por diversión. Juegue con responsabilidad.")
    print("")
    print(
        "----------------------------------------------------------------------------------------------------------"
    )
    print("")
    print("")
    input("Presione Enter para continuar\n")


def menu():
    limpiarPantalla()
    print("")
    print("")
    print(
        BLUE
        + "PYTHON "
        + BRIGHT_YELLOW
        + "CASINO"
        + RESET
        + " - "
        + GREEN
        + "MENÚ PRINCIPAL"
        + RESET
    )
    print("")
    print("Lista de opciones:")
    print(GREEN + "A" + RESET + " - Juego del menor-mayor")
    print(GREEN + "B" + RESET + " - Número secreto")
    print(GREEN + "C" + RESET + " - Blackjack")
    print(GREEN + "D" + RESET + " - Par o impar")
    print(MAGENTA + "E" + RESET + " - Reporte")
    print(RED + "F" + RESET + " - Salir")
    print("")


# Juego del Menor - Mayor
def juego1():
    # Declaracion de variables:
    # STRING:
    # nombre, prediccion, continuar
    # BOOL:
    # prediccionValida, acierto, juegoTerminado
    # INT:
    # numeroActual, numeroSiguiente, racha
    global juego1_nombre
    global juego1_jugadas
    global juego1_mayor_racha
    limpiarPantalla()
    nombre = input("Ingresa tu nombre: ")
    print(f"¡Hola {nombre}! Vamos a jugar al Menor-Mayor.")
    print("Te muestro un numero y tenés que adivinar si el siguiente es Mayor o Menor")

    numeroActual = random.randint(1, 1000)
    print(f"Numero actual: {numeroActual}")
    racha = 0
    juegoTerminado = False

    while not juegoTerminado:
        prediccion = input("¿Mayor o Menor? ")

        prediccionValida = False
        while not prediccionValida:
            if (
                prediccion == "mayor"
                or prediccion == "menor"
                or prediccion == "MAYOR"
                or prediccion == "MENOR"
                or prediccion == "Mayor"
                or prediccion == "Menor"
            ):
                prediccionValida = True

                if (
                    prediccion == "mayor"
                    or prediccion == "MAYOR"
                    or prediccion == "Mayor"
                ):
                    prediccion = "mayor"
                else:
                    prediccion = "menor"
            else:
                print("Por favor ingrese solo 'mayor' o 'menor'")
                prediccion = input("¿MAYOR o MENOR? ")

        numeroSiguiente = random.randint(1, 1000)

        acierto = False
        if prediccion == "mayor" and numeroSiguiente > numeroActual:
            acierto = True
        elif prediccion == "menor" and numeroSiguiente < numeroActual:
            acierto = True

        if acierto:
            racha += 1
            print(
                GREEN
                + f"¡Acertaste! El numero era {numeroSiguiente}\nRacha: {racha}"
                + RESET
            )
        else:
            print(RED + f"¡Le erraste! El numero era {numeroSiguiente}" + RESET)

            print(f"\n{nombre}, ¿Queres seguir jugando?")
            continuar = input(
                "Ingresa 'si' para seguir jugando o 'no' para volver al menu: "
            )

            while (
                continuar != "si"
                and continuar != "no"
                and continuar != "Si"
                and continuar != "No"
            ):
                print("Por favor ingrese solo 'si' o 'no'")
                continuar = input(
                    "Ingresa 'si' para segyur jugando o 'no' para volver al menu: "
                )
            juego1_jugadas += 1
            if continuar == "si" or continuar == "Si":
                racha = 0
                print(f"¡Nueva oportunidad! Vamos de nuevo.")
            else:
                print(
                    f"¡Juego terminado {nombre}! La racha final fue de {racha} aciertos."
                )
                juegoTerminado = True

        if not juegoTerminado:
            numeroActual = random.randint(1, 1000)
            print(f"Nuevo numero: {numeroActual}\n")

        if racha > juego1_mayor_racha:
            juego1_nombre = nombre
            juego1_mayor_racha = racha


# Numero secreto
def juego2():
    # Declaración de variables
    # INT:
    # IntentosRestantes, IntentosRealizados, juego2_jugadas, juego2_ganadas, juego2_perdidas, Intento, Entrada, numerosecreto
    # BOOL:
    # es_valido
    # STRING:
    # Respuesta
    global juego2_nombre
    global juego2_jugadas
    global juego2_ganadas
    global juego2_perdidas
    limpiarPantalla()
    print("¡Bienvenido al juego del número secreto!")
    juego2_nombre = input("¿Cuál es tu nombre? ")
    print("Hola", juego2_nombre, "¡Vamos a jugar al número secreto!")
    print(
        "El juego consiste en adivinar un número entre 1 y 100. Tienes 6 intentos para adivinarlo. ¡Buena suerte!"
    )

    IntentosRestantes = 6
    IntentosRealizados = 0

    Respuesta = "s"
    while Respuesta == "s" or Respuesta == "S":
        juego2_jugadas = juego2_jugadas + 1
        numerosecreto = random.randint(1, 100)
        IntentosRestantes = 6
        IntentosRealizados = 0
        Intento = 0

        while IntentosRestantes > 0:
            es_valido = False
            while not es_valido:
                Entrada = input("Introduce tu intento (1-100): ")

                es_numerico = True
                if len(Entrada) == 0:
                    es_numerico = False

                for caracter in Entrada:
                    if not ("0" <= caracter <= "9"):
                        es_numerico = False

                if es_numerico:
                    Intento = int(Entrada)
                    if 1 <= Intento <= 100:
                        es_valido = True
                    else:
                        print(
                            "Número inválido. Por favor, introduce un número entre 1 y 100."
                        )
                else:
                    print("Por favor introduzca un número. Inténtalo de nuevo.")

            IntentosRealizados = IntentosRealizados + 1

            if Intento == numerosecreto:
                print(
                    "¡Felicidades",
                    juego2_nombre,
                    "has adivinado el número secreto! Lo has logrado en",
                    IntentosRealizados,
                    "intentos.",
                )
                juego2_ganadas = juego2_ganadas + 1
                IntentosRestantes = 0
            elif Intento < numerosecreto:
                print("El número secreto es mayor que", Intento)
            else:
                print("El número secreto es menor que", Intento)

            IntentosRestantes = IntentosRestantes - 1
            if IntentosRestantes > 1:
                print("Te quedan", IntentosRestantes, "intentos.")
            elif IntentosRestantes == 1:
                print("Te queda", IntentosRestantes, "intento.")

        if Intento != numerosecreto:
            print("No te quedan intentos. El número secreto era", numerosecreto)
            juego2_perdidas = juego2_perdidas + 1

        print(
            "Has jugado",
            juego2_jugadas,
            "veces, has acertado",
            juego2_ganadas,
            "veces y has perdido",
            juego2_perdidas,
            "veces.",
        )
        Respuesta = str(input("¿Deseas jugar nuevamente? (s/n) "))
        while (
            Respuesta != "s"
            and Respuesta != "n"
            and Respuesta != "S"
            and Respuesta != "N"
        ):
            Respuesta = input("Por favor ingresa 's' o 'n': ")

    print("\n¡Gracias por jugar, hasta la próxima!")
    print(
        "Has jugado",
        juego2_jugadas,
        "veces, has acertado",
        juego2_ganadas,
        "veces y has perdido",
        juego2_perdidas,
        "veces.",
    )

    input("\nPresione Enter para volver\n")


def juego3():
    limpiarPantalla()
    input("Juego en construcción. Volvé pronto!\n\nPresione Enter para volver\n")


# Par o impar
def juego4():
    # Declaración de variables
    # STRING:
    # continuar, respuesta_j, resultado_caras
    # INT:
    # caraUno, caraDos, suma_caras
    limpiarPantalla()
    global juego4_nombre
    global juego4_jugadas
    global juego4_ganadas
    global juego4_perdidas

    juego4_nombre = input("Jugador/a, ingrese su nombre: \n")

    print(f"\n{juego4_nombre}, sumaremos dos numeros entre 1 y 6.")
    print("Si el resultado es par, usted ganara y sumara un punto.")
    print("De lo contrario perdera y no sumara puntos.")

    continuar = "si"
    while (
        continuar == "si" or continuar == "Si" or continuar == "SI" or continuar == "sI"
    ):

        caraUno = random.randint(1, 6)
        caraDos = random.randint(1, 6)
        suma_caras = caraUno + caraDos

        # esto es lo que le sumé:

        respuesta_j = input(f"\n{juego4_nombre}. Par o impar?: \n")

        while (
            respuesta_j != "par"
            and respuesta_j != "impar"
            and respuesta_j != "PAR"
            and respuesta_j != "IMPAR"
            and respuesta_j != "Par"
            and respuesta_j != "Impar"
        ):
            print("Caracteres incorrectos. Ingresar: par o impar.")
            respuesta_j = input(f"\n{juego4_nombre}. Par o impar?: \n")

        print(f"\nLa suma fue: {suma_caras}")
        # hasta acá.

        if suma_caras % 2 == 0:
            resultado_caras = "par"
        else:
            resultado_caras = "impar"

        if respuesta_j == resultado_caras:

            juego4_ganadas = juego4_ganadas + 1

            print("\nGanaste!")
            print(f"\nHistorial de victorias: {juego4_ganadas}\n")

        else:
            print("Perdiste!\n")
            juego4_perdidas += 1
        juego4_jugadas += 1
        continuar = input(f"{juego4_nombre}. Queres seguir jugando?: (si/no) ")
        while (
            continuar != "si"
            and continuar != "Si"
            and continuar != "SI"
            and continuar != "sI"
            and continuar != "no"
            and continuar != "No"
            and continuar != "NO"
            and continuar != "nO"
        ):
            continuar = input(
                f"Respuesta inválida, {juego4_nombre}. Queres seguir jugando?: (si/no) "
            )
        if (
            continuar == "no"
            or continuar == "No"
            or continuar == "NO"
            or continuar == "nO"
        ):
            print("\nEsperamos volver a verte pronto!\n")


def reporte():
    limpiarPantalla()
    print("")
    print("--------------------------------------------------------")
    print("")
    print(MAGENTA + "Reporte de puntuaciones:" + RESET)
    print("")
    print("Juego 1: Mayor-menor")
    print(f"Nombre del jugador: {juego1_nombre}")
    print(f"Partidas jugadas: {juego1_jugadas}")
    print(f"{GREEN}Mayor racha: {juego1_mayor_racha}{RESET}")
    print("")
    print("Juego 2: Número secreto")
    print(f"Nombre del jugador: {juego2_nombre}")
    print(f"Partidas jugadas: {juego2_jugadas}")
    print(f"{GREEN}Partidas ganadas: {juego2_ganadas}{RESET}")
    print(f"{RED}Partidas perdidas: {juego2_perdidas}{RESET}")
    print("")
    print("Juego 3: Blackjack")
    print("Juego en construcción")
    print("")
    print("Juego 4: Par o impar")
    print(f"Nombre del jugador: {juego4_nombre}")
    print(f"Partidas jugadas: {juego4_jugadas}")
    print(f"{GREEN}Partidas ganadas: {juego4_ganadas}{RESET}")
    print(f"{RED}Partidas perdidas: {juego4_perdidas}{RESET}")
    print("")
    print("")
    print("--------------------------------------------------------")
    print("")
    input("Presione Enter para salir\n")
    limpiarPantalla()


def salir():
    limpiarPantalla()
    print("")
    print("--------------------------------------------------------")
    print("")
    print("  Gracias por jugar. No apueste, " + GREEN + "juegue por diversión" + RESET)
    print("")
    print("--------------------------------------------------------")
    print("")
    input("Presione Enter para salir\n")
    limpiarPantalla()


# Declaración de variables

# STRING:
# comandoLimpiar, opcion, juego1_nombre, juego2_nombre, juego4_nombre

# BOOL:
# continuar, opcionEsValida, flagAdvertencia

# INT:
# juego1_jugadas, juego1_mayor_racha, juego2_jugadas, juego2_ganadas, juego2_perdidas,
# juego4_jugadas, juego4_ganadas, juego4_perdidas

comandoLimpiar = "cls" if os.name == "nt" else "clear"
continuar = True
opcion = ""
opcionEsValida = False
flagAdvertencia = False

# Definición de variables de puntuacion globales para los juegos
juego1_nombre = ""
juego1_jugadas = 0
juego1_mayor_racha = 0

juego2_nombre = ""
juego2_jugadas = 0
juego2_ganadas = 0
juego2_perdidas = 0

juego4_nombre = ""
juego4_jugadas = 0
juego4_ganadas = 0
juego4_perdidas = 0

# Ejecución del programa

cartelInicio()

while continuar:
    while not opcionEsValida:
        menu()
        if not flagAdvertencia:
            print("")
        else:
            print(RED + "Seleccione una opción válida" + RESET)
        opcion = input("Elija una opción: ")
        if "A" <= opcion <= "F" or "a" <= opcion <= "f":
            opcionEsValida = True
        else:
            flagAdvertencia = True
    match opcion:
        case "A" | "a":
            juego1()
        case "B" | "b":
            juego2()
        case "C" | "c":
            juego3()
        case "D" | "d":
            juego4()
        case "E" | "e":
            reporte()
        case "F" | "f":
            salir()
            continuar = False
    opcion = ""
    opcionEsValida = False
    flagAdvertencia = False
