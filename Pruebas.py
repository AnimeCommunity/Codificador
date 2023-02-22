import ventasnasPrueba as ventana
from MySQLConexion import agregarDatosSQL

from tkinter import *
raiz = Tk()

var = StringVar()

import os


#---------------------funciones-----------------------

fName = r"claves.txt"
if os.path.isfile(fName):
    print("Existe el archivo")
else:
    res = open("claves.txt", "w")
    res.write("Gracias por usar la herramienta de codificacion")
    res.close()

def Mostrar():
    ruta = "/claves.txt"

    Image.open(ruta).show()

def suma():
    #Codifiacion

    mensaje = textoCodificar.get()
    cadenacodificada = ""
    desplazamiento = int(numeroClave.get())
    for letra in mensaje:
        cadenacodificada = cadenacodificada + chr(ord(letra) + desplazamiento)


    # Convertir mensaje a cadena
    msj = str(mensaje)
    clu = list(msj)
    pista = clu[0:3]
    clue = ''.join([str(elem) for elem in pista])

    #Guardar clave

    numCla = str(desplazamiento)
    cod = str(cadenacodificada)

    nue = open("claves.txt", "a")
    #Se muestra primero la clave cifrada
    nue.write(os.linesep + "Esta es tu clave cifrada: ")
    nue.write(cod)

    #Se muestra las iniciales de la clave
    nue.write(os.linesep + "Esta es tu clave original: ")
    nue.write(clue + "...")

    #Se muestra la clave numerica
    nue.write(os.linesep + "Esta es tu clave numerica de cifrado: ")
    nue.write(numCla)

    # un entrelineado entre claves
    nue.write(os.linesep + "-------------------------------")

    nue.close()

    agregarDatosSQL(cod, clue)
    return var.set(cadenacodificada)


#-----------------------------------------------------

miframe = Frame(raiz)
miframe.pack()
#--------------codificacion
miLabel = Label(miframe)

tituloLabel= Label(miframe, text="Codificacion")
tituloLabel.grid(row=1, column=1, columnspan=2)


textoCodificar = Entry(miframe)
textoCodificar.grid(row = 2, column =1, padx = 10, pady = 10)

codificarLabel = Label(miframe, text = "Que quieres codificar: ")
codificarLabel.grid(row = 2, column = 0, sticky = "n", padx = 10, pady = 10)




numeroClave = Entry(miframe)
numeroClave.grid(row = 3, column =1, padx = 10, pady = 10)

claveLabel = Label(miframe, text = "Ingresa el numero de cifrado ")
claveLabel.grid(row = 3, column = 0, sticky = "n", padx = 10, pady = 10)


botonEnvio=Button(miframe, text = "Codificar", command=suma)
botonEnvio.grid(row = 4, column = 1, columnspan=2, padx = 10, pady = 10)



mostrarLabel = Entry(miframe, textvariable=var)
mostrarLabel.grid(row = 5, column = 1, sticky = "n", padx = 10, pady = 10)
mostrarLabel.config(background="light green")


showLabel = Label(miframe, text = "Su clave cifrada: ")
showLabel.grid(row = 5, column = 0, sticky = "n", padx = 10, pady = 10)





raiz.mainloop()