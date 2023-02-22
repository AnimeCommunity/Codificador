import ventasnasPrueba as ventana

from tkinter import *

import os

from tkinter import filedialog

from tkinter.filedialog import askopenfilename

raiz = Tk()

var = StringVar()


# diccionarios, crear variables y las etiquetas
# lista

#---------------------funciones-----------------------

fName = r"resultado.txt"
if os.path.isfile(fName):
    print("Hola")
else:
    resultado = open("resultado.txt","w")
    resultado.write("Gracias por usar la herramienta suma")
    resultado.close()

def suma():

    a = int(textoCodificar.get())
    b = int(numeroClave.get())

    sumar = a + b

    resul = open("resultado.txt", "a")
    resul.write(os.linesep + "Este es tu resultado: ")
    sumacion = str(sumar)
    resul.write(str(sumacion))
    resul.close()

    return var.set(sumar)
#Para seleccionar archivos
#def abrir():
#    filename = askopenfilename()


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


