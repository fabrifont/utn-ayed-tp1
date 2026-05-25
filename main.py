# TODO:

# Juego 1: corregir que no pregunte si querés volver a jugar y te mande al menú directamente
# Sacar .strip.tolower, no se permiten los métodos de manejo de strings. Revisar validación

# Juego 4: corregir que no vailde inputs y tome cualquier cosa, se debería manejar sólo con
# opciones como 1 y 2

# AyED 2026 - TP 1 - ISI 111
# Integrantes:
# - Fabrizio Fontanarrosa
# - Clemente Giorgi
# - Santiago Marchionatti
# - Lautaro Casagrande

# Bibliotecas

from colores import *
import os
import random

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


def juego1():
    """juego del menor - mayor"""
    limpiarPantalla()
    nombre = input("Ingresá tu nombre: ")
    print(f"¡Hola {nombre}! Vamos a jugar al menor-mayor.")
    print("Te muestro un número y tenés que adivinar si el siguiente es mayor o menor")

    numeroActual = random.randint(1, 1000)
    print(f"Número actual: {numeroActual}")
    racha = 0
    juegoTerminado = False

    while not juegoTerminado:
        prediccion = input("¿Mayor o menor? ").strip().lower()

        prediccionValida = False
        while not prediccionValida:
            if prediccion == "mayor" or prediccion == "menor":
                prediccionValida = True
            else:
                print("Por favor ingrese sólo 'mayor' o 'menor'")
                prediccion = input("¿MAYOR o MENOR? ").strip().lower()

        numeroSiguiente = random.randint(1, 1000)

        acierto = False
        if (prediccion == "mayor" and numeroSiguiente > numeroActual) or (
            prediccion == "menor" and numeroSiguiente < numeroActual
        ):
            racha += 1
            print(GREEN + f"¡Le diste capo! Racha: {racha}" + RESET)
            acierto = True

        if not acierto:
            print(
                RED
                + f"¡Le erraste como los mejores! El número era {numeroSiguiente}"
                + RESET
            )
            print(f"¡Juego terminado {nombre}! La racha final fue de {racha} aciertos.")
            input("\nPresione Enter para volver")
            juegoTerminado = True

        numeroActual = numeroSiguiente
        if not juegoTerminado:
            print(f"nuevo número: {numeroActual}\n")


def juego2():
    "Declaración de variables"
    "IntentosRestantes, IntentosRealizados, VecesJugadas, VecesAcertadas, VecesPerdidas, Intento, Entrada y numerosecreto: int(Enteros)"
    "es_valido: bool (Booleano)"
    "Respuesta: str (Cadena de caracteres)"
    limpiarPantalla()
    print("¡Bienvenido al juego del número secreto!")
    Nombredeljugador = input("¿Cuál es tu nombre? ")
    print("Hola", Nombredeljugador, "¡Vamos a jugar al número secreto!")
    print(
        "El juego consiste en adivinar un número entre 1 y 100. Tienes 6 intentos para adivinarlo. ¡Buena suerte!"
    )

    IntentosRestantes = 6
    IntentosRealizados = 0
    VecesJugadas = 0
    VecesAcertadas = 0
    VecesPerdidas = 0

    Respuesta = "s"
    while Respuesta == "s":
        VecesJugadas = VecesJugadas + 1
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
                    Nombredeljugador,
                    "has adivinado el número secreto! Lo has logrado en",
                    IntentosRealizados,
                    "intentos.",
                )
                VecesAcertadas = VecesAcertadas + 1
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
            VecesPerdidas = VecesPerdidas + 1

        print(
            "Has jugado",
            VecesJugadas,
            "veces, has acertado",
            VecesAcertadas,
            "veces y has perdido",
            VecesPerdidas,
            "veces.",
        )
        Respuesta = str(input("¿Deseas jugar nuevamente? (s/n) "))
        while Respuesta != "s" and Respuesta != "n":
            Respuesta = input("Por favor ingresa 's' o 'n': ")

    print("¡Gracias por jugar, hasta la próxima!")
    print(
        "Has jugado",
        VecesJugadas,
        "veces, has acertado",
        VecesAcertadas,
        "veces y has perdido",
        VecesPerdidas,
        "veces.",
    )


def juego3():
    limpiarPantalla()
    input("Juego en construcción. Volvé pronto!\n\nPresione Enter para volver\n")


def juego4():
    limpiarPantalla()
    nombre_j = input("Jugador/a, ingrese su nombre: \n")
    print(
        f"\n{nombre_j}, sumaremos dos numeros entre 1 y 6. \nSi el resultado es par, usted ganará y sumará un punto. De lo contrario perderá y no sumará puntos."
    )
    contadorhistorico = 0
    opcionContinuar = ""
    continuarJuego = True

    while continuarJuego:
        caraUno = random.randint(1, 6)
        caraDos = random.randint(1, 6)
        suma_caras = caraUno + caraDos
        respuesta_j = input(f"\n{nombre_j}. Par o impar?: \n")
        print(suma_caras)

        if suma_caras % 2 == 0:
            resultado_caras = "par"
        else:
            resultado_caras = "impar"

        if respuesta_j == resultado_caras:
            contadorhistorico = contadorhistorico + 1
            print("\nGanaste!")
            print(f"\nHistorial de victorias: {contadorhistorico}\n")
        else:
            print("Perdiste!\n")

        opcionContinuar = input(
            f"{nombre_j}. Queres seguir jugando?:\n1 - Sí\n2 - No\n"
        )
        while opcionContinuar != "1" and opcionContinuar != "2":
            print("Seleccione una opción válida")
            opcionContinuar = input(
                f"{nombre_j}. Queres seguir jugando?:\n1 - Sí\n2 - No\n"
            )

        continuarJuego = opcionContinuar == "1"

        if not continuarJuego:
            input("\nEsperamos volver a verte pronto!\nPresione Enter para volver\n")


def reporte():
    return


def salir():
    limpiarPantalla()
    print("")
    print("--------------------------------------------------------")
    print("")
    print("  Gracias por jugar. No apueste, juegue por diversión")
    print("")
    print("--------------------------------------------------------")
    print("")
    input("Presione Enter para salir\n")
    limpiarPantalla()


"""
Declaración de variables
sistemaOperativo, comandoLimpiar, opcion: string
continuar, opcionEsValida, flagAdvertencia: bool
"""

sistemaOperativo = os.name
comandoLimpiar = "cls" if sistemaOperativo == "nt" else "clear"
continuar = True
opcion = ""
opcionEsValida = False
flagAdvertencia = False

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
