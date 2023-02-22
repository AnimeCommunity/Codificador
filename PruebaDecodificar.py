import ventasnasPrueba as ventana

from tkinter import *
raiz = Tk()

var = StringVar()

import os

#VINCULAR MySQL con el programa
#nue = []
#nue = nue.push(clave)

#---------------------funciones-----------------------

fName = r"clavesDecodificadas.txt"
if os.path.isfile(fName):
    print("Existe el archivo")
else:
    res = open("clavesDecodificadas.txt", "w")
    res.write("Gracias por usar la herramienta de decodificacion")
    res.close()

def Mostrar():
    ruta = "/clavesDecodificadas.txt"

    Image.open(ruta).show()

def suma():
    #Decodifiacion

    mensaje_cifrado = textoAcodificar.get()
    cadedeco = ""    #cadenacodificada = ""
    cla_num = int(numeroClave.get()) #desplazamiento = int(numeroClave.get())

    for letra in mensaje_cifrado:
        cadedeco = cadedeco + chr(ord(letra) - cla_num)


    # Convertir mensaje a cadena
    msj = str(mensaje_cifrado)
    clu = list(msj)
    pista = clu[0:3]
    clue = ''.join([str(elem) for elem in pista])

    #Guardar clave

    numCla = str(cla_num)
    cod = str(cadedeco)

    nue = open("clavesDecodificadas.txt", "a")
    #Se muestra primero la clave cifrada
    nue.write(os.linesep + "Esta es tu clave decifrada: ")
    nue.write(cod)

    #Se muestra las iniciales de la clave
    nue.write(os.linesep + "Esta es tu clave codificada: ")
    nue.write(clue + "...")

    #Se muestra la clave numerica
    nue.write(os.linesep + "Esta es tu clave numerica de cifrado: ")
    nue.write(numCla)

    # un entrelineado entre claves
    nue.write(os.linesep + "-------------------------------")

    nue.close()


    return var.set(cadedeco)


#-----------------------------------------------------

miframe = Frame(raiz)
miframe.pack()
#--------------codificacion
miLabel = Label(miframe)

tituloLabel= Label(miframe, text="Decodificacion")
tituloLabel.grid(row=1, column=1, columnspan=2)


textoAcodificar = Entry(miframe)
textoAcodificar.grid(row = 2, column =1, padx = 10, pady = 10)

decodificarLabel = Label(miframe, text = "Que quieres decodificar: ")
decodificarLabel.grid(row = 2, column = 0, sticky = "n", padx = 10, pady = 10)




numeroClave = Entry(miframe)
numeroClave.grid(row = 3, column =1, padx = 10, pady = 10)

claveLabel = Label(miframe, text = "Ingresa el numero de cifrado ")
claveLabel.grid(row = 3, column = 0, sticky = "n", padx = 10, pady = 10)


botonEnvio=Button(miframe, text = "decodificado", command=suma)
botonEnvio.grid(row = 4, column = 1, columnspan=2, padx = 10, pady = 10)



mostrarLabel = Entry(miframe, textvariable=var)
mostrarLabel.grid(row = 5, column = 1, sticky = "n", padx = 10, pady = 10)
mostrarLabel.config(background="light blue")


showLabel = Label(miframe, text = "Su clave cifrada: ")
showLabel.grid(row = 5, column = 0, sticky = "n", padx = 10, pady = 10)





raiz.mainloop()