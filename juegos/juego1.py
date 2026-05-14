from colores import *
import os
import random

sistemaOperativo = os.name
comandoLimpiar = "cls" if sistemaOperativo == "nt" else "clear"


def limpiarPantalla():
    os.system(comandoLimpiar)


def juego1():
    """juego del menor - mayor"""
    limpiarPantalla()
    nombre = input("ingresar nombre: ")
    print(f"¡Hola {nombre}! vamos a jugar al menor-mayor.")
    print("te muestro un numero y tenes que adivinar si el siguiente es mayor o menor")

    numeroActual = random.randint(1, 1000)
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
        if (prediccion == "mayor" and numeroSiguiente > numeroActual) or (
            prediccion == "menor" and numeroSiguiente < numeroActual
        ):
            racha += 1
            print(GREEN + f"¡le diste capo! Racha: {racha}" + RESET)
            acierto = True

        if not acierto:
            print(
                RED
                + f"¡le erraste como los mejores ! el numero era {numeroSiguiente}"
                + RESET
            )
            print(f"¡juego terminado {nombre}! la racha final fue de {racha} aciertos.")
            input("\nPresione Enter para volver al menu...")
            juegoTerminado = True

        numeroActual = numeroSiguiente
        if not juegoTerminado:
            print(f"nuevo número: {numeroActual}\n")
