from io import open
import math

while (1):
    print("Para mover de forma automática:1\nPara mover de forma manual: 2\nPara mover 2 robots: 3\nPara mover 3 robots: 4\n Para ordenar robots: 5")
    L1 = input("Ingrese opción>>")
    if L1 == '1':
        print("Insertar coordenadas x,y")
        x1 =input("x >>")
        y1 = input("y >>")
        RobMov = 0
        robMov = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/RobMov.txt","w")
        robMov.write(str(RobMov))
        robMov.close()

        X1 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/X1.txt","w")
        X1.write(str(x1))
        X1.close()

        Y1 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/Y1.txt","w")
        Y1.write(str(y1))
        Y1.close()     
        

    elif L1 == '2':
        print("Función de momento no disponible")
        #print("Inserte robot que desea mover\n Azul: 1\n Naranjo: 2\n Verde: 3")
        #RobMov = input("Robot >>")
        #print("Insertar coordenadas x,y")
        #x1 =input("x >>")
        #y1 = input("y >>")

        #robMov = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/RobMov.txt","w")
        #robMov.write(str(RobMov))
        #robMov.close()

        #X1 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/X1.txt","w")
        #X1.write(str(x2))
        #X1.close()

        #Y1 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/Y1.txt","w")
        #Y1.write(str(y2))
        #Y1.close()

    elif L1 == '3':
        print("Ha seleccionado mover 2 robot")
        RobMov = 4
        robMov = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/RobMov.txt","w")
        robMov.write(str(RobMov))
        robMov.close()
        
        '''RobMov1 = input("Robot 1 >>")
        RobMov2 = input("Robot 2 >>")
        Rob2Mov = int(RobMov1)+int(RobMov2)
        rob2Mov = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/Rob2Mov.txt","w")
        rob2Mov.write(str(Rob2Mov))
        rob2Mov.close()'''
        
        print("Insertar coordenadas x,y primer robot")
        x1 =input("x >>")
        y1 = input("y >>")
        print("Insertar coordenadas x,y segundo robot")
        x2 =input("x >>")
        y2 = input("y >>")

        X1 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/X1.txt","w")
        X1.write(str(x1))
        X1.close()
        Y1 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/Y1.txt","w")
        Y1.write(str(y1))
        Y1.close()

        X2 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/X2.txt","w")
        X2.write(str(x2))
        X2.close()
        Y2 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/Y2.txt","w")
        Y2.write(str(y2))
        Y2.close()

    elif L1 == '4':
        print("Se moverán los 3 robots")
        RobMov = 5
        robMov = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/RobMov.txt","w")
        robMov.write(str(RobMov))
        robMov.close()
        
        print("Insertar coordenadas x,y primer robot")
        x1 =input("x >>")
        y1 = input("y >>")
        print("Insertar coordenadas x,y segundo robot")
        x2 =input("x >>")
        y2 = input("y >>")
        print("Insertar coordenadas x,y tercer robot robot")
        x3 =input("x >>")
        y3 = input("y >>")

        X1 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/X1.txt","w")
        X1.write(str(x1))
        X1.close()
        Y1 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/Y1.txt","w")
        Y1.write(str(y1))
        Y1.close()

        X2 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/X2.txt","w")
        X2.write(str(x2))
        X2.close()
        Y2 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/Y2.txt","w")
        Y2.write(str(y2))
        Y2.close()

        X3 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/X3.txt","w")
        X3.write(str(x3))
        X3.close()
        Y3 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/Y3.txt","w")
        Y3.write(str(y3))
        Y3.close()
        
    elif L1 == '5':
        print("Se moverán los 3 robots")
        RobMov = 5
        robMov = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/RobMov.txt","w")
        robMov.write(str(RobMov))
        robMov.close()
        
        print("Línea vertical: 1\n Línea Horizontal: 2\n Triangulo: 3")
        TipLin = input("Opción >>")
        pp = 1
        if TipLin == '1':
            x1 = 628
            y1 = 200
            x2 = 628
            y2 = 400
            x3 = 628
            y3 = 600
        elif TipLin == '2':
            x1 = 200
            y1 = 400
            x2 = 620
            y2 = 400
            x3 = 1040
            y3 = 400
        elif TipLin == '3' :
            x1 = 628
            y1 = 150
            x2 = 845
            y2 = 525
            x3 = 411
            y3 = 525
            
        else:
            print("Opción no válida")
            pp = 0

        if pp == 1:
            X1 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/X1.txt","w")
            X1.write(str(x1))
            X1.close()
            Y1 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/Y1.txt","w")
            Y1.write(str(y1))
            Y1.close()

            X2 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/X2.txt","w")
            X2.write(str(x2))
            X2.close()
            Y2 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/Y2.txt","w")
            Y2.write(str(y2))
            Y2.close()

            X3 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/X3.txt","w")
            X3.write(str(x3))
            X3.close()
            Y3 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/Y3.txt","w")
            Y3.write(str(y3))
            Y3.close()
        
    else :
        print("Opción ingresada no válida")

    up = 1
    pit = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/pit.txt","w")
    pit .write(str(up))
    pit .close()
    
