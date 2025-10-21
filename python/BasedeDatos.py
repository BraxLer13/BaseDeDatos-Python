import mysql.connector
def conexion():
    conexion = mysql.connector.connect(host = "localhost", database = "tienda", user = "root", password = "")
    if conexion.is_connected():
        print("Conexión exitosa.")
    else:
        print("Error de conexión.")
    return conexion

