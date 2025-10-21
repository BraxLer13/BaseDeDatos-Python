from BasedeDatos import conexion
from mysql.connector import Error

class Cliente:
    def __init__(self):
        self.conexion = conexion()

    def agregarCliente(self, nombre, apellido, email, historial):
        if not self.conexion:
            print("No hay conexión con la base de datos.")
            return
        try:
            cursor = self.conexion.cursor()
            sql = """
                INSERT INTO Clientes (nombreCliente, apellidoCliente, emailCliente, historialCliente)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (nombre, apellido, email, historial))
            self.conexion.commit()
            print("Cliente agregado correctamente.")
        except Error as e:
            print(f"Error al agregar cliente: {e}")
        finally:
            cursor.close()

    def consultarClientes(self):
        if not self.conexion:
            return []
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM Clientes")
            datos = cursor.fetchall()
            print("Consulta de clientes exitosa.")
            return datos
        except Error as e:
            print(f"Error al consultar clientes: {e}")
            return []
        finally:
            cursor.close()

    def actualizarCliente(self, idCliente, nombre, apellido, email, historial):
        if not self.conexion:
            return
        try:
            cursor = self.conexion.cursor()
            sql = """
                UPDATE Clientes
                SET nombreCliente=%s, apellidoCliente=%s, emailCliente=%s, historialCliente=%s
                WHERE idCliente=%s
            """
            cursor.execute(sql, (nombre, apellido, email, historial, idCliente))
            self.conexion.commit()
            print("Cliente actualizado correctamente.")
        except Error as e:
            print(f"Error al actualizar cliente: {e}")
        finally:
            cursor.close()

    def eliminarCliente(self, idCliente):
        if not self.conexion:
            return
        try:
            cursor = self.conexion.cursor()
            sql = "DELETE FROM Clientes WHERE idCliente=%s"
            cursor.execute(sql, (idCliente,))
            self.conexion.commit()
            print("Cliente eliminado correctamente.")
        except Error as e:
            print(f"Error al eliminar cliente: {e}")
        finally:
            cursor.close()

    def totalComprasPorCliente(self):
        if not self.conexion:
            return []
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT nombreCliente, SUM(historialCliente) FROM Cliente GROUP BY nombreCliente")
            return cursor.fetchall()
        except Error as e:
            print(f"Error al calcular total de compras: {e}")
            return []
        finally:
            cursor.close()

    def valorTotalCompras(self):
        if not self.conexion:
            return 0
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT SUM(historialCliente) FROM Clientes")
            total = cursor.fetchone()[0]
            return total if total else 0
        except Error as e:
            print(f"❌ Error al calcular valor total: {e}")
            return 0
        finally:
            cursor.close()
