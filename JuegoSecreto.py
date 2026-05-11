import random

print("¡Bienvenido al juego del número secreto!")
Nombredeljugador = str(input("¿Cuál es tu nombre? "))
print("Hola", Nombredeljugador, "¡Vamos a jugar al número secreto!")
print("El juego consiste en adivinar un número entre 1 y 100. Tienes 6 intentos para adivinarlo. ¡Buena suerte!")
IntentosRestantes = 6
IntentosRealizados = 0
VecesJugadas = 0
VecesAcertadas = 0  
VecesPerdidas = 0


for i in range(1, 1000): # El juego se repetirá hasta que el usuario decida dejar de jugar, para eso se le preguntará al finalizar cada partida si desea jugar nuevamente.
    VecesJugadas = i
    numerosecreto = random.randint(1, 100)
    #print(numerosecreto) #Borrar al terminar el juego o antes de entregar el trabajo. Se deja para facilitar las pruebas.
    IntentosRestantes = 6
    IntentosRealizados = 0
    while IntentosRestantes > 0:
        intento = int(input("Introduce tu intento:"))
    
        IntentosRealizados = IntentosRealizados + 1
        if intento == numerosecreto:
            print("¡Felicidades", Nombredeljugador, "has adivinado el número secreto! Lo has logrado en", IntentosRealizados, "intentos." )
            VecesAcertadas = VecesAcertadas + 1
            print("Has jugado", VecesJugadas, "veces, has acertado", VecesAcertadas, "veces y has perdido", VecesPerdidas, "veces.")
            break
        elif intento < numerosecreto:
            print("El número secreto es mayor que", intento)
            IntentosRestantes = IntentosRestantes - 1
        else:
            print("El número secreto es menor que", intento)
            IntentosRestantes = IntentosRestantes - 1

        if IntentosRestantes == 6:
           print("Te quedan", IntentosRestantes, "intentos.")
        elif IntentosRestantes == 5:
           print("Te quedan", IntentosRestantes, "intentos.")
        elif IntentosRestantes == 4:
           print("Te quedan", IntentosRestantes, "intentos.")
        elif IntentosRestantes == 3:
            print("Te quedan", IntentosRestantes, "intentos.")
        elif IntentosRestantes == 2:
            print("Te quedan", IntentosRestantes, "intentos.")  
        elif IntentosRestantes == 1:
            print("Te queda", IntentosRestantes, "intento.")        
        elif IntentosRestantes == 0:
            print("No te quedan intentos. El número secreto era", numerosecreto)
            VecesPerdidas = VecesPerdidas + 1
            print("Has jugado", VecesJugadas, "veces, has acertado", VecesAcertadas, "veces y has perdido", VecesPerdidas, "veces.")

    if  input("¿Deseas jugar nuevamente? (s/n) ") == "n":
        print("¡Gracias por jugar, hasta la próxima!")
        print("Has jugado", VecesJugadas, "veces, has acertado", VecesAcertadas, "veces y has perdido", VecesPerdidas, "veces.")
        break       
    else: 
        continue
