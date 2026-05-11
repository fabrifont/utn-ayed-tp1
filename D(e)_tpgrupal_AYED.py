#Ejercicio D con puntualizaciones.

import random 
import os

os.system("cls") 


nombre_j = input("Jugador/a, ingrese su nombre: \n")

descripcion_j = print(f"\n{nombre_j}, sumaremos dos numeros entre 1 y 6. \nSi el resultado es par, usted ganara y sumara un punto. De lo contrario perdera y no sumara puntos.")

#historial de victorias.
contadorhistorico = 0

#while en si, hasta que al final de alguna ronda el jugador introduzca no.
continuar = "si"

while continuar == "si":
  
  #random.ranint (a,b) genera n random en el rango (a,b).  
  caraUno = random.randint (1, 6)
  caraDos = random.randint (1, 6)

  suma_caras = caraUno + caraDos

  #la respuesta de la suma de las caras se le muestra al jugador sólo después de introducir par/impar.
  respuesta_j = input(f"\n{nombre_j}. Par o impar?: \n")
  
  print(suma_caras)

 # resto de la división por 2 == 0 para obtener los pares.
  if suma_caras % 2 == 0:
    resultado_caras = "par"

  else:
    resultado_caras = "impar" 

 #igualdad entre las asignaciones de las variables.
  if respuesta_j == resultado_caras:
    
    #el historial de victorias suma 1, y tira Ganaste!, cuando la igualdad anterior se cumple.
    contadorhistorico = contadorhistorico + 1
    print("\nGanaste!")
    print(f"\nHistorial de victorias: {contadorhistorico}\n")
      
  else:
    print("Perdiste!\n")    
    
  continuar = input(f"{nombre_j}. Queres seguir jugando?: (si/no) ")
  
  #if para cortar el while de la línea n° 17.
  if continuar == ("no"):
    print("\nEsperamos volver a verte pronto!\n")