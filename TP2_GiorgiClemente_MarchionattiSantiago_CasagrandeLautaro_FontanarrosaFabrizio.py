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


def buscarJugador(nombres, cant, nombre):
    # Búsqueda lineal sobre el array: devuelve el índice del jugador
    # o -1 si no está registrado
    # INT:
    # indice, i
    indice = -1
    i = 0
    while i < cant and indice == -1:
        if nombres[i] == nombre:
            indice = i
        i = i + 1
    return indice


# Juego del Menor - Mayor
def juego1():
    # Declaracion de variables:
    # STRING:
    # nombre, prediccion
    # BOOL:
    # acierto, juegoTerminado
    # INT:
    # numeroActual, numeroSiguiente, racha, indice
    global j1_cant
    limpiarPantalla()
    nombre = input("Ingresá tu nombre: ")

    indice = buscarJugador(j1_nombres, j1_cant, nombre)
    if indice == -1:
        if j1_cant >= MAX_JUGADORES:
            print(
                RED
                + "Ya hay 10 jugadores registrados. No hay cupo para un jugador nuevo."
                + RESET
            )
            input("Presione Enter para volver al menú\n")
            return
        j1_nombres[j1_cant] = nombre
        j1_rachaMax[j1_cant] = 0
        indice = j1_cant
        j1_cant = j1_cant + 1

    print(f"¡Hola {nombre}! Vamos a jugar al Menor-Mayor.")
    print("Te muestro un numero y tenés que adivinar si el siguiente es Mayor o Menor")

    numeroActual = random.randint(1, 1000)
    print(f"Número actual: {numeroActual}")
    racha = 0
    juegoTerminado = False

    while not juegoTerminado:
        prediccion = input("¿Mayor o Menor? ").lower()

        while prediccion != "mayor" and prediccion != "menor":
            print("Por favor ingrese sólo 'mayor' o 'menor'")
            prediccion = input("¿Mayor o Menor? ").lower()

        numeroSiguiente = random.randint(1, 1000)

        if numeroSiguiente == numeroActual:
            print(
                YELLOW
                + f"Salió el mismo número ({numeroSiguiente}). No suma para la racha, el juego continúa."
                + RESET
            )
        else:
            acierto = False
            if prediccion == "mayor" and numeroSiguiente > numeroActual:
                acierto = True
            elif prediccion == "menor" and numeroSiguiente < numeroActual:
                acierto = True

            if acierto:
                racha = racha + 1
                print(
                    GREEN
                    + f"¡Acertaste! El número era {numeroSiguiente}\nRacha: {racha}"
                    + RESET
                )
            else:
                print(RED + f"¡Le erraste! El número era {numeroSiguiente}" + RESET)
                print(f"¡Juego terminado {nombre}! Tu racha fue de {racha} aciertos.")
                juegoTerminado = True

        if not juegoTerminado:
            numeroActual = random.randint(1, 1000)
            print(f"Nuevo número: {numeroActual}\n")

    if racha > j1_rachaMax[indice]:
        j1_rachaMax[indice] = racha

    input("Presione Enter para volver al menú\n")


