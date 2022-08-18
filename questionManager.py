import os
###!!! notas!!! se actualizaran los archivos, al encender el bot, y cuando se registre una nueva respuesta.
### la actualizacion tomara la lista antes creada y checkeara si el nombre de archivo no esta en la lista



#Crear funcion que actualice y ordene los archivos de respuesta, para llamarla cuando se se escriban preguntas, se busquen o escriban respuestas

def actualizar_lista_respuestas():

    preguntas_lista = []

    ###codigo robado revisa archivos .txt que tengan cierto formato
    for file in os.listdir():
        if file.startswith("0") and file.endswith(".txt"):
            print(file)   #impime el nombre del archivo
            preguntas_lista.append(file[:len(file)-4])
            preguntas_lista.sort(key=ordenar_p)

    if len(preguntas_lista) != 0:
        for x in preguntas_lista:
            n_archivo = x+".txt"
            abrir = open(n_archivo, "r")
            leer_lineas = abrir.readlines()
            abrir.close()

            texto = ""

            for y in leer_lineas:
                texto = texto + y.strip("\n")
            #transformamos texto a objeto pregunta
            objeto = texto.split(";;;")

            preguntas_lista[int(x)] = pregunta(x,objeto[0],objeto[1],objeto[2])
    return(preguntas_lista)

def ordenar_p(p):
    numero = int(p)
    return(numero)



###Crear objeto pregunta###
class pregunta:
    def __init__(self, codigo, enunciado, palabras_clave, respuestas):
        self.enunciado = enunciado
        self.palabras_clave = palabras_clave.split(";;")
        self.respuestas = respuestas.split(";;")
        self.codigo = codigo

    def __str__(self):
        return (self.codigo)

    def objeto_a_str(self):
        texto = self.codigo + ";;;" + self.enunciado + ";;;"
        for z in self.palabras_clave:
            texto = texto + z + ";;"
        texto = texto + ";"
        for z in self.respuestas:
            texto = texto + z + ";;"
        texto = texto + ";"

        return texto


    def escribir_objeto(self):
        titulo = str(self.codigo)+".txt"
        abrir = open(titulo, "w")
        print(self.objeto_a_str(),  file=abrir)
        abrir.close()

    #metodo que devuelva un string trabajable para hacerlo objeto.


    def escribir_pregunta(self):
        mensaje = "**Pregunta: " + self.codigo +"** \n Tags: "
        tags = ""
        for x in self.palabras_clave:
            tags+= "["+x+"] "
        mensaje+= tags + "\n" + self.enunciado

        respuesta = "Respuesta(s): \n"
        if len(self.respuestas) == 1:
            respuesta += self.respuestas[0]
        else:
            for x in range(1,len(self.respuestas)):
                respuesta += "Respuesta "+ str(x) + ": "+self.respuestas[x] + "\n"



        return [mensaje,respuesta]
