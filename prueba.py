def DatoPWM(xf,yf,xr,yr,xo,yo,c):
    AlphR = math.degrees(math.atan2((yo-yr),(xo-xr))*-1
    if AlpR >= 0:
        AlpR = AlpR
    else:
        AlpR = 360 + AlpR

    AlphRP = math.degrees(math.atan2((yf-yr),(xf-xr))*-1
    if AlpRF >=0:
        AlpRF = AlpRF
    else:
        AlpRF = 360 + AlpRF

    Dif = AlphR - AlphRP
    if Dif >=0:
        Dif = Dif
    else:
        Dif = 360 + Dif

    if DifVe < 15 or DifVe >345 and ConsMoV == 1 :
        if c!=1:
            print("Moverse derecho")
            c=1
            Dato = 1
        Dato = 210
    else:
        ConsMoV = 0

    if DifVe > 180 and DifVe < 355 and ConsMoV == 0:
        if c!=2:
            print("Girar sentido anti horario")
            c=2
            Dato = 1
        else:
            Dato = 5
    elif DifVe > 5 and DifVe <=180 and ConsMoV == 0:
        if c!=3:
            print("Girar sentido horario")
            c=3
            Dato = 1
        else:
            Dato = 106
    else:
        ConsMoV = 1
    return(Dato,Dif,c)