# Numero secreto
def juego2():
    # Declaración de variables
    # INT:
    # IntentosRestantes, IntentosRealizados, Intento, numerosecreto, indice
    # BOOL:
    # es_valido, es_numerico
    # STRING:
    # nombre, Respuesta, Entrada
    global j2_cant
    limpiarPantalla()
    print("¡Bienvenido al juego del número secreto!")
    nombre = input("¿Cuál es tu nombre? ")

    indice = buscarJugador(j2_nombres, j2_cant, nombre)
    if indice == -1:
        if j2_cant >= MAX_JUGADORES:
            print(RED + "El juego alcanzó su máximo de jugadores." + RESET)
            input("Presione Enter para volver al menú\n")
            return
        j2_nombres[j2_cant] = nombre
        j2_jugadas[j2_cant] = 0
        j2_ganadas[j2_cant] = 0
        j2_perdidas[j2_cant] = 0
        indice = j2_cant
        j2_cant = j2_cant + 1

    print("Hola", nombre, "¡Vamos a jugar al número secreto!")
    print(
        "El juego consiste en adivinar un número entre 1 y 100. Tienes 6 intentos para adivinarlo. ¡Buena suerte!"
    )

    Respuesta = "s"
    while Respuesta == "s":
        j2_jugadas[indice] = j2_jugadas[indice] + 1
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
                    nombre,
                    "has adivinado el número secreto! Lo has logrado en",
                    IntentosRealizados,
                    "intentos.",
                )
                j2_ganadas[indice] = j2_ganadas[indice] + 1
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
            j2_perdidas[indice] = j2_perdidas[indice] + 1

        print(
            "Has jugado",
            j2_jugadas[indice],
            "veces, has acertado",
            j2_ganadas[indice],
            "veces y has perdido",
            j2_perdidas[indice],
            "veces.",
        )
        Respuesta = input("¿Deseas jugar nuevamente? (s/n) ").lower()
        while Respuesta != "s" and Respuesta != "n":
            Respuesta = input("Por favor ingresá 's' o 'n': ").lower()

    print("\n¡Gracias por jugar, hasta la próxima!")
    print(
        "Has jugado",
        j2_jugadas[indice],
        "veces, has acertado",
        j2_ganadas[indice],
        "veces y has perdido",
        j2_perdidas[indice],
        "veces.",
    )

    input("\nPresione Enter para volver\n")


