# AyED 2026 - TP 2 - ISI 111
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
YELLOW = "\033[33m"
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
    nombre = input("Ingresá tu nombre: ")
    print(f"¡Hola {nombre}! Vamos a jugar al Menor-Mayor.")
    print("Te muestro un numero y tenés que adivinar si el siguiente es Mayor o Menor")

    numeroActual = random.randint(1, 1000)
    print(f"Número actual: {numeroActual}")
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
                print("Por favor ingrese sólo 'mayor' o 'menor'")
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
                + f"¡Acertaste! El número era {numeroSiguiente}\nRacha: {racha}"
                + RESET
            )
        else:
            print(RED + f"¡Le erraste! El número era {numeroSiguiente}" + RESET)

            print(f"\n{nombre}, ¿Querés seguir jugando?")
            continuar = input(
                "Ingresá 'si' para seguir jugando o 'no' para volver al menú: "
            )

            while (
                continuar != "si"
                and continuar != "no"
                and continuar != "Si"
                and continuar != "No"
            ):
                print("Por favor ingrese sólo 'si' o 'no'")
                continuar = input(
                    "Ingresa 'si' para seguir jugando o 'no' para volver al menú: "
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
            print(f"Nuevo número: {numeroActual}\n")

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
            Respuesta = input("Por favor ingresá 's' o 'n': ")

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
    # continuar, respuesta_j, resultado_caras, apuesta_str, nombre_ingresado
    # INT:
    # caraUno, caraDos, suma_caras, apuesta, i, indice_jugador
    limpiarPantalla()
    global juego4_nombres
    global juego4_jugadas_arr
    global juego4_ganadas_arr
    global juego4_perdidas_arr
    global juego4_creditos_arr  # para los créditps.
    global juego4_cant_jugadores  # para saber cantidad de jugadores.

    nombre_ingresado = input("Jugador/a, ingrese su nombre: \n")

    indice_jugador = -1
    i = 0
    while i < juego4_cant_jugadores:
        if juego4_nombres[i] == nombre_ingresado:
            indice_jugador = i
            i = juego4_cant_jugadores
        i += 1

    if indice_jugador == -1:
        if juego4_cant_jugadores >= maximo_j:
            print(
                f"\nLo sentimos, {nombre_ingresado}. No hay cupos disponibles (máximo {maximo_j} jugadores)."
            )
            input("\nPresione Enter para volver al menú\n")
            return
        else:
            indice_jugador = juego4_cant_jugadores
            juego4_nombres[indice_jugador] = nombre_ingresado
            juego4_creditos_arr[indice_jugador] = 1000
            juego4_jugadas_arr[indice_jugador] = 0
            juego4_ganadas_arr[indice_jugador] = 0
            juego4_perdidas_arr[indice_jugador] = 0
            juego4_cant_jugadores += 1
            print(f"\n¡Bienvenido/a, {nombre_ingresado}! Sos un jugador nuevo.")
    else:
        print(f"\n¡Hola de nuevo, {nombre_ingresado}!")

        if juego4_creditos_arr[indice_jugador] <= 0:
            print(
                "Tus créditos estaban en $0. Se reinician a $1000 para que puedas seguir jugando."
            )
            juego4_creditos_arr[indice_jugador] = 1000

    print(f"\n{nombre_ingresado}, sumaremos dos numeros entre 1 y 6.")
    print("Si el resultado es par, usted ganará y sumará un punto.")
    print("De lo contrario perderá y no sumará puntos.")
    print(f"\nCréditos actuales: {juego4_creditos_arr[indice_jugador]}$")
    print(
        "En cada ronda deberás apostar una suma menor o igual a tus créditos disponibles."
    )
    print(
        "Si acertás, ganás el monto apostado. Si fallás, se te resta el monto apostado."
    )

    continuar = "si"
    while (
        continuar == "si" or continuar == "Si" or continuar == "SI" or continuar == "sI"
    ):

        print(f"\nCréditos disponibles: {juego4_creditos_arr[indice_jugador]}$")

        apuesta_str = input(f"{nombre_ingresado}. ¿Cuánto querés apostar?: \n")
        while (
            not apuesta_str.isdigit()
            or int(apuesta_str) <= 0
            or int(apuesta_str) > juego4_creditos_arr[indice_jugador]
        ):

            print(
                f"Apuesta inválida. Ingresá un número entero entre 1 y {juego4_creditos_arr[indice_jugador]}."
            )
            apuesta_str = input(f"{nombre_ingresado}. ¿Cuánto querés apostar?: \n")

        apuesta = int(apuesta_str)

        caraUno = random.randint(1, 6)
        caraDos = random.randint(1, 6)
        suma_caras = caraUno + caraDos

        respuesta_j = input(f"\n{nombre_ingresado}. Par o impar?: \n")

        while (
            respuesta_j != "par"
            and respuesta_j != "impar"
            and respuesta_j != "PAR"
            and respuesta_j != "IMPAR"
            and respuesta_j != "Par"
            and respuesta_j != "Impar"
        ):
            print("Caracteres incorrectos. Ingresar: par o impar.")
            respuesta_j = input(f"\n{nombre_ingresado}. Par o impar?: \n")

        print(f"\nLa suma fue: {suma_caras}")

        if suma_caras % 2 == 0:
            resultado_caras = "par"
        else:
            resultado_caras = "impar"

        if respuesta_j == resultado_caras:

            juego4_ganadas_arr[indice_jugador] += 1
            juego4_creditos_arr[indice_jugador] += apuesta

            print("\n¡Ganaste!")
            print(
                f"Ganaste ${apuesta}. Créditos actuales: {juego4_creditos_arr[indice_jugador]}$"
            )
            print(f"Historial de aciertos: {juego4_ganadas_arr[indice_jugador]}\n")

        else:
            juego4_perdidas_arr[indice_jugador] += 1
            juego4_creditos_arr[indice_jugador] -= apuesta

            print("\n¡Perdiste!")
            print(
                f"Perdiste ${apuesta}. Créditos actuales: {juego4_creditos_arr[indice_jugador]}$\n"
            )

        juego4_jugadas_arr[indice_jugador] += 1

        if juego4_creditos_arr[indice_jugador] <= 0:
            print(f"{nombre_ingresado}, te quedaste sin créditos.")
            continuar = input(
                f"{nombre_ingresado}. Querés seguir jugando? Se reiniciarán tus créditos a $1000: (si/no) "
            )

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
                    f"Respuesta inválida, {nombre_ingresado}. Querés seguir jugando?: (si/no) "
                )

            if (
                continuar == "si"
                or continuar == "Si"
                or continuar == "SI"
                or continuar == "sI"
            ):
                juego4_creditos_arr[indice_jugador] = 1000
                print(
                    f"\n¡Créditos reiniciados! Ahora tenés {juego4_creditos_arr[indice_jugador]}$.\n"
                )
            else:
                print("\nEsperamos volver a verte pronto!\n")
            continue

        continuar = input(f"{nombre_ingresado}. Querés seguir jugando?: (si/no) ")

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
                f"Respuesta inválida, {nombre_ingresado}. Querés seguir jugando?: (si/no) "
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
    if juego4_cant_jugadores == 0:
        print("Todavía no jugó nadie.")
    else:
        i = 0
        while i < juego4_cant_jugadores:
            print(f"\nJugador: {juego4_nombres[i]}")
            print(f"Partidas jugadas: {juego4_jugadas_arr[i]}")
            print(f"{GREEN}Aciertos: {juego4_ganadas_arr[i]}{RESET}")
            print(f"{RED}Partidas perdidas: {juego4_perdidas_arr[i]}{RESET}")
            print(f"Créditos actuales: {juego4_creditos_arr[i]}$")
            i += 1
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
# comandoLimpiar, opcion, juego1_nombre, juego2_nombre
# BOOL:
# continuar, opcionEsValida, flagAdvertencia
# INT:
# juego1_jugadas, juego1_mayor_racha, juego2_jugadas, juego2_ganadas, juego2_perdidas,
# MAX_JUGADORES, juego4_cant_jugadores
# ARRAYS (listas usadas como arrays de tamaño fijo):
# juego4_nombres, juego4_jugadas_arr, juego4_ganadas_arr, juego4_perdidas_arr, juego4_creditos_arr

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

maximo_j = 10
juego4_nombres = [""] * maximo_j
juego4_jugadas_arr = [0] * maximo_j
juego4_ganadas_arr = [0] * maximo_j
juego4_perdidas_arr = [0] * maximo_j
juego4_creditos_arr = [0] * maximo_j
juego4_cant_jugadores = 0

# Ejecución del programa

cartelInicio()

while opcion != "f" and opcion != "F":
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
    opcionEsValida = False
    flagAdvertencia = False

salir()
