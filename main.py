import discord
import strHandler as strH
import documentacionManager as dM
import funnyanswer as funny
# import errorManager as eM

import questionManager as qM

lista_preguntas_main = qM.actualizar_lista_respuestas()[:]
print(lista_preguntas_main)

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)




    async def on_message(self, message, lista_preguntas_main=None):
        print(message)
        lectura_id = open("base_ids.txt", "r")
        leer_id = lectura_id.read()
        # obtener id del usuario, si no esta en la lista mandarle las istrucciones del bot
        if message.author == self.user:
            return

        ###trabajar el funnyanswer
        if funny.mandarfunny(message.content) !="":
            await message.channel.send(funny.mandarfunny(message.content))
            await message.channel.send("\n **comedia+=1**")

        if (str(message.author.id) not in leer_id):

            nueva_base_id = leer_id + "\n" + str(message.author.id) + " \n"

            escritura_id = open("base_ids.txt", "w")
            escritura_id.write(nueva_base_id)
            print("despues de grabado" + "\n" + nueva_base_id)

            mensaje_bienvenida = "**" + message.author.name + "**" + " no te conozco, me presento soy SAVia y vengo a ayudarte con tu ramo IIC1103 \n"  # añadir como usar sus comandos
            #agregar mas cosas al mensaje de bienvenida
            help=open("instrucciones.txt","r")
            y=0
            help_m = ""
            help_txt = help.readlines()
            while (help_txt[y])[:4] != "*---":
                help_m = help_m + help_txt[y] + "\n"
                y+=1

            await message.channel.send(mensaje_bienvenida)
            await message.channel.send(help_m)
            escritura_id.close()
            lectura_id.close()
        else:
            if message.content == "help savia":
                help = open("instrucciones.txt", "r")
                y = 0
                help_m = ""
                help_txt = help.readlines()
                while (help_txt[y])[:4] != "*---":


                    help_m = help_m + help_txt[y] + "\n"
                    y+=1

                await message.channel.send(help_m)

            # ver porque tira a else

            mensaje = (str(message.content))

            mensaje = strH.limpiar_mensaje(mensaje)

            if mensaje[:9] == "oh savia ":




                mensaje = mensaje[9:]
                #añadir pregunta trigger
                if mensaje.startswith("add ¿?"):
                    await message.channel.send("paso por ¿?")
                    lista_preguntas_main = qM.actualizar_lista_respuestas()[:]
                    mensaje = mensaje[6:]

                    #importar questionManager y crear el objeto pregunta

                    codigo = "0" + str(len(lista_preguntas_main))

                    mensaje = mensaje.split(";;;")

                    pregunta_agregar = qM.pregunta(codigo,mensaje[0],mensaje[1],"aun no se han agregado respuestas :(")
                    pregunta_agregar.escribir_objeto()
                    await message.channel.send("se ha agregado tu respuesta al sistema :D")

                    lista_preguntas_main = qM.actualizar_lista_respuestas()[:]


                #buscar pregunta, opcion por tag, codigo contenido
                if mensaje.startswith("buscar "):
                    mensaje = mensaje[7:]


                #busca error, si es que esta registrado
                if mensaje[:5] == "error":
                    await  message.channel.send("funciona error")

                    # no usar strHandler borra info de los errores

                elif mensaje[0:4] == "info":
                    # await message.channel.send("funciona info")
                    palabras = strH.seleccionar_palabras(mensaje[5:])
                    print("variable palabras")
                    print(palabras)
                    mandar = dM.docu_palabras_claves(palabras)  # lineas del archivo a imprimir
                    print("variable mandar ")
                    print(mandar)
                    for e in mandar:
                        await message.channel.send(str(e))
                elif mensaje[0:4] == "list":
                    print("entro a list")
                    mandar = "tenemos definicion para... \n "
                    lista = (dM.codigo_disponible())[:]
                    print(lista)
                    mandar = mandar + "**CODIGO:** \n"
                    for i in lista:
                        mandar = mandar + i +"\n"
                    #cubre aspectos de la documentacion



                    await message.channel.send(mandar)

                elif mensaje[:3] == "add fun":
                    #lista con quienes pueden agregar en un archv, "managment roles"
                    #revisar codigo de la api, ver el objeto, message.author.roles.name = tester
                    #llamar escribirfunny(bool,frase)
                    #bool True si esta en la lista

                    roles = open("managment roles.txt")
                    L_roles = roles.readlines()
                    roles.close()

                    for i in range(0,len(L_roles)):
                        L_roles[i]=L_roles[i].strip()



                    seguir = True
                    x = 0

                    while seguir:
                        if message.author.roles[x].name in L_roles:
                            funny.escribirfunny(True,mensaje[4:])
                            seguir = False

                            await message.channel.send("agregada la respuesta")
                        if x > len(message.author.roles):
                            seguir = False
                            await message.channel.send("no tienes permitido crear respuestas funny")
                        x+=1



                    '''
                    leer_documentacion = open("documentacion.txt","r")
                    for e in mandar:
                        e = int(e)
                        print("e",e)
                        await  message.channel.send(leer_documentacion.readline()[e])

                    await  message.channel.send(mandar)
                    '''


                    # mensaje = mensaje[4:]

                    # palabras =strH.seleccionar_palabras(mensaje)



intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)

#process to keep my key secret
def obtenerkey():

    abrir_key = open("key.txt", "r")
    leer_key = abrir_key.readlines()
    leer_key = str(leer_key[0])
    abrir_key.close()
    return leer_key
#end of the process
client.run(obtenerkey())
