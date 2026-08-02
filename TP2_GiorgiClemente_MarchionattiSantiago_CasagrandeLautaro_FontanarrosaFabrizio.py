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
BRIGHT_YELLOW = "\033[93m"
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
    # intentosRestantes, intentosRealizados, intento, numeroSecreto, indice
    # BOOL:
    # esValido, esNumerico
    # STRING:
    # nombre, respuesta, entrada
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

    respuesta = "s"
    while respuesta == "s":
        j2_jugadas[indice] = j2_jugadas[indice] + 1
        numeroSecreto = random.randint(1, 100)
        intentosRestantes = 6
        intentosRealizados = 0
        intento = 0

        while intentosRestantes > 0:
            if intentosRestantes > 1:
                print("Te quedan", intentosRestantes, "intentos.")
            elif intentosRestantes == 1:
                print("Te queda", intentosRestantes, "intento.")

            esValido = False
            while not esValido:
                entrada = input("Introduce tu intento (1-100): ")

                esNumerico = True
                if len(entrada) == 0:
                    esNumerico = False

                for caracter in entrada:
                    if not ("0" <= caracter <= "9"):
                        esNumerico = False

                if esNumerico:
                    intento = int(entrada)
                    if 1 <= intento <= 100:
                        esValido = True
                    else:
                        print(
                            "Número inválido. Por favor, introduce un número entre 1 y 100."
                        )
                else:
                    print("Por favor introduzca un número. Inténtalo de nuevo.")

            intentosRealizados = intentosRealizados + 1

            if intento == numeroSecreto:
                print(
                    "¡Felicidades",
                    nombre,
                    "has adivinado el número secreto! Lo has logrado en",
                    intentosRealizados,
                    "intentos.",
                )
                j2_ganadas[indice] = j2_ganadas[indice] + 1
                intentosRestantes = 0
            elif intento < numeroSecreto:
                print("El número secreto es mayor que", intento)
            else:
                print("El número secreto es menor que", intento)

            intentosRestantes = intentosRestantes - 1

        if intento != numeroSecreto:
            print("No te quedan intentos. El número secreto era", numeroSecreto)
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
        respuesta = input("¿Deseas jugar nuevamente? (s/n) ").lower()
        while respuesta != "s" and respuesta != "n":
            respuesta = input("Por favor ingresá 's' o 'n': ").lower()

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
    # carta (0-51): rango = carta % 13 (0="2", 1="3", ..., 8="10", 9="J", 10="Q", 11="K", 12="A")
    #               palo  = carta // 13 (0="Corazones", 1="Diamantes", 2="Tréboles", 3="Picas")
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
    # Pasa los ases de 11 a 1
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
                print(
                    RED + f"\n{sumaJugador} contra {sumaBanca}. Gana la banca." + RESET
                )
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
    # nombre, respuesta, continuar, apuestaStr, resultado
    # INT:
    # indice, apuesta, caraUno, caraDos, sumaCaras
    # BOOL:
    # esNumerica, apuestaValida
    global j4_cant
    limpiarPantalla()

    nombre = input("Jugador/a, ingrese su nombre: \n")

    indice = buscarJugador(j4_nombres, j4_cant, nombre)

    if indice == -1:
        if j4_cant >= MAX_JUGADORES:
            print(
                RED
                + f"\nLo sentimos, {nombre}. No hay cupos disponibles (máximo {MAX_JUGADORES} jugadores)."
                + RESET
            )
            input("\nPresione Enter para volver al menú\n")
            return
        indice = j4_cant
        j4_nombres[indice] = nombre
        j4_creditos[indice] = 1000
        j4_jugadas[indice] = 0
        j4_ganadas[indice] = 0
        j4_perdidas[indice] = 0
        j4_cant = j4_cant + 1
        print(f"\n¡Bienvenido/a, {nombre}! Sos un jugador nuevo.")
    else:
        print(f"\n¡Hola de nuevo, {nombre}!")
        # Según el enunciado, quien se queda en cero no puede seguir jugando
        if j4_creditos[indice] <= 0:
            print(RED + "Te quedaste sin créditos. No podés seguir jugando." + RESET)
            input("\nPresione Enter para volver al menú\n")
            return

    print(f"\n{nombre}, sumaremos dos números entre 1 y 6.")
    print("Si el resultado es par, usted ganará y sumará un punto.")
    print("De lo contrario perderá y no sumará puntos.")
    print(f"\nCréditos actuales: {j4_creditos[indice]}$")
    print(
        "En cada ronda deberás apostar una suma menor o igual a tus créditos disponibles."
    )
    print(
        "Si acertás, ganás el monto apostado. Si fallás, se te resta el monto apostado."
    )

    continuar = "si"
    while continuar == "si":

        print(f"\nCréditos disponibles: {j4_creditos[indice]}$")

        # Validación de la apuesta carácter por carácter: debe ser un
        # entero entre 1 y los créditos disponibles
        apuestaValida = False
        apuesta = 0
        while not apuestaValida:
            apuestaStr = input(f"{nombre}. ¿Cuánto querés apostar?: \n")
            esNumerica = True
            if len(apuestaStr) == 0:
                esNumerica = False
            for caracter in apuestaStr:
                if not ("0" <= caracter <= "9"):
                    esNumerica = False
            if esNumerica:
                apuesta = int(apuestaStr)
                if 1 <= apuesta <= j4_creditos[indice]:
                    apuestaValida = True
                else:
                    print(
                        f"Apuesta inválida. Ingresá un número entero entre 1 y {j4_creditos[indice]}."
                    )
            else:
                print("Por favor ingresá un número entero.")

        caraUno = random.randint(1, 6)
        caraDos = random.randint(1, 6)
        sumaCaras = caraUno + caraDos

        respuesta = input(f"\n{nombre}. ¿Par o impar?: \n").lower()
        while respuesta != "par" and respuesta != "impar":
            print("Respuesta inválida. Ingresá 'par' o 'impar'.")
            respuesta = input(f"\n{nombre}. ¿Par o impar?: \n").lower()

        print(f"\nLa suma fue: {sumaCaras}")

        if sumaCaras % 2 == 0:
            resultado = "par"
        else:
            resultado = "impar"

        if respuesta == resultado:
            j4_ganadas[indice] = j4_ganadas[indice] + 1
            j4_creditos[indice] = j4_creditos[indice] + apuesta

            print(GREEN + "\n¡Ganaste!" + RESET)
            print(f"Ganaste ${apuesta}. Créditos actuales: {j4_creditos[indice]}$")
            print(f"Historial de aciertos: {j4_ganadas[indice]}\n")
        else:
            j4_perdidas[indice] = j4_perdidas[indice] + 1
            j4_creditos[indice] = j4_creditos[indice] - apuesta

            print(RED + "\n¡Perdiste!" + RESET)
            print(f"Perdiste ${apuesta}. Créditos actuales: {j4_creditos[indice]}$\n")

        j4_jugadas[indice] = j4_jugadas[indice] + 1

        if j4_creditos[indice] <= 0:
            # Según el enunciado, quien se queda en cero no puede seguir jugando
            print(
                RED
                + f"{nombre}, te quedaste sin créditos. No podés seguir jugando."
                + RESET
            )
            continuar = "no"
        else:
            continuar = input(f"{nombre}. ¿Querés seguir jugando? (si/no): ").lower()
            while continuar != "si" and continuar != "no":
                continuar = input(
                    f"Respuesta inválida, {nombre}. ¿Querés seguir jugando? (si/no): "
                ).lower()
            if continuar == "no":
                print("\n¡Esperamos volver a verte pronto!\n")

    input("\nPresione Enter para volver al menú\n")


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


