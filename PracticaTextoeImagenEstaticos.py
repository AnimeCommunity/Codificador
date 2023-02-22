from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width = 500, height = 400)

miFrame.pack()
miImagen = PhotoImage(file = "Logo.PNG")

#miLabel = Label(miFrame, text ="Hola tio")
#miLabel.place(x = 100, y = 200)
#miFrame, image = text = "Hola mundo", fg = "Blue", font=("Comic Sans MS", 20)).place(x = 100, y = 200)
Label(miFrame, image = miImagen).place(x = 100, y = 200)




raiz.mainloop()