from io import open

k=0
print('Esperando confirmación de conección de robots')
while (1):
    ack = open("C:/Users/Neftali/Desktop/Comunicación esp/ack.txt","r")#abre el archivo de ACK
    k = ack.read()
    print(k)

    if k == '1':
        print('Ingrese el robot a dar instruciones, 1 si es el azul, 2 si es el naranjo, 3 si es el verde, cualquier boton para pararlo')
        RM = input("Robot a mandar>>")
        if RM == '1': ## instrucciónes a robot azul
            print('Ha seleccionado el azul, presione 1 para mover, presione otro botón para parar')
            O= input("Orden>>")
            if O == '1':
                print('Ingrese el sentido del movimiento, Adelante:1, Atrás:2, Horario: 3, Antihorario: 4')
                D=input("Sentido de movimiento>>")
                CT=input("Ciclo de trabajo>>")
            else :
                D=0
                CT=0
        elif RM == '2': ## instrucciónes a robot naranjo
            print('Ha seleccionado el naranjo, presione 1 para mover, presione otro botón para parar')
            O= input("Orden>>")
            if O == '1':
                print('Ingrese el sentido del movimiento, Adelante:1, Atrás:2, Horario: 3, Antihorario :4 ')
                D=input("Sentido de movimiento>>")
                CT=input("Ciclo de trabajo>>")
            else :
                D=0
                CT=0
        elif RM == '3': ## instrucciónes a robot verde
            print('Ha seleccionado el verde, presione 1 para mover, presione otro botón para parar')
            O= input("Orden>>")
            if O == '1':
                print('Ingrese el sentido del movimiento, Adelante:1, Atrás:2, Horario: 3, Antihorario: 4')
                D=input("Sentido de movimiento>>")
                CT=input("Ciclo de trabajo>>")
                
            else :
                D=0
                CT=0
        else:
            print('Ha seleccionado detener todos los robots')
            D=0
            CT=0
        
        CT = int(CT)
        
        if D == '1':
            CT = CT
        elif D == '2':
            CT = CT + 101
        elif D == '3':
            CT = CT + 202
        elif D == '4':
            CT = CT + 303
        else:
            CT = 0
        CT = CT + 1

        if RM == '1': ## instrucciónes a robot azul
            azul = open("C:/Users/Neftali/Desktop/Comunicación esp/Azul/ordena.txt","w")
            azul.write(str(CT))
            azul.close()
            print('Instrucción enviada a azul')
        elif RM == '2': ## instrucciónes a robot naranjo
            naranjo = open("C:/Users/Neftali/Desktop/Comunicación esp/Naranjo/ordenn.txt","w")
            naranjo.write(str(CT))
            naranjo.close()
            print('Instrucción enviada a naranjo')
        elif RM == '3': ## instrucciónes a robot verde
            verde = open("C:/Users/Neftali/Desktop/Comunicación esp/Verde/ordenv.txt","w")
            verde.write(str(CT))
            verde.close()
            print('Instrucción enviada a verde')
        else:
            azul = open("C:/Users/Neftali/Desktop/Comunicación esp/Azul/ordena.txt","w")
            naranjo = open("C:/Users/Neftali/Desktop/Comunicación esp/Naranjo/ordenn.txt","w")
            verde = open("C:/Users/Neftali/Desktop/Comunicación esp/Verde/ordenv.txt","w")
            azul.write(str(CT))
            print('Instrucción enviada a azul')
            naranjo.write(str(CT))
            print('Instrucción enviada a naranjo')
            verde.write(str(CT))
            print('Instrucción enviada a verde')
            azul.close()
            naranjo.close()
            verde.close()
        print(CT)
        

    

    
            
            
    

