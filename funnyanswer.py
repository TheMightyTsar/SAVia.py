def mandarfunny(mensaje):
    Open_txt = open("comedia.txt")
    lineas_txt = Open_txt.readlines()
    Open_txt.close()
    triggers = []
    respuesta = ""
    for i in lineas_txt:
        triggers.append(i.strip())

    for x in range(0,len(triggers)):
        if triggers[x] == mensaje[:]:
            respuesta = triggers[x+1][4:]
    return respuesta

def escribirfunny(ayudante,frase):
    #chequear role en main, ayudante = Bool
    if ayudante:
        ###abrir el archivo para no se reinicie con el write
        Open_txt = open("comedia.txt")
        lineas_txt = Open_txt.readlines()
        Open_txt.close()

        #############

        #split, buscar elemento para separar el trigger y la respuesta
        trigger = " https://"
        frase = frase.split(trigger)
        frase[1] = "----https://"+frase[1]
        #usar split para dividir mensaje que activa y respuesta(imagen/video/link etc)
        Open_txt = open("comedia.txt", "w")
        for i in lineas_txt:
            print(i,file=Open_txt)
        print(frase[0],file=Open_txt)
        print(frase[1],file=Open_txt)
        Open_txt.close()



