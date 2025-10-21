from BasedeDatos import conexion
from mysql.connector import Error

class Producto:
    def __init__(self):
        self.conexion = conexion()

    def agregarProducto(self, nombreProducto, precioProducto, stockProducto, categoriaProducto):
        if not self.conexion:
            print("No hay conexión con la base de datos.")
            return
        try:
            cursor = self.conexion.cursor()
            sql = """
                INSERT INTO Productos (nombreProducto, precioProducto, stockProducto, categoriaProducto)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (nombreProducto, precioProducto, stockProducto, categoriaProducto))
            self.conexion.commit()
            print("Producto agregado correctamente.")
        except Error as e:
            print(f"Error al agregar producto: {e}")
        finally:
            cursor.close()

    def consultarProductos(self):
        if not self.conexion:
            return []
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM Productos")
            datos = cursor.fetchall()
            print("Consulta de productos exitosa.")
            return datos
        except Error as e:
            print(f"Error al consultar productos: {e}")
            return []
        finally:
            cursor.close()

    def actualizarProducto(self, idProducto, nombre, precio, stock, categoria):
        if not self.conexion:
            return
        try:
            cursor = self.conexion.cursor()
            sql = """
                UPDATE Productos
                SET nombreProducto=%s, precioProducto=%s, stockProducto=%s, categoriaProducto=%s
                WHERE idProducto=%s
            """
            cursor.execute(sql, (nombre, precio, stock, categoria, idProducto))
            self.conexion.commit()
            print("Producto actualizado correctamente.")
        except Error as e:
            print(f"Error al actualizar producto: {e}")
        finally:
            cursor.close()

    def eliminarProducto(self, idProducto):
        if not self.conexion:
            return
        try:
            cursor = self.conexion.cursor()
            sql = "DELETE FROM Productos WHERE idProducto=%s"
            cursor.execute(sql, (idProducto,))
            self.conexion.commit()
            print("Producto eliminado correctamente.")
        except Error as e:
            print(f"Error al eliminar producto: {e}")
        finally:
            cursor.close()

    def valorPorCategoria(self):
        if not self.conexion:
            return []
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT categoriaProducto, SUM(precioProducto * stockProducto) FROM Productos GROUP BY categoriaProducto")
            return cursor.fetchall()
        except Error as e:
            print(f"Error al calcular valor por categoría: {e}")
            return []
        finally:
            cursor.close()

    def valorTotalInventario(self):
        if not self.conexion:
            return 0
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT SUM(precioProducto * stockProducto) FROM Productos")
            total = cursor.fetchone()[0]
            return total if total else 0
        except Error as e:
            print(f"Error al calcular inventario total: {e}")
            return 0
        finally:
            cursor.close()

    def productosStockBajo(self):
        if not self.conexion:
            return []
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM Productos WHERE stockProducto < 5")
            return cursor.fetchall()
        except Error as e:
            print(f"Error al consultar productos con poco stock: {e}")
            return []
        finally:
            cursor.close()
