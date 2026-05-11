import random 
import os

os.system("cls") 


nombre_j = input("Jugador/a, ingrese su nombre: \n")

descripcion_j = print(f"\n{nombre_j}, sumaremos dos numeros entre 1 y 6. \nSi el resultado es par, usted ganara y sumara un punto. De lo contrario perdera y no sumara puntos.")
contadorhistorico = 0

continuar = "si"

while continuar == "si":
    
  caraUno = random.randint (1, 6)
  caraDos = random.randint (1, 6)

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
    
  
  continuar = input(f"{nombre_j}. Queres seguir jugando?: (si/no) ")
  
  
  if continuar == ("no"):
    print("\nEsperamos volver a verte pronto!\n")