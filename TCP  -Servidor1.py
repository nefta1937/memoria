import time
import socket                         #Llama las librerías necesarias para el programa
import os
from io import open


ack = open("C:/Users/Neftali/Desktop/Comunicación esp/ack.txt","w+")#abre el archivo de ACK
ack.write(str(0)) ##Pone el ack en cero
ack.close()

sBlue = socket.socket()                   #Abre socket azul
hostBlue = ''
portBlue = 3000
sBlue.bind((hostBlue, portBlue))        
print("Esperando a Azul")

sBlue.listen(1)                           #Espera robot azul

blueClient, addr = sBlue.accept()                  #Genera la conexión con el cliente
print ('Conectado con: ', addr)
ConfirmBlue = blueClient.recv(1024)            #Recibe confirmaión de conección
print(ConfirmBlue)                    #Imprime mensaje de confirmación

sRed = socket.socket()                   #Abre socket Rojo
hostRed = ''
portRed = 3001
sRed.bind((hostRed, portRed))        
print("Esperando a Naranjo")

sRed.listen(1)                           #Espera robot Rojo

redClient, addr1 = sRed.accept()  
print ('Conectado con: ', addr1)
ConfirmRed = redClient.recv(1024)            #Recibe confirmción de cambio de ciclo de trabajo
print(ConfirmRed)                    #Imprime mensaje de confirmación

sGreen = socket.socket()                   #Abre socket Rojo
hostGreen = ''
portGreen = 3002
sGreen.bind((hostGreen, portGreen))        
print("Esperando a Verde")

sGreen.listen(1)                           #Espera robot Rojo

greenClient, addr2 = sGreen.accept()  
print ('Conectado con: ', addr2)
ConfirmGreen = greenClient.recv(1024)            #Recibe confirmción de cambio de ciclo de trabajo
print(ConfirmGreen)                    #Imprime mensaje de confirmación

print ('Conecciones realizadas')

ack = open("C:/Users/Neftali/Desktop/Comunicación esp/ack.txt","w+")#abre el archivo de ACK
ack.write(str(1))# Pone ack en 1, programa listo para recibir información

ack.close()

i=0
IniBlue = "999"
IniRed = "999"
IniGreen = "999"

while True:
   
   blueFilePointer = open("C:/Users/Neftali/Desktop/Comunicación esp/Azul/ordena.txt","r+")
   blueData = blueFilePointer.read()
   blueFilePointer.close()
      
   if IniBlue != blueData:

      try:
         blueData = int(blueData)
      except ValueError:
         blueData = 1
         print("Dato Vacíoen azul")
         
      blueData = str(blueData)
      blueClient.send(blueData.encode())                 #Envía el ciclo de trabajo al cliente
      print('Azul ha cambiado a : ', blueData)
      IniBlue = blueData
   
   redFilePointer = open("C:/Users/Neftali/Desktop/Comunicación esp/Naranjo/ordenn.txt","r+")
   redData = redFilePointer.read()
   redFilePointer.close()

   blueData = str(blueData)
   
   if IniRed != redData:

      try:
         redData = int(redData)
      except ValueError:
         redData = 1
         print("Dato Vacío en rojo")

      redData = str(redData)   
      redClient.send(redData.encode())               #Envía el ciclo de trabajo al cliente
      print('Naranjo ha cambiado a : ', redData)
      IniRed = redData
      

   greenFilePointer = open("C:/Users/Neftali/Desktop/Comunicación esp/Verde/ordenv.txt","r+")
   greenData = greenFilePointer.read()
   greenFilePointer.close()
   if IniGreen != greenData:

      try:
         greenData = int(greenData)
      except ValueError:
         greenData = 1
         print("Dato Vacío en verde")

      greenData = str(greenData)   
      greenClient.send(greenData.encode())               #Envía el ciclo de trabajo al cliente
      print('Verde ha cambiado a : ', greenData)
      IniGreen = greenData
