# Importar la clase MongoClient desde el módulo pymongo
from pymongo import MongoClient

# Definir la clase "conexion_mongo"
class conexion_mongo:

    # Constructor de la clase, acepta tres argumentos opcionales (host, db y coleccion)
    def __init__(self, host: str = 'localhost', db: str = 'DbTest', coleccion: str = "ColeccionTest"):
        # Crear una instancia de MongoClient utilizando el valor proporcionado para el parámetro "host"
        self.host = MongoClient(host)

        # Acceder a la base de datos especificada en el parámetro "db" y guardar una referencia a esta base de datos en el atributo "db" de la clase
        self.db = self.host[db]

        # Guardar el nombre de la base de datos especificada en el parámetro "db" en el atributo "nombre_database" de la clase
        self.nombre_database = db

        # Guardar una referencia a la colección especificada en el parámetro "coleccion" en el atributo "coleccion" de la clase
        self.coleccion = self.db[coleccion]

        # Guarda el nombre de la colección que se pasa por parámetro al constructor en el atributo "nameCollection" de la clase
        self.nameCollection = coleccion

    # Función que devuelve la referencia a la colección guardada en el atributo "coleccion"
    def mi_coleccion(self):
        return self.coleccion

    # Función que devuelve una lista de los nombres de todas las colecciones en la base de datos guardada en el atributo "db"
    def List_colecciones(self):
        return self.db.list_collection_names()

    # Función para consultar todos los datos de la colección guardada en el atributo "coleccion" y devuelve una lista con los documentos encontrados
    def ConsultarTodosLosDatos(self):
        lista = []

        # Itera sobre cada documento de la colección utilizando el método "find"
        # y agrega el documento a la lista creada anteriormente
        for dato in self.coleccion.find({},{"_id":0}):
            lista.append(dato)

        return lista

    #Funcion para eliminar una colección de la base de datos
    def EliminarCollection(self):
        #Elimina una colección de la base de datos utilizando el método "drop_collection"
        self.db.drop_collection(self.nameCollection)




