
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
import random

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
    """juego del menor - mayor"""
    limpiarPantalla()
    nombre = input("ingresar nombre: ")
    print(f"¡Hola {nombre}! vamos a jugar al menor-mayor.")
    print("te muestro un numero y tenes que adivinar si el siguiente es mayor o menor")
    
    numeroActual = random.randint(1,1000)
    print(f"Número actual: {numeroActual}")
    racha = 0
    juegoTerminado = False
    
    while not juegoTerminado:
        prediccion = input("¿mayor o menor? ").strip().lower()
        

        prediccionValida = False
        while not prediccionValida:
            if prediccion in ["mayor", "menor"]:
                prediccionValida = True
            else:
                print("por favor ingrese solo 'mayor' o 'menor'")
                prediccion = input("¿MAYOR o MENOR? ").strip().lower()
        
        numeroSiguiente = random.randint(1, 1000)
        
        acierto = False
        if (prediccion == "mayor" and numeroSiguiente > numeroActual) or \
           (prediccion == "menor" and numeroSiguiente < numeroActual):
            racha += 1
            print(GREEN + f"¡le diste capo! Racha: {racha}" + RESET)
            acierto = True
        

        if not acierto:
            print(RED + f"¡le erraste como los mejores ! el numero era {numeroSiguiente}" + RESET)
            print(f"¡juego terminado {nombre}! la racha final fue de {racha} aciertos.")
            input("\nPresione Enter para volver al menu...")
            juegoTerminado = True
        

        numeroActual = numeroSiguiente
        if not juegoTerminado:
            print(f"nuevo número: {numeroActual}\n")

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