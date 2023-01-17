from managerMensajes import actualizarMensaje, crearMensaje,eliminarMensaje,obtenerMensaje
class App:

    def menu(self):
        while True:
            print(
                ' MENU\n'+
                ' 1)Crear mensaje encriptado \n'+
                ' 2)Visualizar mensajes \n'+
                ' 3)Actualizar mensaje\n'+
                ' 4)Eliminar mensaje  \n'+
                ' 5)Salir \n'+
                '^^^^^^^^\n'+
                '^^^^^^^^\n'+
                '^^^^^^^^\n')

            option = input("Elige una opción: ")
            if option == "1":
                mensaje = input('Imgrese un mensaje que desee encriptar:')
                crearMensaje(mensaje)
            elif option == "2":
                obtenerMensaje()
            elif option == "3":
                _id = input("Ingrese id del mensaje para actualizar:")
                nuevoMensaje = input("Ingrse mensaje nuevo:")
                actualizarMensaje(_id,nuevoMensaje)
            elif option == "4":
                eliminarMensaj_e = input("Ingrese id del mensaje:")
                eliminarMensaje(eliminarMensaj_e)
            elif option == "5":
                break
            else:
                print("Opcion invalida")

App().menu()