# Blackjack
def textoCarta(carta):
    # INT:
    # carta (0-51): rango = carta % 13 (0=2 ... 8=10, 9=J, 10=Q, 11=K, 12=A)
    #               palo  = carta // 13 (0=Corazones, 1=Diamantes, 2=Tréboles, 3=Picas)
    rangos = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    palos = ["Corazones", "Diamantes", "Tréboles", "Picas"]
    return rangos[carta % 13] + " de " + palos[carta // 13]


def valorMano(mano, cant):
    # Suma los valores de las cartas: 2-10 su número, J/Q/K valen 10,
    # el As vale 11 y pasa a valer 1 si la suma se pasa de 21
    # INT:
    # suma, ases, i, rango
    suma = 0
    ases = 0
    for i in range(cant):
        rango = mano[i] % 13
        if rango <= 8:
            suma = suma + rango + 2
        elif rango <= 11:
            suma = suma + 10
        else:
            suma = suma + 11
            ases = ases + 1
    while suma > 21 and ases > 0:
        suma = suma - 10
        ases = ases - 1
    return suma


def mostrarMano(mano, cant):
    # INT:
    # i
    for i in range(cant):
        print("  " + textoCarta(mano[i]))


def juego3():
    # Declaración de variables
    # STRING:
    # nombre, decision, otraPartida
    # BOOL:
    # turnoJugador
    # INT:
    # indice, tope, cantJugador, cantBanca, sumaJugador, sumaBanca, i, j, aux
    global j3_cant
    limpiarPantalla()
    print("¡Bienvenido al Blackjack!")
    nombre = input("Ingresá tu nombre: ")

    indice = buscarJugador(j3_nombres, j3_cant, nombre)
    if indice == -1:
        if j3_cant >= MAX_JUGADORES:
            print(
                RED
                + "Ya hay 10 jugadores registrados. No hay cupo para un jugador nuevo."
                + RESET
            )
            input("Presione Enter para volver al menú\n")
            return
        j3_nombres[j3_cant] = nombre
        j3_ganadas[j3_cant] = 0
        indice = j3_cant
        j3_cant = j3_cant + 1

    print(
        f"\n¡Hola {nombre}! Jugás contra la banca. Gana el que se acerque más a 21 sin pasarse."
    )

    otraPartida = "si"
    while otraPartida == "si":
        # Se crea y baraja un mazo nuevo de 52 cartas en cada partida
        mazo = [0] * 52
        for i in range(52):
            mazo[i] = i
        for i in range(51, 0, -1):
            j = random.randint(0, i)
            aux = mazo[i]
            mazo[i] = mazo[j]
            mazo[j] = aux
        tope = 0

        manoJugador = [0] * 12
        cantJugador = 0
        manoBanca = [0] * 12
        cantBanca = 0

        # Reparto inicial: dos cartas para el jugador y dos para la banca
        manoJugador[cantJugador] = mazo[tope]
        cantJugador = cantJugador + 1
        tope = tope + 1
        manoBanca[cantBanca] = mazo[tope]
        cantBanca = cantBanca + 1
        tope = tope + 1
        manoJugador[cantJugador] = mazo[tope]
        cantJugador = cantJugador + 1
        tope = tope + 1
        manoBanca[cantBanca] = mazo[tope]
        cantBanca = cantBanca + 1
        tope = tope + 1

        print("\nCartas de la banca:")
        mostrarMano(manoBanca, cantBanca)
        sumaBanca = valorMano(manoBanca, cantBanca)
        print("Suma de la banca:", sumaBanca)
        print("\nTus cartas:")
        mostrarMano(manoJugador, cantJugador)
        sumaJugador = valorMano(manoJugador, cantJugador)
        print("Tu suma:", sumaJugador)

        # Turno del jugador
        turnoJugador = True
        while turnoJugador:
            if sumaJugador >= 21:
                turnoJugador = False
            else:
                decision = input("\n¿Pedir o Plantarse? ").lower()
                while decision != "pedir" and decision != "plantarse":
                    print("Opción inválida. Ingresá 'pedir' o 'plantarse'.")
                    decision = input("¿Pedir o Plantarse? ").lower()
                if decision == "plantarse":
                    turnoJugador = False
                else:
                    manoJugador[cantJugador] = mazo[tope]
                    cantJugador = cantJugador + 1
                    tope = tope + 1
                    sumaJugador = valorMano(manoJugador, cantJugador)
                    print("Recibiste:", textoCarta(manoJugador[cantJugador - 1]))
                    print("Tu suma:", sumaJugador)

        if sumaJugador > 21:
            print(RED + "\nTe pasaste de 21. ¡Gana la banca!" + RESET)
        else:
            # Turno de la banca: pide con 16 o menos, se planta con 17 o más
            print("\nTurno de la banca. Su suma:", sumaBanca)
            while sumaBanca <= 16:
                manoBanca[cantBanca] = mazo[tope]
                cantBanca = cantBanca + 1
                tope = tope + 1
                sumaBanca = valorMano(manoBanca, cantBanca)
                print(
                    "La banca pide carta:",
                    textoCarta(manoBanca[cantBanca - 1]),
                    "- Suma:",
                    sumaBanca,
                )
            print("La banca se planta con", sumaBanca)

            if sumaBanca > 21:
                print(GREEN + "\nLa banca se pasó de 21. ¡Ganaste!" + RESET)
                j3_ganadas[indice] = j3_ganadas[indice] + 1
            elif sumaJugador > sumaBanca:
                print(GREEN + f"\n{sumaJugador} contra {sumaBanca}. ¡Ganaste!" + RESET)
                j3_ganadas[indice] = j3_ganadas[indice] + 1
            elif sumaJugador < sumaBanca:
                print(RED + f"\n{sumaJugador} contra {sumaBanca}. Gana la banca." + RESET)
            else:
                print(YELLOW + f"\n{sumaJugador} contra {sumaBanca}. ¡Empate!" + RESET)

        print(f"\n{nombre}, ganaste {j3_ganadas[indice]} partidas en total.")
        otraPartida = input("¿Querés jugar otra partida? (si/no): ").lower()
        while otraPartida != "si" and otraPartida != "no":
            print("Por favor ingresá 'si' o 'no'.")
            otraPartida = input("¿Querés jugar otra partida? (si/no): ").lower()

    input("\nPresione Enter para volver al menú\n")


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
    print("Si el resultado es par, usted ganará y sumará un punto.")
    print("De lo contrario perderá y no sumará puntos.")

    continuar = "si"
    while continuar == "si":

        caraUno = random.randint(1, 6)
        caraDos = random.randint(1, 6)
        suma_caras = caraUno + caraDos

        respuesta_j = input(f"\n{juego4_nombre}. Par o impar?: \n").lower()

        while respuesta_j != "par" and respuesta_j != "impar":
            print("Caracteres incorrectos. Ingresar: par o impar.")
            respuesta_j = input(f"\n{juego4_nombre}. Par o impar?: \n").lower()

        print(f"\nLa suma fue: {suma_caras}")

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
        continuar = input(f"{juego4_nombre}. Querés seguir jugando?: (si/no) ").lower()
        while continuar != "si" and continuar != "no":
            continuar = input(
                f"Respuesta inválida, {juego4_nombre}. Querés seguir jugando?: (si/no) "
            ).lower()
        if continuar == "no":
            print("\nEsperamos volver a verte pronto!\n")


# Reporte
def burbujaDesc(nombres, valores, cant):
    # Ordena de mayor a menor según valores, moviendo los nombres
    # junto con ellos (método burbuja sobre arrays paralelos)
    # INT:
    # i, j, auxValor
    # STRING:
    # auxNombre
    for i in range(cant - 1):
        for j in range(cant - 1 - i):
            if valores[j] < valores[j + 1]:
                auxValor = valores[j]
                valores[j] = valores[j + 1]
                valores[j + 1] = auxValor
                auxNombre = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = auxNombre


def reporteGanadores():
    # Opción a: jugadores ordenados de mayor a menor por cantidad
    # de veces que ganaron cada juego (excepto menor/mayor)
    # INT:
    # i
    limpiarPantalla()
    print(MAGENTA + "Jugadores ordenados por victorias (mayor a menor)" + RESET)

    print("\n" + CYAN + "Número secreto" + RESET)
    if j2_cant == 0:
        print("  Todavía no hay jugadores registrados.")
    else:
        nombresAux = [""] * MAX_JUGADORES
        valoresAux = [0] * MAX_JUGADORES
        for i in range(j2_cant):
            nombresAux[i] = j2_nombres[i]
            valoresAux[i] = j2_ganadas[i]
        burbujaDesc(nombresAux, valoresAux, j2_cant)
        for i in range(j2_cant):
            print(f"  {nombresAux[i]}: {valoresAux[i]} ganadas")

    print("\n" + CYAN + "Blackjack" + RESET)
    if j3_cant == 0:
        print("  Todavía no hay jugadores registrados.")
    else:
        nombresAux = [""] * MAX_JUGADORES
        valoresAux = [0] * MAX_JUGADORES
        for i in range(j3_cant):
            nombresAux[i] = j3_nombres[i]
            valoresAux[i] = j3_ganadas[i]
        burbujaDesc(nombresAux, valoresAux, j3_cant)
        for i in range(j3_cant):
            print(f"  {nombresAux[i]}: {valoresAux[i]} ganadas")

    print("\n" + CYAN + "Par o impar" + RESET)
    print("  Pendiente: se implementará junto con la refactorización del juego 4.")

    input("\nPresione Enter para continuar\n")


def reporteJuegosPorJugador():
    # Opción b: dado un nombre, informar a qué juegos jugó y
    # cuántos puntos obtuvo en cada uno
    # STRING:
    # nombre
    # BOOL:
    # encontro
    # INT:
    # i1, i2, i3
    limpiarPantalla()
    nombre = input("Ingresá el nombre del jugador: ")
    encontro = False

    i1 = buscarJugador(j1_nombres, j1_cant, nombre)
    if i1 != -1:
        encontro = True
        print(f"Menor-Mayor: su mejor racha es de {j1_rachaMax[i1]} aciertos.")

    i2 = buscarJugador(j2_nombres, j2_cant, nombre)
    if i2 != -1:
        encontro = True
        print(
            f"Número secreto: {j2_ganadas[i2]} ganadas"
            + f" ({j2_jugadas[i2]} jugadas, {j2_perdidas[i2]} perdidas)."
        )

    i3 = buscarJugador(j3_nombres, j3_cant, nombre)
    if i3 != -1:
        encontro = True
        print(f"Blackjack: {j3_ganadas[i3]} partidas ganadas.")

    if not encontro:
        print(f"{nombre} no está registrado en ningún juego.")

    print("Par o impar: pendiente de implementar junto con el juego 4.")
    input("\nPresione Enter para continuar\n")


def reporteCreditos():
    # Opción c: jugadores de Par-Impar ordenados de menor a mayor
    # según su crédito
    limpiarPantalla()
    print("Listado de jugadores de Par-Impar ordenado por crédito:")
    print("Pendiente: se implementará junto con el sistema de crédito del juego 4.")
    input("\nPresione Enter para continuar\n")


def reporteRacha():
    # Opción d: dado un nombre, mostrar su racha en el juego
    # de menor/mayor
    # STRING:
    # nombre
    # INT:
    # i1
    limpiarPantalla()
    nombre = input("Ingresá el nombre del jugador: ")
    i1 = buscarJugador(j1_nombres, j1_cant, nombre)
    if i1 == -1:
        print(f"{nombre} no está registrado en el juego del Menor-Mayor.")
    else:
        print(
            f"La mejor racha de {nombre} en el Menor-Mayor es de {j1_rachaMax[i1]} aciertos."
        )
    input("\nPresione Enter para continuar\n")


def reporte():
    # Submenú iterativo del reporte
    # STRING:
    # opcionReporte
    opcionReporte = ""
    while opcionReporte != "e":
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
            + MAGENTA
            + "REPORTE"
            + RESET
        )
        print("")
        print("Lista de opciones:")
        print(GREEN + "A" + RESET + " - Jugadores ordenados por victorias (mayor a menor)")
        print(GREEN + "B" + RESET + " - Juegos jugados por un jugador")
        print(GREEN + "C" + RESET + " - Jugadores de Par-Impar ordenados por crédito")
        print(GREEN + "D" + RESET + " - Racha de un jugador en el Menor-Mayor")
        print(RED + "E" + RESET + " - Volver al menú principal")
        print("")
        opcionReporte = input("Elija una opción: ").lower()
        while opcionReporte < "a" or opcionReporte > "e":
            print(RED + "Seleccione una opción válida" + RESET)
            opcionReporte = input("Elija una opción: ").lower()
        if opcionReporte == "a":
            reporteGanadores()
        elif opcionReporte == "b":
            reporteJuegosPorJugador()
        elif opcionReporte == "c":
            reporteCreditos()
        elif opcionReporte == "d":
            reporteRacha()


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
# comandoLimpiar, opcion, juego4_nombre
# BOOL:
# continuar, opcionEsValida, flagAdvertencia
# INT:
# MAX_JUGADORES, j1_cant, j2_cant, j3_cant,
# juego4_jugadas, juego4_ganadas, juego4_perdidas
# ARRAYS SIMULADOS (longitud fija MAX_JUGADORES, un solo tipo de dato,
# sin métodos de lista; la cantidad de posiciones ocupadas la lleva jX_cant):
# j1_nombres (str), j1_rachaMax (int)
# j2_nombres (str), j2_jugadas, j2_ganadas, j2_perdidas (int)
# j3_nombres (str), j3_ganadas (int)

