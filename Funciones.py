import math
'''Función para elegir dato a mandar'''
def DatoPWM(xf,yf,xr,yr,xo,yo,c,ConsMo):

    AlpR = math.degrees(math.atan2((yo-yr),(xo-xr)))*-1

    if AlpR >=  0:
        AlpR = AlpR
    else:
        AlpR = 360 + AlpR

    AlpRP = math.degrees(math.atan2((yf-yr),(xf-xr)))*-1
    if AlpRP >=0:
        AlpRP = AlpRP
    else:
        AlpRP = 360 + AlpRP

    Dif = AlpR - AlpRP
    if Dif >=0:
        Dif = Dif
    else:
        Dif = 360 + Dif

    if Dif <= 15 or Dif >=345 and ConsMo == 1 :
        if c!=1:
            print("Moverse derecho")
            c=1
            Dato = 1
        else:
            Dato = 210
    else:
        ConsMo = 0

    if Dif > 180 and Dif < 345 and ConsMo == 0:
        if c!=2:
            print("Girar sentido anti horario")
            c=2
            Dato = 1
        else:
            Dato = 10
    elif Dif > 15 and Dif <=180 and ConsMo == 0:
        if c!=3:
            print("Girar sentido horario")
            c=3
            Dato = 1
        else:
            Dato = 110
    
    else:
        if c!=1:
            print("Moverse derecho")
            c=1
            Dato = 1
        else:
            Dato = 210
        ConsMo = 1
    return(Dato,Dif,c,ConsMo)


def Discrim(x1,y1,xr1,yr1,xr2,yr2,xr3,yr3):
    VecAz = ((x1-ax1)**2+(y1-ay1)**2)**(1/2) #Distancia entre puntos
    VecNa = ((x1-rx1)**2+(y1-ry1)**2)**(1/2)
    VecVe = ((x1-vx1)**2+(y1-vy1)**2)**(1/2)

    Series = [VecAz, VecNa, VecVe]

    Salida = min(Series)

    if VecAz == Salida:
        xfr1 = x1 
        yfr1 = y1
        xfr2 = xr2
        yfr2 = yr2
        xfr3 = xr3
        yfr3 = yr3

    elif VecNa == Salida:
        xfr1 = xr1 
        yfr1 = yr1
        xfr2 = x1
        yfr2 = y1
        xfr3 = xr3
        yfr3 = yr3

    elif VecVe == Salida:
        xfr1 = xr1 
        yfr1 = yr1
        xfr2 = xr2
        yfr2 = yr2
        xfr3 = x1
        yfr3 = y1


    return(xfr1,yfr1,xfr2,yfr2,xfr3,yfr3)

    

'''Función para discriminar a que punto vomer 2 robots'''

def Discrim2(x1,y1,x2,y2,xr1,yr1,xr2,yr2,xr3,yr3):
    VecR1P1 = ((x1 - xr1)**2 + (y1 - yr1)**2)**(1/2)   #Distancia entre robot robot1 y pto1
    VecR1P2 = ((x2 - xr1)**2 + (y2 - yr1)**2)**(1/2)   #Distancia entre robot robot1 y pto2
    
    VecR2P1 = ((x1 - xr2)**2 + (y1 - yr2)**2)**(1/2)   #Distancia entre robot robot2 y pto1
    VecR2P2 = ((x2 - xr2)**2 + (y2 - yr2)**2)**(1/2)   #Distancia entre robot robot2 y pto2

    VecR3P1 = ((x1 - xr3)**2 + (y1 - yr3)**2)**(1/2)   #Distancia entre robot robot3 y pto1
    VecR3P2 = ((x2 - xr3)**2 + (y2 - yr3)**2)**(1/2)   #Distancia entre robot robot3 y pto2
    
    OpMov1 = VecR1P1 + VecR2P2
    OpMov2 = VecR1P1 + VecR3P2
    OpMov3 = VecR2P1 + VecR1P2
    OpMov4 = VecR2P1 + VecR3P2
    OpMov5 = VecR3P1 + VecR1P2
    OpMov6 = VecR3P1 + VecR2P2

    Series = [OpMov1, OpMov2, OpMov3, OpMov4, OpMov5, OpMov6]

    Salida = min(Series)

    if OpMov1 == Salida:
        xfr1 = x1 
        yfr1 = y1
        xfr2 = x2
        yfr2 = y2
        xfr3 = xr3
        yfr3 = yr3

    elif OpMov2 == Salida:
        xfr1 = x1
        yfr1 = y1
        xfr2 = xr2
        yfr2 = yr2
        xfr3 = x2
        yfr3 = y2

    elif OpMov3 == Salida:
        xfr1 = x2
        yfr1 = y2
        xfr2 = x1
        yfr2 = y1
        xfr3 = xr3
        yfr3 = yr3

    elif OpMov4 == Salida:
        xfr1 = xr1
        yfr1 = yr1
        xfr2 = x1
        yfr2 = y1
        xfr3 = x2
        yfr3 = y2

    elif OpMov5 == Salida:
        xfr1 = x2
        yfr1 = y2
        xfr2 = xr2
        yfr2 = yr2
        xfr3 = x1
        yfr3 = y1

    elif OpMov6 == Salida:
        xfr1 = xr1
        yfr1 = yr1
        xfr2 = x2
        yfr2 = y2
        xfr3 = x1
        yfr3 = y1    

    return(xfr1,yfr1,xfr2,yfr2,xfr3,yfr3)



