#-----------UI------------
from tkinter import *
raiz = Tk()
#----------------codificación-----------
#from CodificacionCesar import *



raiz.title("Ventanas de pruebas")
raiz.iconbitmap("bmo.ico")
raiz.config(bg="light blue")

miframe = Frame(raiz)
miframe.pack()

miLabel = Label(miframe, text ="Bievenido a Codificacion Cesar", font="Arial")
miLabel.config(width="70", height="30", bg = "blue")
miLabel.grid(row=1, column=1, padx=10, pady=10, columnspan=4, sticky ="n")

#-------------contenido----------







raiz.mainloop()