def burbujaAsc(nombres, valores, cant):
    # Ordena de menor a mayor según valores, moviendo los nombres
    # junto con ellos (método burbuja sobre arrays paralelos)
    # INT:
    # i, j, auxValor
    # STRING:
    # auxNombre
    for i in range(cant - 1):
        for j in range(cant - 1 - i):
            if valores[j] > valores[j + 1]:
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
    if j4_cant == 0:
        print("  Todavía no hay jugadores registrados.")
    else:
        nombresAux = [""] * MAX_JUGADORES
        valoresAux = [0] * MAX_JUGADORES
        for i in range(j4_cant):
            nombresAux[i] = j4_nombres[i]
            valoresAux[i] = j4_ganadas[i]
        burbujaDesc(nombresAux, valoresAux, j4_cant)
        for i in range(j4_cant):
            print(f"  {nombresAux[i]}: {valoresAux[i]} ganadas")

    input("\nPresione Enter para continuar\n")


def reporteJuegosPorJugador():
    # Opción b: dado un nombre, informar a qué juegos jugó y
    # cuántos puntos obtuvo en cada uno
    # STRING:
    # nombre
    # BOOL:
    # encontro
    # INT:
    # i1, i2, i3, i4
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

    i4 = buscarJugador(j4_nombres, j4_cant, nombre)
    if i4 != -1:
        encontro = True
        print(
            f"Par o impar: {j4_ganadas[i4]} aciertos"
            + f" ({j4_jugadas[i4]} jugadas, {j4_perdidas[i4]} perdidas)."
        )

    if not encontro:
        print(f"{nombre} no está registrado en ningún juego.")

    input("\nPresione Enter para continuar\n")


