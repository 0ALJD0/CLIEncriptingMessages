import pymongo
# #*Conexion a MongoDB
from  pymongo import MongoClient
# #*Variables de entorno
#install python-dotenv python-decouple
from decouple import  config


class awaDB:
    try:
        client = MongoClient(config('DBCONNECT'), serverSelectionTimeoutMS = config('MONGO_TIME_OUTSIDE'))
        client.server_info()
        print('¡Base de datos conectada!')
    except pymongo.errors.ServerSelectionTimeoutError as errorType:
        print("Añadiendo tiempo de espera:" + errorType)
    except pymongo.errors.ConnectionError as errorConnection:
        print("No se logró la conexión con la DB:" + errorConnection)