comandoLimpiar = "cls" if os.name == "nt" else "clear"
continuar = True
opcion = ""
opcionEsValida = False
flagAdvertencia = False

# Definición de variables de puntuacion globales para los juegos

MAX_JUGADORES = 10

j1_nombres = [""] * MAX_JUGADORES
j1_rachaMax = [0] * MAX_JUGADORES
j1_cant = 0

j2_nombres = [""] * MAX_JUGADORES
j2_jugadas = [0] * MAX_JUGADORES
j2_ganadas = [0] * MAX_JUGADORES
j2_perdidas = [0] * MAX_JUGADORES
j2_cant = 0

j3_nombres = [""] * MAX_JUGADORES
j3_ganadas = [0] * MAX_JUGADORES
j3_cant = 0

juego4_nombre = ""
juego4_jugadas = 0
juego4_ganadas = 0
juego4_perdidas = 0

# Ejecución del programa

cartelInicio()

while opcion != "f":
    while not opcionEsValida:
        menu()
        if not flagAdvertencia:
            print("")
        else:
            print(RED + "Seleccione una opción válida" + RESET)
        opcion = input("Elija una opción: ").lower()
        if "a" <= opcion <= "f":
            opcionEsValida = True
        else:
            flagAdvertencia = True
    match opcion:
        case "a":
            juego1()
        case "b":
            juego2()
        case "c":
            juego3()
        case "d":
            juego4()
        case "e":
            reporte()
    opcionEsValida = False
    flagAdvertencia = False

salir()
