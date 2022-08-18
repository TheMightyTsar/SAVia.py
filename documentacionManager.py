def docu_palabras_claves(palabras):
    lineas_a_devolver = []
    lectura_docu = open("documentacion.txt", "r")
    contenido=lectura_docu.readlines()

    for e in palabras:
        i = 0
        encontrar = False
        while encontrar == False:
            linea=contenido[i]
            #print(linea[:len(e)])

            if e == linea[:len(e)]:
                conjunto= linea[len(e):]+"\n" #modificar esto
                #lineas_a_devolver.append("**"+linea)
                x = i+1
                while (contenido[x])[:4] != "----":
                    #lineas_a_devolver.append(contenido[x])
                    conjunto=conjunto+contenido[x]+"\n"
                    x+=1


                encontrar = True
                lineas_a_devolver.append(conjunto)

                #agregar lineas hasta que se encuentre con una linea que tenga un "signo" de cierre

            i += 1
    lectura_docu.close()


    return (lineas_a_devolver)

#funcion para encontrar todos los codigos disponibles
def codigo_disponible():
    codigos_leer = open("documentacion.txt","r")
    codigos_disp = []
    leer = codigos_leer.readlines()
    for x in leer:
        print(x)

        i = 0
        largox=len(x)
        encontrado = False
        while encontrado == False:

            if (x[i:i+2] != "**") and (largox > i):
                i += 1
                print(i)
                print(largox > i)
            elif x[:i+1].isupper():

                codigo = "**" + x[:i+2]
                print(codigo)
                codigos_disp.append(codigo)
                encontrado = True
            else:
                encontrado = True




        print("salio del while")
    codigos_leer.close()
    print("salio del for in")
    return(codigos_disp)