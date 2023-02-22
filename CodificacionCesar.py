
codificar = True
while codificar:
        codificar = str(input("¿Quieres cifrar algo? (S/N) "))
        if codificar == "S" or codificar == "s" or codificar == "":
            mensaje = input("Ingresa tu mensaje: ")
            cadenacodificada = ""
            desplazamiento = int(input("Ingresa la clave numerica: "))
            for letra in mensaje:
                cadenacodificada = cadenacodificada + chr(ord(letra) + desplazamiento)


            print(cadenacodificada)


        if codificar == "N" or codificar== "n":
            codificar = False

        else:
            print("selecciona una nueva opcion: ")
            codificar = True



cambiar = True

while cambiar:

        escribir_mensaje = str(input("¿Deseas decofificar un mensaje? (S/N) "))

        if escribir_mensaje == "S" or escribir_mensaje == "s" or escribir_mensaje == "":
            mensaje_cifrado = input("Ingresa tu mensaje: ")
            cadedeco = ""

            cla_num = int(input("Ingresa la clave numerica: "))

            for letra in mensaje_cifrado:
                cadedeco = cadedeco + chr(ord(letra) - cla_num)

            print("Tu mensaje significa: ",cadedeco)



        if escribir_mensaje == "N" or escribir_mensaje == "n":
            cambiar = False

        else:
            cambiar = True






