#LIBRERIA PARA MONGO
#INTALAMOS PYMONGO
import pymongo
#IMPORTAMOS LA FUNCION PARA LA CONEXIÓN CON LA DB DE MONGO
from  pymongo import MongoClient
# #*Variables de entorno
#INSTALAMOS LOS PAQUETES python-dotenv python-decouple
from decouple import  config


class awaDB:
    #UA PEUQEÑA COMPROBACION PARA REALIZAR LA CONEXIÓN
    #O DE EXISTIR ALGÚN ERROR CAPTURARLO Y MOSTRARLO
    try:
        client = MongoClient(config('DBCONNECT'), serverSelectionTimeoutMS = config('MONGO_TIME_OUTSIDE'))
        client.server_info()
        print('¡Base de datos conectada!')
    except pymongo.errors.ServerSelectionTimeoutError as errorType:
        print("Añadiendo tiempo de espera:" + errorType)
    except pymongo.errors.ConnectionError as errorConnection:
        print("No se logró la conexión con la DB:" + errorConnection)