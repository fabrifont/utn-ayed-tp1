
# TODO: Revisar lógica general del sistema, hacer algún diagrama de flujo para ver cómo 
# acomodamos la ejecución de las funciones (while's, condicionales). Recordar que no se
# permite el uso de break ni return vacío dentro de bucles ni exit

# AyED 2026 - TP 1 - ISI 111
# Integrantes:
# - Fabrizio Fontanarrosa
# - Clemente Giorgi
# - Santiago Marchionatti
# - Lautaro Casagrande

# Bibliotecas

from colores import *
import os

# Definición de funciones

def limpiarPantalla():
    os.system(comandoLimpiar)

def cartelInicio():
    limpiarPantalla()
    print("")
    print("----------------------------------------------------------------------------------------------------------")
    print("")
    print("Los juegos de apuestas están" + RED + " prohibidos " + RESET + "para los menores de 18 años, y son" + RED + " perjudiciales " + RESET + "para la salud.")
    print("")
    print("Juegue por diversión. Juegue con responsabilidad.")
    print("")
    print("----------------------------------------------------------------------------------------------------------")
    print("")
    print("")
    input("Presione Enter para continuar\n")

def menu():
    limpiarPantalla()
    print("")
    print("")
    print(BLUE + "PYTHON " + BRIGHT_YELLOW + "CASINO" + RESET + " - " + GREEN + "MENÚ PRINCIPAL" + RESET)
    print("")
    print("Lista de opciones:")
    print(GREEN + "A" + RESET + " - Juego del menor-mayor")
    print(GREEN + "B" + RESET + " - Número secreto")
    print(GREEN + "C" + RESET + " - Blackjack")
    print(GREEN + "D" + RESET + " - Par o impar")
    print(MAGENTA + "E" + RESET + " - Reporte")
    print(RED + "F" + RESET + " - Salir")
    print("")

def validarOpcion(opcionIngresada):
    return opcionIngresada == "A" or opcionIngresada == "B" or opcionIngresada == "C" or opcionIngresada == "D" or opcionIngresada == "E" or opcionIngresada == "F" or opcionIngresada == "a" or opcionIngresada == "b" or opcionIngresada == "c" or opcionIngresada == "d" or opcionIngresada == "e" or opcionIngresada == "f"

def juego1():
    return

def juego2():
    return

def juego3():
    limpiarPantalla()
    input("Juego en construcción. Volvé pronto!\n\nPresione Enter para volver\n")

def juego4():
    return

def reporte():
    return

def salir():
    limpiarPantalla()
    print("")
    print("--------------------------------------------------------")
    print("")
    print("  Gracias por jugar, no apueste, juegue por diversión")
    print("")
    print("--------------------------------------------------------")
    print("")
    input("Presione Enter para salir\n")

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
""" menu()
opcion = input("Elija una opción: ")
 """

while continuar:
    while not opcionEsValida:
        menu()
        if not flagAdvertencia:
            print("")
        else: 
            print(RED + "Seleccione una opción válida" + RESET)
        opcion = input("Elija una opción: ")
        if validarOpcion(opcion):
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