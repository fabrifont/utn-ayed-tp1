
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
    input("Para continuar, presione Enter\n")

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
    print("")

def validarOpcion(opcionIngresada):
    return opcionIngresada == "A" or opcionIngresada == "B" or opcionIngresada == "C" or opcionIngresada == "D" or opcionIngresada == "E" or opcionIngresada == "F" or opcionIngresada == "a" or opcionIngresada == "b" or opcionIngresada == "c" or opcionIngresada == "d" or opcionIngresada == "e" or opcionIngresada == "f"

def juego1():
    return

def juego2():
    return

def juego3():
    print("Juego en construcción. Volvé pronto!")

def juego4():
    return

def reporte():
    return

def salir():
    continuar = False

"""
Declaración de variables
sistemaOperativo, comandoLimpiar, opcion: string
continuar: bool
"""

sistemaOperativo = os.name
comandoLimpiar = "cls" if sistemaOperativo == "nt" else "clear"
continuar = True
opcion = ""
opcionEsValida = False
# Ejecución del programa

cartelInicio()
menu()
opcion = input("Elija una opción: ")
""" while continuar:
    while not opcionEsValida:
        opcionEsValida = validarOpcion(opcion) """