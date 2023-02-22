from tkinter import *

raiz = Tk()

miNombre = StringVar()


miFrame = Frame(raiz, width = 1200, height = 600)
miFrame.pack()
cuadroTexto = Entry(miFrame, textvariable=miNombre)
cuadroTexto.grid(row = 0, column =1, padx = 10, pady = 10)

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row = 1, column =1, padx = 10, pady = 10)

cuadroPass = Entry(miFrame)
cuadroPass.grid(row = 2, column =1, padx = 10, pady = 10)
cuadroPass.config(show = "*")
#con show podemos hacer que lo que se muestra en la casilla sean * cuando ingresamos algo

textoComentario = Text(miFrame, width = 16, height = 5)
textoComentario.grid(row = 3, column =1, padx = 10, pady = 10)
#aqui creamos la barra de scroll osea la tipica barra para ver el contenido de un cadro de texto
scrollvert =Scrollbar(miFrame, command= textoComentario.yview)
scrollvert.grid(row=3, column = 2, sticky ="nsew")
#scrollvert.grid es para ubicar el scroll al lado de la caja de comentarios, el stickey es para que se
#adapte a lo largo de la caja de comenarios
textoComentario.config(yscrollcommand=scrollvert.set)
#esta pequeña configuracion es para que la barr de scroll vaya bajando/apareciendo donde yo escribo


nombreLabel = Label(miFrame, text = "Nombre: ")
nombreLabel.grid(row = 0, column = 0, sticky = "w", padx = 10, pady = 10)
#Sticky es para ubicar el contenido hacia aun lado, N norte, E este, S sur, W oeste, y hay intermedio NW, NE,SW,SE
#grid es para la grilla, ubicar los elementos como si fueran casillas
#padx y pady es para configurar los bordes entre los elementos

ApellidoLabel = Label(miFrame, text = "Apellido: ")
ApellidoLabel.grid(row = 1, column = 0, sticky = "e", padx = 10, pady = 10)

passLabel = Label(miFrame, text = "pais de nacimiento: ")
passLabel.grid(row = 2, column = 0, sticky = "n", padx = 10, pady = 10)

comentariosLabel = Label(miFrame, text = "Comentarios: ")
comentariosLabel.grid(row = 3, column = 0, sticky = "n", padx = 10, pady = 10)

#aca se va a definir la funcion del boton
def codigoBoton():
    miNombre.set("daniel")
botonEnvio=Button(raiz, text = "Enviar comentarios", command=codigoBoton)
botonEnvio.pack()
#esto es para agregar un boton



raiz.mainloop()