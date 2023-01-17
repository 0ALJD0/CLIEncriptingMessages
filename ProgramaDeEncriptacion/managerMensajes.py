#Importamos la base de datos del archvo dbconnect.py
from dbconnect import awaDB
#Importamos  para la id de los objetos de la base de datos MongoDb
from bson.objectid import ObjectId
#Import para encryptar el mensaje creado
##DEBEMOS DE INSTALAR CON PIP cryptography y fernet
from cryptography.fernet import Fernet
#Inicializamos las variables que nos permitirá crear la colección en la DB
encryptynDB = awaDB.client['EncryptynDB']
coleccionEncryptynDB = encryptynDB['MensajeEncriptado']



    
    # Inivializamos una lista que almacenará todos los documentos de nuestra colección MensajeEncriptado
_ListaDeMensajes = []

    # Metodo para crear el mensaje, pedimos al usuario que ingrese el mensaje, y luego lo encriptamos y subimos 
    #a la DB para luego mostrarselo
def crearMensaje( mensaje):
    try:
        # Generar una clave en formato de secuencia de bytes:
        llave = Fernet.generate_key()
        objetoEncripcion = Fernet(llave)
        textoEncriptado = objetoEncripcion.encrypt(str.encode(mensaje))
        print("Mensaje Encriptado: ",textoEncriptado)
        textoDesencriptadoBytes = objetoEncripcion.decrypt(textoEncriptado)
        textoDesencriptado = textoDesencriptadoBytes.decode()
        print("Mensaje desencriptado: ", textoDesencriptado)
        __data = {"MensajeEncriptado": textoEncriptado, "Mensaje":textoDesencriptado, "status": True}
        coleccionEncryptynDB.insert_one(__data)
    except TypeError as messageTypeError:
        print("Error al crear => " + messageTypeError)


# Metodo obtenerMensaje, donde le mostraremos al usuario todos los documentos, es decir, los mensajes encriptados.
def obtenerMensaje():
    try:
        print("\t\t\tLista de mensajes")
        for mensaje in coleccionEncryptynDB.find():
            _ListaDeMensajes.append(mensaje)
            print("id:",mensaje['_id'],"status: ", mensaje['status'],"Mensaje: ",mensaje['Mensaje'],
                "\nMensajeEncriptado: ", mensaje['MensajeEncriptado'],"\n");
            
    except TypeError as messageTypeError:
        print("Error al obtener los objetos => No hay datos.")

# Metodo actualizarMensaje, este hará lo mismo que el metodo crear, solo que en vez de crear desde cero
#pedirá al usuario la id de uno de los mensajes y de esta forma se pueda actualizar su contenido.
def actualizarMensaje( id, mensaje):
    try:
        MensajeElegido = coleccionEncryptynDB.find_one({"_id":ObjectId(id)})
        if MensajeElegido:
            # ?Generar una clave en formato de secuencia de bytes:
            llave = Fernet.generate_key()
            objetoEncripcion = Fernet(llave)
            textoEncriptado = objetoEncripcion.encrypt(str.encode(mensaje))
            print("Mensaje cifrado",textoEncriptado)
            textDecryptedBytes = objetoEncripcion.decrypt(textoEncriptado)
            textDecrypted = textDecryptedBytes.decode()
            print("Mensaje desencriptado: ", textDecrypted)
            actualizarMensaje = coleccionEncryptynDB.update_one({"_id":ObjectId(id)}, {"$set": {"MensajeEncriptado": textoEncriptado, "Mensaje":textDecrypted}})
        else:
            print("No se encontro el id del mensaje.")
    except TypeError as messageTypeError:
        print("Error al Actualizar Mensaje => No se encontro el id del mensaje.")

# Metodo eliminarMensaje, en este le pedirá al usuario que ingrese el id de un documento, es decir, un mnesaje
# , de esta forma se eliminará de la DB el mensaje
def eliminarMensaje( id):
    try:
        MensajeElegido = coleccionEncryptynDB.find_one({"_id":ObjectId(id)})
        if MensajeElegido:
            eliminarMensaje = coleccionEncryptynDB.delete_one({"_id":ObjectId(id)})
            print("Se elimino mensaje exitosamente.")
        else:
            print("No se encontro el id del mensaje.")

    except TypeError as messageTypeError:
        print("ErrorDelete => No se encontro el mensaje")