def Discrim3(x1,y1,x2,y2,x3,y3,ax1,ay1,rx1,ry1,vx1,vy1,TM):

    VecAz1 = ((x1-ax1)**2+(y1-ay1)**2)**(1/2)   #Distancia entre robot azul y pto1
    VecAz2 = ((x2-ax1)**2+(y2-ay1)**2)**(1/2)   #Distancia entre robot azul y pto2
    VecAz3 = ((x3-ax1)**2+(y3-ay1)**2)**(1/2)   #Distancia entre robot azul y pto3
    VecNa1 = ((x1-rx1)**2+(y1-ry1)**2)**(1/2)   #Distancia entre robot naranjo y pto1
    VecNa2 = ((x2-rx1)**2+(y2-ry1)**2)**(1/2)   #Distancia entre robot naranjo y pto2
    VecNa3 = ((x3-rx1)**2+(y3-ry1)**2)**(1/2)   #Distancia entre robot naranjo y pto3
    VecVe1 = ((x1-vx1)**2+(y1-vy1)**2)**(1/2)   #Distancia entre robot verde y pto1
    VecVe2 = ((x2-vx1)**2+(y2-vy1)**2)**(1/2)   #Distancia entre robot verde y pto2
    VecVe3 = ((x3-vx1)**2+(y3-vy1)**2)**(1/2)   #Distancia entre robot verde y pto3

    OpMov1 = VecAz1 + VecNa2 + VecVe3
    OpMov2 = VecAz1 + VecNa3 + VecVe2 
    OpMov3 = VecAz2 + VecNa1 + VecVe3 
    OpMov4 = VecAz3 + VecNa2 + VecVe1
    OpMov5 = VecAz2 + VecNa3 + VecVe1
    OpMov6 = VecAz3 + VecNa1 + VecVe2

    Series = [OpMov1, OpMov2, OpMov3, OpMov4, OpMov5, OpMov6]

    Salida = min(Series)

    if OpMov1 == Salida:
        xfr1 = x1 
        yfr1 = y1
        xfr2 = x2
        yfr2 = y2
        xfr3 = x3
        yfr3 = y3

    elif OpMov2 == Salida:
        xfr1 = x1
        yfr1 = y1
        xfr2 = x3
        yfr2 = y3
        xfr3 = x2
        yfr3 = y2

    elif OpMov3 == Salida:
        xfr1 = x2
        yfr1 = y2
        xfr2 = x1
        yfr2 = y1
        xfr3 = x3
        yfr3 = y3

    elif OpMov4 == Salida:
        xfr1 = x3
        yfr1 = y3
        xfr2 = x1
        yfr2 = y1
        xfr3 = x2
        yfr3 = y2

    elif OpMov5 == Salida:
        xfr1 = x2
        yfr1 = y2
        xfr2 = x3
        yfr2 = y3
        xfr3 = x1
        yfr3 = y1

    elif OpMov6 == Salida:
        xfr1 = x3
        yfr1 = y3
        xfr2 = x2
        yfr2 = y2
        xfr3 = x1
        yfr3 = y1    

    return(xfr1,yfr1,xfr2,yfr2,xfr3,yfr3)
