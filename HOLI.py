import math
import os
from io import open
import time
import prueba
import socket

CTRA = CTRN = CTRV = 0

ConsMoV = 1

ca=cn=cv=0
c=0

ax1=ay1=cx1=cy1=vx1=vy1=amx1=amy1=rx1=ry1=rox1=roy1=0

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

while(1):
    per = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/per.txt","r")
    p = per.read()
    per.close()

    if p == '1' :
        azulx = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/azul/x.txt","r")
        azuly = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/azul/y.txt","r")
        ax = azulx.read() 
        ay = azuly.read()
        azulx.close()
        azuly.close()
         
        celestex = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/celeste/x.txt","r")
        celestey = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/celeste/y.txt","r")
        cx = celestex.read()
        cy = celestey.read()
        celestex.close()
        celestey.close()

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
        
        rojox = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/rojo/x.txt","r")
        rojoy = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/rojo/y.txt","r")
        rx = rojox.read()
        ry = rojoy.read()
        rojox.close()
        rojoy.close()
    
        rosadox = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/cafe/x.txt","r")
        rosadoy = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/cafe/y.txt","r")
        rox = rosadox.read() 
        roy = rosadoy.read()
        rosadox.close()
        rosadoy.close()
        
        if ax is None:
            ax = ax1
        if ay is None:
            ay = ay1
        ax1 = int(ax)
        ay1 = int(ay)

        if cx is None:
            cx = cx1
        if cy is None:
            cy = cy1
        cx1 = int(cx)
        cy1 = int(cy)

        if vx is None:
            vx = vx1
        if ay is None:
            vy = vy1
        vx1 = int(vx)
        vy1 = int(vy)

        if amx is None:
            amx = amx1
        if amy is None:
            amy = amy1
        amx1 = int(amx)
        amy1 = int(amy)

        if rx is None:
            rx = rx1
        if ry is None:
            ry = ry1
        rx1 = int(rx)
        ry1 = int(ry)

        if rox is None:
            rox = rox1
        if roy is None:
            roy = roy1
        rox1 = int(rox)
        roy1 = int(roy)

        
    
    ###ANGULOS###

        AlpRA = math.degrees(math.atan2((cy1-ay1),(cx1-ax1)))*-1
        if AlpRA >=0:
            AlpRA = AlpRA
        else:
            AlpRA = 360 + AlpRA
        AlpRV = math.degrees(math.atan2((amy1-vy1),(amx1-vx1)))*-1
        if AlpRV >=0:
            AlpRV = AlpRV
        else:
            AlpRV = 360 + AlpRV
        AlpRN = math.degrees(math.atan2((roy1-ry1),(rox1-rx1)))*-1
        """if AlpRN >=0:
            AlpRN = AlpRN
        else:
            AlpRN = 360 + AlpRN"""

    ### ver si hay movimiento

        robMov = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/RobMov.txt","r")
        Robmov = robMov.read()
        robMov.close()

        X1 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/X1.txt","r")
        x1 = int(X1.read())
        X1.close()
        Y1 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/Y1.txt","r")
        y1 = int(Y1.read())
        Y1.close()

        X2 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/X2.txt","r")
        x2 = int(X2.read())
        X2.close()
        Y2 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/Y2.txt","r")
        y2 = int(Y2.read())
        Y2.close()

        X3 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/X3.txt","r")
        x3 = int(X3.read())
        X3.close()
        Y3 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/Y3.txt","r")
        y3 = int(Y3.read())
        Y3.close()

        if Robmov == '0': ##automático
            VecAz = ((x1-ax1)**2+(y1-ay1)**2)**(1/2) #Distancia entre puntos
            VecNa = ((x1-rx1)**2+(y1-ry1)**2)**(1/2)
            VecVe = ((x1-vx1)**2+(y1-vy1)**2)**(1/2)
            #print("La Distancia del robot azul al punto es: ",VecAz,"\nLa Distancia del robot naranjo al punto es: ",VecNa,"\nLa Distancia del robot verde al punto es: ",VecVe)
            ############################################################
            if VecAz <= VecNa and VecAz <=VecVe and VecAz <= VecVe:
                print("El robot azul está más cerca")
                AlpRAF = math.degrees(math.atan((y1-ay1),(x1-ax1)))*-1
                if AlpRAF >=0:
                    AlpRAF = AlpRAF
                else:
                    AlpRAF = 360 + AlpRAF
                if VecAz > 15:
                    print("Comenzar movimiento")
                    print(AlpRA)
                    print(AlpRAF)
            ##movimiento del robot
                
                    if AlpRA < (AlpRAF+5) and AlpRA > (AlpRAF-5):
                        print("Moverse derecho")
                        ConsGir = 1
                        CTRA = 20                        
                    else:
                        ConsGir = 0
                    ##Corregir la dirección del robot

                    if AlpRA < AlpRAF and ConsGir == 0:
                        print("Girar sentido anti horario")
                        CTRA = 320  
                    elif AlpRA > AlpRAF and ConsGir == 0:
                        print("Girar sentido horario")
                        CTRA = 220  
                    
                else :
                    print("UI puede volver a funcionar ")
                    CTRA = 0
                    PasMovRA = 0 ##PASO A MOVIMIENTO A ROBOT BLOQUEADO HASTA QUE SE CAMBIEN COORDENADAS FINALES

                
            ###########################################################        
            elif VecNa <= VecVe and VecNa <=VecAz:
                print("El robot naranjo está más cerca")
                AlpRNF = math.degrees(math.atan2((y1-ry1),(x1-rx1)))*-1
                if AlpRNF >=0:
                    AlpRNF = AlpRNF
                else:
                    AlpRNF = 360 + AlpRNF

                if VecAz > 15:
                    print("Comenzar movimiento")

            ##movimiento del robot
                
                    if AlpRN < (AlpRNF+15) and AlpRN > (AlpRNF-15):
                        print("Moverse derecho")
                        ConsGir = 1
                        CTRN = 225

                    else:
                        ConsGir = 0
                    ##Corregir la dirección del robot

                    if AlpRN < AlpRNF and ConsGir == 0:
                        print("Girar sentido anti horario")
                        CTRN = 15
                    elif AlpRN > AlpRNF and ConsGir == 0:
                        print("Girar sentido horario")
                        CTRN = 116
                else :
                    print("UI puede volver a funcionar ")
                    CTRN = 0
                    PasMovRN = 0 ##PASO A MOVIMIENTO A ROBOT BLOQUEADO HASTA QUE SE CAMBIEN COORDENADAS FINALES

                naranjo = open("C:/Users/Neftali/Desktop/Comunicación esp/Naranjo/ordenn.txt","w")
                naranjo.write(str(CTRN))
                naranjo.close()
            #####################################################   
            else:
                """if AlpRVF >=0:
                    AlpRVF = AlpRVF
                else:
                    AlpRVF = 360 + AlpRVF"""
                AlpRVF = math.degrees(math.atan2((y1-vy1),(x1-vx1)))*-1
                if VecVe > 15:
                    DifVe = AlpRV - AlpRVF
                    #print("Comenzar movimiento")

            ##movimiento del robot
                
                    if abs(DifVe) < 15 and ConsMoV == 1 :
                        if c!=1:
                            print("Moverse derecho")
                            c=1
                            CTRV = 0
                        else: 
                            CTRV = 225

                    else:
                        ConsMoV = 0
                    ##Corregir la dirección del robot

                    if DifVe < -10 and ConsMoV == 0:
                        if c!=2:
                            print("Girar sentido anti horario")
                            c=2
                            CTRV = 0
                        else:
                            CTRV = 5
                    elif DifVe >10 and ConsMoV == 0:
                        if c!=3:
                            print("Girar sentido horario")
                            c=3
                            CTRV = 0
                        else:
                            CTRV = 106
                    else:
                        ConsMoV = 1 
                else :
                    print("UI puede volver a funcionar ")
                    CTRV = 0
                    PasMovRV = 0 ##PASO A MOVIMIENTO A ROBOT BLOQUEADO HASTA QUE SE CAMBIEN COORDENADAS FINALES

        ##########################################################        
        elif Robmov == '1':##mover azul
            H=0

        elif Robmov == '2':##mover naranjo
            H=0

        elif Robmov == '3':##mover verde
            H=0

        elif Robmov == '4':##mover dos

            rob2Mov = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/Rob2Mov.txt","w")
            Rob2Mov = rob2Mov.read()
            rob2Mov.close()

            if Rob2Mov == '3':##mueve azul y naranjo
                VecAz1 = ((x1 - ax1)**2 + (y1 - ay1)**2)**(1/2)   #Distancia entre robot azul y pto1
                VecAz2 = ((x2 - ax1)**2 + (y2 - ay1)**2)**(1/2)   #Distancia entre robot azul y pto2
                VecNa1 = ((x1 - rx1)**2 + (y1 - ry1)**2)**(1/2)   #Distancia entre robot naranjo y pto1
                VecNa2 = ((x2 - rx1)**2 + (y2 - ry1)**2)**(1/2)   #Distancia entre robot naranjo y pto2
                OpMov1 = VecAz1 + VecNa2
                OpMov2 = VecAz2 + VecNa1

                if OpMov1 <= OpMov2:
                    print("Azul a punto 1 y Naranjo a punto 2")
                if OpMov1 > OpMov2:
                    print("Azul a punto 2 y Naranjo a punto 2")
                

            elif Rob2Mov == '4':## mueve azul y verde
                VecAz1 = ((x1-ax1)**2+(y1-ay1)**2)**(1/2)   #Distancia entre robot azul y pto1
                VecAz2 = ((x2-ax1)**2+(y2-ay1)**2)**(1/2)   #Distancia entre robot azul y pto2
                VecVe = ((x1-vx1)**2+(y1-vy1)**2)**(1/2)   #Distancia entre robot verde y pto1
                VecVe = ((x2-vx1)**2+(y2-vy1)**2)**(1/2)   #Distancia entre robot verde y pto2
                OpMov1 = VecAz1 + VecVe2
                OpMov2 = VecAz2 + VecVe1

                if OpMov1 <= OpMov2:
                    print("Azul a punto 1 y Verde a punto 2")
                if OpMov1 > OpMov2:
                    print("Azul a punto 2 y Verde a punto 2")

            elif Rob2Mov == '5':## mueve naranjo y verde
                VecNa = ((x1-rx1)**2+(y1-ry1)**2)**(1/2)   #Distancia entre robot naranjo y pto1
                VecNa = ((x2-rx1)**2+(y2-ry1)**2)**(1/2)   #Distancia entre robot naranjo y pto2
                VecVe = ((x1-vx1)**2+(y1-vy1)**2)**(1/2)   #Distancia entre robot verde y pto1
                VecVe = ((x2-vx1)**2+(y2-vy1)**2)**(1/2)   #Distancia entre robot verde y pto2
                OpMov1 = VecNa1 + VecVe2
                OpMov2 = VecNa2 + VecVe1

                if OpMov1 <= OpMov2:
                    print("Naranjo a punto 1 y Verde a punto 2")
                if OpMov1 > OpMov2:
                    print("Naranjo a punto 2 y Verde a punto 2")
        elif Robmov == '5':##mover todos
            VecAz1 = ((x1-ax1)**2+(y1-ay1)**2)**(1/2)   #Distancia entre robot azul y pto1
            VecAz2 = ((x2-ax1)**2+(y2-ay1)**2)**(1/2)   #Distancia entre robot azul y pto2
            VecAz3 = ((x3-ax1)**2+(y3-ay1)**2)**(1/2)   #Distancia entre robot azul y pto3
            VecNa1 = ((x1-rx1)**2+(y1-ry1)**2)**(1/2)   #Distancia entre robot naranjo y pto1
            VecNa2 = ((x2-rx1)**2+(y2-ry1)**2)**(1/2)   #Distancia entre robot naranjo y pto2
            VecNa3 = ((x3-rx1)**2+(y3-ry1)**2)**(1/2)   #Distancia entre robot naranjo y pto3
            VecVe1 = ((x1-vx1)**2+(y1-vy1)**2)**(1/2)   #Distancia entre robot verde y pto1
            VecVe2 = ((x2-vx1)**2+(y2-vy1)**2)**(1/2)   #Distancia entre robot verde y pto2
            VecVe3 = ((x3-vx1)**2+(y3-vy1)**2)**(1/2)   #Distancia entre robot verde y pto3

            ##CONDICIONES DE ELECCIÓN DE ROBOT MÁS CERCANO
            OpMov1 = VecAz1 + VecNa2 + VecVe3
            OpMov2 = VecAz1 + VecNa3 + VecVe2 
            OpMov3 = VecAz2 + VecNa1 + VecVe3 
            OpMov4 = VecAz3 + VecNa2 + VecVe1
            OpMov5 = VecAz2 + VecNa3 + VecVe1
            OpMov6 = VecAz3 + VecNa1 + VecVe2
            

            if OpMov1 <= OpMov2 and OpMov1 <= OpMov3 and OpMov1 <= OpMov4 and OpMov1 <= OpMov5 and OpMov1 <= OpMov6:
                print("Azul >> Punto 1\nNaranjo >> Punto 2\nVerde >> Punto 3")

            elif OpMov2 <= OpMov1 and OpMov2 <= OpMov3 and OpMov2 <= OpMov4 and OpMov2 <= OpMov5 and OpMov2 <= OpMov6:
                print("Azul >> Punto 1\nNaranjo >> Punto 3\nVerde >> Punto 4")

            elif OpMov3 <= OpMov1 and OpMov3 <= OpMov2 and OpMov3 <= OpMov4 and OpMov3 <= OpMov5 and OpMov3 <= OpMov6:
                print("Azul >> Punto 2\nNaranjo >> Punto 1\nVerde >> Punto 3")

            elif OpMov4 <= OpMov1 and OpMov4 <= OpMov2 and OpMov4 <= OpMov3 and OpMov4 <= OpMov5 and OpMov4 <= OpMov6:
                print("Azul >> Punto 3\nNaranjo >> Punto 2\nVerde >> Punto1")

            elif OpMov5 <= OpMov1 and OpMov5 <= OpMov2 and OpMov5 <= OpMov3 and OpMov5 <= OpMov4 and OpMov5 <= OpMov6:
                print("Azul >> Punto 2\nNaranjo >> Punto 3\nVerde >> Punto1")

            elif OpMov6 <= OpMov1 and OpMov6 <= OpMov2 and OpMov6 <= OpMov3 and OpMov6 <= OpMov4 and OpMov6 <= OpMov5:
                print("Azul >> Punto 3\nNaranjo >> Punto 1\nVerde >> Punto2")

    ctra = str(CTRA)
    ctrn = str(CTRN)
    ctrv = str(CTRV)
    
    if IniBlue != CTRA:
        blueClient.send(ctra.encode())                 #Envía el ciclo de trabajo al cliente
        print('Azul ha cambiado a : ', ctra)
        IniBlue = CTRA
   
    if IniRed != CTRN:
        redClient.send(ctrn.encode())               #Envía el ciclo de trabajo al cliente
        print('Naranjo ha cambiado a : ', ctrn)
        IniRed = CTRN
      
    if IniGreen != CTRV:
        greenClient.send(ctrv.encode())               #Envía el ciclo de trabajo al cliente
        print('Verde ha cambiado a : ', ctrv)
        IniGreen = CTRV
