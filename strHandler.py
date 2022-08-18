
def limpiar_mensaje(mensaje): #pasar este filtro para documentacion y preguntas
    clave_invalidez="\/;" #que nadie me vaya a matar el codigo o algo con un \ o un ;
    for i in range(0,len(mensaje)):
        if mensaje[i] in clave_invalidez[0]:
            mensaje=mensaje[:i]+mensaje[i+1:]

    return(mensaje)

def seleccionar_palabras(mensaje): #encontrar palabras buscando los espacios

    palabras=[]
    palabra=""
    #empezamos a añadir las palabras a la lista
    for e in range(0,len(mensaje)):
        if mensaje[e] == " ":
            if palabra not in palabras:
                palabras.append(palabra)

            palabra=""
        else:
            palabra = palabra + (mensaje[e]).upper()
            palabra.upper()
    if palabra not in palabras:
        palabras.append(palabra)


    #comprobar validez, ¿son conectores?, palabras en una lista de conectores? si no validarla
    #crear una lista con las palbras
    #¿clave para buscar frases literales?
    #añadir palabras encontradas a lista para tirar a los buscadores,
    return(palabras)
#def seleccionar_frases(mensaje):
