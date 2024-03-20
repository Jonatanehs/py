poderes = []
castigos = []
monedas = 0
oro = 0
vidas = 0
aco =0
acof = 0
pregunta = 0
respuesta = 0
a= 0
d=0
fallas = 0
inte = 1
f = 1
j=0
h= 0
print("En busca de las ruinas")

# while inte <=10 or True: 
while inte <= 10 or True:
        poderes =[]
        print("Nivel 1: Explorando la Selva Profunda")
        pregunta1 = int(input("¿Cuántos centímetros tiene un metro? "))
        if pregunta1 == 100:
            print("La respuesta 1 es correcta")
            monedas += 5000
            pregunta += 1
        
            aco +=1
        else:
            print("Respuesta incorrecta")
            fallas += 1
            acof +1
    
        pregunta2 = int(input("¿Cuántos metros hay de árbol a árbol? "))
        if pregunta2 == 5:
            print("La respuesta 2 es correcta")
            monedas += 5000
            aco +=1
            pregunta += 1
        else:
            print("Respuesta incorrecta")
            acof +=1
            fallas +=1
    
        pregunta3 = input("Mil metros corresponde a: ")
        if pregunta3.lower() == "1km":
            print("La respuesta 3 es correcta")
            monedas += 5000
            aco +=1
            pregunta += 1
        else:
            print("Respuesta incorrecta")
            acof +=1
            fallas +=1
    
        pregunta4 = input("¿Los árboles pueden medir más de 1 metro? ")
        if pregunta4.lower() == "si":
            print("La respuesta 4 es correcta")
            monedas += 5000
            aco +=1
            pregunta += 1
        else:
            print("Respuesta incorrecta")
            acof +=1
            fallas +=1
    
        pregunta5 = int(input("¿Cuánto da una distancia de 10 * 10? "))
        if pregunta5 == 100:
            print("La respuesta 5 es correcta")
            aco +=1
            monedas += 5000
            pregunta += 1
        else:
            print("Respuesta incorrecta")
            acof +=1
            fallas +=1

        if pregunta >= 2:
            print("Nivel superado")
            monedas += 20000
            poderes.append("Daga de la tribu")
            print("Las monedas acumuladas son:", monedas)
            print("Tus poderes son ",poderes)
            print("Tus castigos son ", castigos)
            print("La cantidad de aciertos ", pregunta)
            print("La cantidad de fallas ", fallas)
            
        else:
            print("Condenado a perderte por siempre en la selva.")
            castigos.append("perderse en la selva")
            print("Las monedas acumuladas son:", monedas)
            print("Tus poderes son ",poderes)
            print("Tus castigos son ", castigos)
            print("La cantidad de aciertos ", pregunta)
            print("La cantidad de fallas ", fallas)
            inte +=15

            break
    
    
        while True:
        
            poderes[0] ="Daga de la tribu"
            while True:  
                
                print(monedas)
                fallas = 0
                pregunta = 0
                print("Nivel 2")
                pregunta1 = input("¿El océano es agua? ")
                if pregunta1.lower() == "si":
                    pregunta += 1
                    aco +=1 
                    print("La respuesta es correcta")  
                    monedas += 10000
                else:
                    print("La respuesta es incorrecta")
                    acof +=1
                    fallas +=1
            
                pregunta2 = int(input("¿Cuánto es 2 * 2? "))
                if pregunta2 == 4:
                    pregunta += 1
                    aco +=1 
                    print("La respuesta es correcta")  
                    monedas += 10000
                else:
                    print("La respuesta es incorrecta")
                    acof +=1
                    fallas +=1
            
                pregunta3 = int(input("¿A qué grado está un triángulo rectángulo? "))
                if pregunta3 == 90:
                    aco +=1
                    pregunta += 1 
                    print("La respuesta es correcta")  
                    monedas += 10000
                else:
                    print("La respuesta es incorrecta")
                    acof +=1
                    fallas +=1
            
                pregunta4 = input("¿Un barco puede recorrer 100 km de distancia? ")
                if pregunta4.lower() == "si":
                    pregunta += 1
                    aco +=1 
                    print("La respuesta es correcta")  
                    monedas += 10000
                else:
                    print("La respuesta es incorrecta")
                    acof +=1
                    fallas +=1
            
                pregunta5 = input("¿El humano puede alcanzar la velocidad de un barco? ")
                if pregunta5.lower() == "no":
                    pregunta += 1 
                    aco +=1
                    print("La respuesta es correcta")  
                    monedas += 10000
                else:
                    print("La respuesta es incorrecta")
                    acof +=1
                    fallas +=1
            
                if pregunta >= 3:
                    print("")
                    poderes.append("Mapa de templos")
                    monedas += 30000
                    print("Las monedas acumuladas son:", monedas)
                    print("Tus poderes son ",poderes)
                    print("Tus castigos son ", castigos)
                    print("La cantidad de aciertos ", pregunta)
                    print("La cantidad de fallas ", fallas)
                    break
                    
                print("Las monedas que tienes son:", monedas)
                print("Recuerda que se necesita 40.000 monedas de plata para una segunda y ultima oportunidad")
                res = input("¿Desea obtener otra vida? ") 
                if res.lower() == "no" or monedas < 40000:
                    print("No hay más oportunidades")
                    print("Condenado a morir")
                    castigos.append("condenado a morir")
                    print("Las monedas acumuladas son:", monedas)
                    print("Tus poderes son ",poderes)
                    print("Tus castigos son ", castigos)
                    print("La cantidad de aciertos ", pregunta)
                    print("La cantidad de fallas ", fallas)
                    a +=1
                    break
                elif res.lower() == "si" or monedas >=40000:
                    monedas -= 40000
            if a == 1:
                break
                
            if a==0:
                f=0    
                pregunta = 0
                fallas = 0
                print("Nivel 3: En busca del Amuleto Ancestral")
                pregunta1 = int(input("¿Cuántos huesos tiene el cuerpo? "))
                if pregunta1 == 206:
                    pregunta += 1 
                    aco  +=1
                    print("La respuesta es correcta")  
                    oro += 20000
                else:
                    print("La respuesta es incorrecta")
                    acof +=1
                    fallas +=1
            
                pregunta2 = input("¿La arqueología estudia los huesos? ")
                if pregunta2.lower() == "si":
                    pregunta += 1 
                    aco  +=1
                    print("La respuesta es correcta")  
                    oro += 20000
                else:
                    print("La respuesta es incorrecta")
                    acof +=1
                    fallas +=1
            
                pregunta3 = input("¿Qué es el petróleo? ")
                if pregunta3.lower() == "fosiles":
                    pregunta += 1 
                    aco  +=1
                    print("La respuesta es correcta")  
                    oro += 20000
                else:
                    print("La respuesta es incorrecta")
                    acof +=1
                    fallas +=1
            
                pregunta4 = int(input("¿Cuántas hectáreas puede tener un templo? "))
                if pregunta4 == 90:
                    pregunta += 1 
                    aco  +=1
                    print("La respuesta es correcta")  
                    oro += 20000
                else:
                    print("La respuesta es incorrecta")
                    acof +=1
                    fallas +=1
            
                pregunta5 = int(input("¿Cuál puede ser el resultado del cubo de 3? "))
                if pregunta5 == 27:
                    pregunta += 1
                    aco  +=1 
                    print("La respuesta es correcta")  
                    oro += 20000
                else:
                    print("La respuesta es incorrecta")
                    acof +=1
                    fallas +=1
            
                if pregunta == 5:
                    print("Monedas de plata acumuladas ", monedas)
                
                    oro += 100000
                    print("Monedas de oro aumuladas ", oro)
                    poderes.append("Amuleto")
                    inte += 12
                    print("Las monedas acumuladas son:", monedas)
                    print("Tus monedas de oro son ", oro)
                    print("Tus poderes son ",poderes)
                    print("Tus castigos son ", castigos)
                    print("La cantidad de aciertos ", pregunta)
                    print("La cantidad de fallas ", fallas)
                    f +=1
                elif pregunta >= 3:
                    print("Recuerda que para acceder al nivel 1 son 60.000 monedas de plata")
                    print("Para el segundo nivel son 120.000 monedas de plata")
                    print("Si elijes un numero que no sea 1 o 2 o no tengas monedas suficientes, no podras pasar")
                    print("Tus monedas actuales son:", monedas)
                    respuesta = int(input("¿Desea ir al nivel 1 o 2? "))
                    if pregunta >= 3 and respuesta == 2 and monedas >= 120000:
                
                        monedas -= 120000
                        print("Volverás al nivel 2")
                        
                    elif pregunta >= 3 and respuesta == 1 and monedas >= 60000:
                        inte += 1
                        monedas -= 120000
                        print("Volverás al nivel 1")
                        break
                    else:
                        print("Las fieras te devoran")
                        castigos.append("Fieras te devoran")
                        print("Las monedas acumuladas son:", monedas)
                        print("Tus monedas de oro son ", oro)
                        print("Tus poderes son ",poderes)
                        print("Tus castigos son ", castigos)
                        print("La cantidad de aciertos ", pregunta)
                        print("La cantidad de fallas ", fallas)
                        inte +=12
                        a +=1
                        break
                else:
                    print("Las fieras te devoran")
                    castigos.append("Fieras te devoran")
                    print("Las monedas acumuladas son:", monedas)
                    print("Tus monedas de oro son ", oro)
                    print("Tus poderes son ",poderes)
                    print("Tus castigos son ", castigos)
                    print("La cantidad de aciertos ", pregunta)
                    print("La cantidad de fallas ", fallas)
                    inte +=12
                    a +=1
                    break
                if f ==1:
                    print("Nivel 4: Desafiando las Ruinas Antiguas")
                    pregunta = 0
                    fallas = 0
                    inte = 1
                    pregunta1 = int(input("Cual es el resultado de 10 + 10: "))
                    if pregunta1 == 20:
                        print("Respuesta correcta")
                        pregunta +=1
                        aco  +=1
                    else: 
                        print("Respuesta incorrecta")
                        fallas +=1
                        acof +=1
                    pregunta2 = int(input("el cubo de 2 es: "))
                    if pregunta2 == 4:
                        print("Respuesta correcta")
                        pregunta +=1
                        aco  +=1
                    else: 
                        print("Respuesta incorrecta")
                        fallas +=1
                        acof +=1
                    if pregunta == 2:
                        print("Recibiste la lanza del destino")
                        poderes.append("Lanza del destino")
                        oro +=1000000
                        print("Las monedas acumuladas son:", monedas)
                        print("Tus monedas de oro son ", oro)
                        print("Tus poderes son ",poderes)
                        print("Tus castigos son ", castigos)
                        print("La cantidad de aciertos ", pregunta)
                        print("La cantidad de fallas ", fallas)
                        inte += 12
                        d +=1
                        
                    elif pregunta < 2:
                        print("Tus monedas de plata son: ", monedas)
                        print("Tus monedas de oro son: ", oro)
                        respuesta = ""
                        respuesta = input("Desea volver al nivel uno s/n ")
                        if respuesta == "s" and oro >= 160000 and monedas >=40000:
                            monedas -=40000
                            oro -= 160000
                            print("vuelves al nivel uno")
                            j+=1
                        else:
                            print("consumido por los rios caudalosos")
                            castigos.append("Rios caudalosos")
                            print("Tus monedas de oro son ", oro)
                            print("Tus poderes son ",poderes)
                            print("Tus castigos son ", castigos)
                            print("La cantidad de aciertos ", pregunta)
                            print("La cantidad de fallas ", fallas)
                            inte += 12
                            j+=1
                            a +=1
                            break
                    if d ==1:
                        fallas = 0
                        respuesta = 0
                        pregunta =0
                        a = 0
                        j = 0
                        print("Nivel 5: Confrontación en el Templo Sagrado")  
                        pregunta1 = int(input("el resultado de la multiplicacion 10 *9 "))     
                        if pregunta1 == 90:
                            print("Respuesta correcta")
                            pregunta +=1
                            aco +=1
                        else: 
                            print("Respuesta incorrecta")
                            acof +=1
                            fallas +=1
                        pregunta2 = int(input("cual es el resultado de la resta 10 - 6 ")) 
                        if pregunta2 == 4:
                            print("Respuesta correcta")
                            pregunta +=1
                            aco +=1
                        else: 
                            print("Respuesta incorrecta")
                            acof +=1
                            fallas +=1
                        pregunta3 = input(" 8 * 8 da 25 ")
                        if pregunta3 == "no":
                            print("Respuesta correcta")
                            pregunta +=1
                            aco +=1
                        else: 
                            print("Respuesta incorrecta")
                            acof +=1
                            fallas +=1 
                        if pregunta == 3:
                            print("Felicidades, lograste derrotar al señor oscuro")
                            poderes.append("Maestro explorador")
                            print("Las monedas acumuladas son:", monedas)
                            print("Tus monedas de oro son ", oro)
                            print("Tus poderes son ",poderes)
                            print("Tus castigos son ", castigos)
                            print("La cantidad de aciertos ", pregunta)
                            print("La cantidad de fallas ", fallas)
                            j +=1
                            a +=1
                        else:
                            print("No lograste derrotar al señor oscuro")
                            castigos.append("Perdedor")
                            print("Las monedas acumuladas son:", monedas)
                            print("Tus monedas de oro son ", oro)
                            print("Tus poderes son ",poderes)
                            print("Tus castigos son ", castigos)
                            print("La cantidad de aciertos ", pregunta)
                            print("La cantidad de fallas ", fallas)
                            j +=1
                            a +=1

                        if len(castigos) >=3:
                            print("por tus castigos, fuiste condenado ha quedar atrapado por el señor oscuro")        
                            print("Las monedas acumuladas son:", monedas)
                            print("Tus monedas de oro son ", oro)
                            print("Tus poderes son ",poderes)
                            print("Tus castigos son ", castigos)
                            print("La cantidad de aciertos ", pregunta)
                            print("La cantidad de fallas ", fallas)
                            print("Cantidad de aciertos acomulados ", aco)
                            print("Cantidad de desaciertos acomulados ", acof)
                            print("Gracias por jugar")
                        # elif len(poderes) == 5:
                        #     print("Por pasar todos los desafios con exito, te convertiste en un super sagrado")
                        #     print("Las monedas acumuladas son:", monedas)
                        #     print("Tus monedas de oro son ", oro)
                        #     print("Tus poderes son ",poderes)
                        #     print("Tus castigos son ", castigos)
                        #     print("La cantidad de aciertos ", pregunta)
                        #     print("La cantidad de fallas ", fallas)
                        #     print("Cantidad de aciertos acomulados ", aco)
                        #     print("Cantidad de desaciertos acomulados ", acof)
                        #     print("Gracias por jugar")
                        # else:
                        #     print("Haz pasado el juego con exito,  felicidades")
                        #     print("Las monedas acumuladas son:", monedas)
                        #     print("Tus monedas de oro son ", oro)
                        #     print("Tus poderes son ",poderes)
                        #     print("Tus castigos son ", castigos)
                        #     print("La cantidad de aciertos ", pregunta)
                        #     print("La cantidad de fallas ", fallas)
                        #     print("Cantidad de aciertos acomulados ", aco)
                        #     print("Cantidad de desaciertos acomulados ", acof)
                        #     print("Gracias por jugar")
                    if j>0:
                        break
        if a >0:
            break