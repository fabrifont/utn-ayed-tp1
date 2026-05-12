import random

print("¡Bienvenido al juego del número secreto!")
Nombredeljugador = input("¿Cuál es tu nombre? ")
print("Hola", Nombredeljugador, "¡Vamos a jugar al número secreto!")
print("El juego consiste en adivinar un número entre 1 y 100. Tienes 6 intentos para adivinarlo. ¡Buena suerte!")

IntentosRestantes = 6
IntentosRealizados = 0
VecesJugadas = 0
VecesAcertadas = 0
VecesPerdidas = 0

respuesta = "s"
while respuesta == "s":
    VecesJugadas = VecesJugadas + 1
    numerosecreto = random.randint(1, 100)
    IntentosRestantes = 6
    IntentosRealizados = 0
    intento = 0 

    while IntentosRestantes > 0:
            intento = int(input("Introduce tu intento: "))
            IntentosRealizados = IntentosRealizados + 1
            if intento == numerosecreto:
                print("¡Felicidades", Nombredeljugador, "has adivinado el número secreto! Lo has logrado en", IntentosRealizados, "intentos.")
                VecesAcertadas = VecesAcertadas + 1
                IntentosRestantes = 0
            elif intento < numerosecreto:
                print("El número secreto es mayor que", intento)
                IntentosRestantes = IntentosRestantes - 1
            else:
                print("El número secreto es menor que", intento)
                IntentosRestantes = IntentosRestantes - 1

            if IntentosRestantes > 1:
                print("Te quedan", IntentosRestantes, "intentos.")
            elif IntentosRestantes == 1:
                print("Te queda", IntentosRestantes, "intento.")

    if intento != numerosecreto:
        print("No te quedan intentos. El número secreto era", numerosecreto)
        VecesPerdidas = VecesPerdidas + 1

    print("Has jugado", VecesJugadas, "veces, has acertado", VecesAcertadas, "veces y has perdido", VecesPerdidas, "veces.")
    respuesta = input("¿Deseas jugar nuevamente? (s/n) ")
    while respuesta != "s" and respuesta != "n":
        respuesta = input("Por favor ingresa 's' o 'n': ")

print("¡Gracias por jugar, hasta la próxima!")
print("Has jugado", VecesJugadas, "veces, has acertado", VecesAcertadas, "veces y has perdido", VecesPerdidas, "veces.")
