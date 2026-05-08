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
    print("----------------------------------------------------------------------------------------------------------")
    print("")
    print("Los juegos de apuesta están" + RED + " prohibidos " + RESET + "para los menores de 18 años, y son" + RED + " perjudiciales " + RESET + "para la salud.")
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

def juego1():
    return

def juego2():
    return

def juego3():
    return

def juego4():
    return

def reporte():
    return

def salir():
    return

"""
Declaración de variables
sistemaOperativo, comandoLimpiar: string
"""

sistemaOperativo = os.name
comandoLimpiar = "cls" if sistemaOperativo == "nt" else "clear"

# Ejecución del programa

cartelInicio()