def reporteCreditos():
    # Opción c: jugadores de Par-Impar ordenados de menor a mayor
    # según su crédito
    # INT:
    # i
    limpiarPantalla()
    print(
        MAGENTA + "Jugadores de Par-Impar ordenados por crédito (menor a mayor)" + RESET
    )
    if j4_cant == 0:
        print("  Todavía no hay jugadores registrados.")
    else:
        nombresAux = [""] * MAX_JUGADORES
        valoresAux = [0] * MAX_JUGADORES
        for i in range(j4_cant):
            nombresAux[i] = j4_nombres[i]
            valoresAux[i] = j4_creditos[i]
        burbujaAsc(nombresAux, valoresAux, j4_cant)
        for i in range(j4_cant):
            print(f"  {nombresAux[i]}: ${valoresAux[i]}")
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
        print(
            GREEN + "A" + RESET + " - Jugadores ordenados por victorias (mayor a menor)"
        )
        print(GREEN + "B" + RESET + " - Juegos jugados por un jugador")
        print(GREEN + "C" + RESET + " - Jugadores de Par-Impar ordenados por crédito")
        print(GREEN + "D" + RESET + " - Racha de un jugador en el Menor-Mayor")
        print(RED + "E" + RESET + " - Volver al menú principal")
        print("")
        opcionReporte = input("Elija una opción: ").lower()
        while len(opcionReporte) != 1 or opcionReporte < "a" or opcionReporte > "e":
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
# comandoLimpiar, opcion
# BOOL:
# opcionEsValida, flagAdvertencia
# INT:
# MAX_JUGADORES, j1_cant, j2_cant, j3_cant, j4_cant
# ARRAYS SIMULADOS (longitud fija MAX_JUGADORES, un solo tipo de dato,
# sin métodos de lista; la cantidad de posiciones ocupadas la lleva jX_cant):
# j1_nombres (str), j1_rachaMax (int)
# j2_nombres (str), j2_jugadas, j2_ganadas, j2_perdidas (int)
# j3_nombres (str), j3_ganadas (int)
# j4_nombres (str), j4_jugadas, j4_ganadas, j4_perdidas, j4_creditos (int)

comandoLimpiar = "cls" if os.name == "nt" else "clear"
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

j4_nombres = [""] * MAX_JUGADORES
j4_jugadas = [0] * MAX_JUGADORES
j4_ganadas = [0] * MAX_JUGADORES
j4_perdidas = [0] * MAX_JUGADORES
j4_creditos = [0] * MAX_JUGADORES
j4_cant = 0

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
        if len(opcion) == 1 and "a" <= opcion <= "f":
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
