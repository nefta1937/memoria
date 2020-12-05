import math
import os
from io import open
import time
import prueba
import socket

ax1=ay1=cx1=cy1=vx1=vy1=amx1=amy1=rx1=ry1=rox1=roy1=0

CTRV=0

cv=10

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
IniGreen = "999"
HisAlp1 = math.tan(math.radians(20))
HisAlp2 = math.tan(math.radians(20))
cd=3

while(1):
    per = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/per.txt","r")
    p = per.read()
    per.close()

    if p == '1' :
        verdex = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/verde/x.txt","r")
        verdey = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/verde/y.txt","r")
        vx = verdex.read()
        vy = verdey.read()
        verdex.close()
        verdey.close()        
    
        amarillox = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/amarillo/x.txt","r")
        amarilloy = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/amarillo/y.txt","r")
        amx = amarillox.read()
        amy = amarilloy.read()
        amarillox.close()
        amarilloy.close()
        X1 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/X1.txt","r")
        x1 = int(X1.read())
        X1.close()
        Y1 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/Y1.txt","r")
        y1 = int(Y1.read())
        Y1.close()
        if vx is None:
            vx = vx1
        if vy is None:
            vy = vy1
        vx1 = int(vx)
        vy1 = int(vy)
        amx1 = int(amx)
        amy1 = int(amy)
        if vx1 == amx1 :
            pva = pva
            
        else:
            py = amy1-vy1
            px = amx1-vx1
            pva = py / px*-1
        VecVe = ((x1-vx1)**2+(y1-vy1)**2)**(1/2)
        if x1 == vx1 :
            PenRoVFi = PenRoVFi
            
        else:
            PenRoVFi = (y1-vy1)/(x1-vx1)
            PenRoVFi = PenRoVFi*-1        
        VecAm = ((x1-amx1)**2+(y1-amy1)**2)**(1/2)
        Hs=PenRoVFi+HisAlp1
        Hi=PenRoVFi-HisAlp1
        if VecVe > 25:
            DisRV = abs(abs(pva)-abs(PenRoVFi))
            if DisRV <= abs(HisAlp2) :
                ConsGir=1
                if VecAm < VecVe:
                    if cv != 9:
                          cv=9
                          print("Adelante")
                          print("Vector amarillo: ",VecAm,"\nVector verde",VecVe)
                    #ConsGir = 1
                    print("DisRV",DisRV)
                    CTRV = 232
                    cd = 0
                elif VecAm >= VecVe:
                    if cv != 10:
                        cv=10
                        print("Atras")
                        print("Vector amarillo: ",VecAm,"\nVector verde",VecVe)
                    
                    CTRV = 331
            else:
                ConsGir = 0
    

##Corregir la dirección del robot
            if PenRoVFi <0 and ConsGir == 0 :
                if abs(pva) > abs(Hs):
                    if cv!=3:
                        print("Girar sentido anti horario 1")
                        print("PVA: ",pva)
                        print("pvpf",Hs)
                        print("DisRV",DisRV)
                        print("PenRoVFi",PenRoVFi)
                        cv=3
                    CTRV = 20
                    cd=1

                elif abs(pva) < abs(Hi):
                    if cv!=2:
                        print("Girar sentido horario 1")
                        print("PVA: ",pva)
                        print("pvpf",Hi)
                        print("DisRV",DisRV)
                        print("PenRoVFi2",PenRoVFi)
                        cv=2
                    CTRV = 120
                        
            elif PenRoVFi >0 :
                if abs(pva) < abs(PenRoVFi-HisAlp1) :
                    if cv != 5:
                        print("Girar sentido anti horario 2")
                        print(PenRoVFi)
                        print(pva)
                        cv = 5
                    CTRV =20
            
                    cd = 1

                elif abs(pva) > abs(PenRoVFi+HisAlp1):
                       
                    if cv != 4:
                        print("Girar sentido horario 2")
                        print(PenRoVFi)
                        print(pva)
                        cv = 4
                    CTRV = 20
                    cd = 2
                else:
                    cd=3
        else :
            print("UI puede volver a funcionar ")
            CTRV = 0
            PasMovRV = 0 ##PASO A MOVIMIENTO A ROBOT BLOQUEADO HASTA QUE SE CAMBIEN COORDENADAS FINALES
            X1 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/X1.txt","w")
            X1.write(vx)
            X1.close()
            Y1 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/Y1.txt","w")
            Y1.write(vy)
            Y1.close()
       
        CTRV=str(CTRV)
        if IniGreen != CTRV:

            greenClient.send(CTRV.encode())               #Envía el ciclo de trabajo al cliente
            print('Verde ha cambiado a : ', CTRV)
            IniGreen = CTRV
        
