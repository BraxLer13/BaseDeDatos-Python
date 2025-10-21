import tkinter as Ventana
from Producto import Producto
from Cliente import Cliente


class interfaz:
    def __init__(self):
        self.producto = Producto()
        self.cliente = Cliente()
        self.formulario = " "

        self.entryIdP = " "
        self.entryNombreP = " "
        self.entryPrecioP = " "
        self.entryStockP = " "
        self.entryCategoriaP = " "

        self.entryIdC = " "
        self.entryNombreC = " "
        self.entryApellidoC = " "
        self.entryEmailC = " "
        self.entryHistorialC = " "

    def getIdP(self): 
        return self.entryIdP.get()
    
    def getNombreP(self): 
        return self.entryNombreP.get()
    
    def getPrecioP(self): 
        return self.entryPrecioP.get()
    
    def getStockP(self): 
        return self.entryStockP.get()
    
    def getCategoriaP(self): return self.entryCategoriaP.get()

    def setIdP(self, valor):
        self.entryIdP.delete(0, 'end')
        self.entryIdP.insert(0, valor)

    def setNombreP(self, valor):
        self.entryNombreP.delete(0, 'end')
        self.entryNombreP.insert(0, valor)

    def setPrecioP(self, valor):
        self.entryPrecioP.delete(0, 'end')
        self.entryPrecioP.insert(0, valor)

    def setStockP(self, valor):
        self.entryStockP.delete(0, 'end')
        self.entryStockP.insert(0, valor)

    def setCategoriaP(self, valor):
        self.entryCategoriaP.delete(0, 'end')
        self.entryCategoriaP.insert(0, valor)


    def getIdC(self): 
        return self.entryIdC.get()
    
    def getNombreC(self): 
        return self.entryNombreC.get()
    
    def getApellidoC(self): 
        return self.entryApellidoC.get()
    
    def getEmailC(self): 
        return self.entryEmailC.get()
    
    def getHistorialC(self): 
        return self.entryHistorialC.get()

    def setIdC(self, valor):
        self.entryIdC.delete(0, 'end')
        self.entryIdC.insert(0, valor)

    def setNombreC(self, valor):
        self.entryNombreC.delete(0, 'end')
        self.entryNombreC.insert(0, valor)

    def setApellidoC(self, valor):
        self.entryApellidoC.delete(0, 'end')
        self.entryApellidoC.insert(0, valor)

    def setEmailC(self, valor):
        self.entryEmailC.delete(0, 'end')
        self.entryEmailC.insert(0, valor)

    def setHistorialC(self, valor):
        self.entryHistorialC.delete(0, 'end')
        self.entryHistorialC.insert(0, valor)

    # ******** VENTANA PRINCIPAL ***********
    def ventana(self):
        self.formulario = Ventana.Tk()
        self.formulario.title("Gestión Tienda - CRUD")
        self.formulario.geometry("900x700")
        self.formulario.configure(bg="#4F2C2C")  


        contenedor = Ventana.Frame(self.formulario, bg="gray")
        contenedor.pack(expand=True)

        Ventana.Label(contenedor, text="SISTEMA DE TIENDA", font=("Arial", 20, "bold"), bg="#1E1E1E", fg="white").pack(pady=15)
        Ventana.Button(contenedor, text="Productos", bg="green", fg="white", width=25, font=("Arial", 12), command=lambda: self.productos()).pack(pady=5)
        Ventana.Button(contenedor, text="Clientes", bg="blue", fg="black", width=25, font=("Arial", 12), command=lambda: self.clientes()).pack(pady=5)

        return self.formulario

    # ******** PRODUCTOS ********
    def productos(self):
        ventana = Ventana.Toplevel()
        ventana.title("Productos")
        ventana.geometry("750x650")
        ventana.configure(bg="#2ebc3a")  

        Ventana.Label(ventana, text="GESTIÓN DE PRODUCTOS", font=("Arial", 18, "bold"), bg="#2ebc3a", fg="black").pack(pady=10)

        Ventana.Label(ventana, text="Nombre:", bg="#2ebc3a", fg="black").pack()
        self.entryNombreP = Ventana.Entry(ventana, width=40)
        self.entryNombreP.pack()

        Ventana.Label(ventana, text="Precio:", bg="#2ebc3a", fg="black").pack()
        self.entryPrecioP = Ventana.Entry(ventana, width=40)
        self.entryPrecioP.pack()

        Ventana.Label(ventana, text="Stock:", bg="#2ebc3a", fg="black").pack()
        self.entryStockP = Ventana.Entry(ventana, width=40)
        self.entryStockP.pack()

        Ventana.Label(ventana, text="Categoría:", bg="#2ebc3a", fg="black").pack()
        self.entryCategoriaP = Ventana.Entry(ventana, width=40)
        self.entryCategoriaP.pack()

        Ventana.Label(ventana, text="ID:", bg="#2ebc3a", fg="black").pack()
        self.entryIdP = Ventana.Entry(ventana, width=20)
        self.entryIdP.pack()

        resultado = Ventana.Label(ventana, text="", bg="#2ebc3a", fg="black", font=("Arial", 11))
        resultado.pack(pady=10)

        # Botones CRUD
        Ventana.Button(ventana, text="Agregar", bg="green", fg="white", width=15, command=lambda: self.agregarProducto(self.entryNombreP, self.entryPrecioP, self.entryStockP, self.entryCategoriaP, resultado)).pack(pady=3)
        Ventana.Button(ventana, text="Consultar", bg="blue", fg="white", width=15, command=lambda: self.consultarProductos(resultado)).pack(pady=3)
        Ventana.Button(ventana, text="Actualizar", bg="orange", fg="black", width=15, command=lambda: self.actualizarProducto(self.entryIdP, self.entryNombreP, self.entryPrecioP, self.entryStockP, self.entryCategoriaP, resultado)).pack(pady=3)
        Ventana.Button(ventana, text="Eliminar", bg="red", fg="white", width=15, command=lambda: self.eliminarProducto(self.entryIdP, resultado)).pack(pady=3)

        Ventana.Button(ventana, text="Valor total inventario", bg="purple", fg="white", width=25, command=lambda: self.valorInventario(resultado)).pack(pady=3)
        Ventana.Button(ventana, text="Valor por categoría", bg="yellow", fg="black", width=25, command=lambda: self.valorPorCategoria(resultado)).pack(pady=3)
        Ventana.Button(ventana, text="Productos con stock bajo", bg="brown", fg="white", width=30, command=lambda: self.productosStockBajo(resultado)).pack(pady=3)

    # ********* FUNCIONES PRODUCTOS ********
    def agregarProducto(self, nombre, precio, stock, categoria, label):
        try:
            self.producto.agregarProducto(nombre.get(), float(precio.get()), int(stock.get()), categoria.get())
            label.config(text="Producto agregado correctamente")
        except:
            label.config(text="Error al agregar producto")
        finally:
            self.setNombreP("")
            self.setPrecioP("")
            self.setStockP("")
            self.setCategoriaP("")

    def consultarProductos(self, label):
        try:
            datos = self.producto.consultarProductos()
            texto = "\n".join(str(fila) for fila in datos)
            label.config(text=texto)
        except:
            label.config(text="Error al consultar productos")

    def actualizarProducto(self, idp, nombre, precio, stock, categoria, label):
        try:
            self.producto.actualizarProducto(int(idp.get()), nombre.get(), float(precio.get()), int(stock.get()), categoria.get())
            label.config(text=f"Producto {idp.get()} actualizado")
        except:
            label.config(text="Error al actualizar producto")
        finally:
            self.setIdP("")
            self.setNombreP("")
            self.setPrecioP("")
            self.setStockP("")
            self.setCategoriaP("")

    def eliminarProducto(self, idp, label):
        try:
            self.producto.eliminarProducto(int(idp.get()))
            label.config(text=f"Producto {idp.get()} eliminado")
        except:
            label.config(text="Error al eliminar producto")
        finally:
            self.setIdP("")

    def valorInventario(self, label):
        try:
            total = self.producto.valorTotalInventario()
            label.config(text=f"Valor total del inventario: {total}")
        except:
            label.config(text="Error al calcular inventario")

    def valorPorCategoria(self, label):
        try:
            datos = self.producto.valorPorCategoria()
            texto = "\n".join(f"Categoría: {d[0]} - Valor: {d[1]}" for d in datos)
            label.config(text=texto)
        except:
            label.config(text="Error al calcular valor por categoría")

    def productosStockBajo(self, label):
        try:
            datos = self.producto.productosStockBajo()
            if len(datos) == 0:
                label.config(text="No hay productos con stock bajo")
            else:
                texto = "\n".join(f"ID: {fila[0]}, Nombre: {fila[1]}, Stock: {fila[3]}" for fila in datos)
                label.config(text=texto)
        except:
            label.config(text="Error al consultar stock bajo")

    # *********CLIENTES *********
    def clientes(self):
        ventana = Ventana.Toplevel()
        ventana.title("Módulo Clientes")
        ventana.geometry("750x650")
        ventana.configure(bg="#209dbc")  

        Ventana.Label(ventana, text="GESTIÓN DE CLIENTES", font=("Arial", 18, "bold"), bg="#209dbc", fg="white").pack(pady=10)

        Ventana.Label(ventana, text="Nombre:", bg="#209dbc", fg="white").pack()
        self.entryNombreC = Ventana.Entry(ventana, width=40)
        self.entryNombreC.pack()

        Ventana.Label(ventana, text="Apellido:", bg="#209dbc", fg="white").pack()
        self.entryApellidoC = Ventana.Entry(ventana, width=40)
        self.entryApellidoC.pack()

        Ventana.Label(ventana, text="Email:", bg="#209dbc", fg="white").pack()
        self.entryEmailC = Ventana.Entry(ventana, width=40)
        self.entryEmailC.pack()

        Ventana.Label(ventana, text="Historial de compras:", bg="#209dbc", fg="white").pack()
        self.entryHistorialC = Ventana.Entry(ventana, width=40)
        self.entryHistorialC.pack()

        Ventana.Label(ventana, text="ID:", bg="#209dbc", fg="white").pack()
        self.entryIdC = Ventana.Entry(ventana, width=20)
        self.entryIdC.pack()

        resultado = Ventana.Label(ventana, text="", bg="#209dbc", fg="black", font=("Arial", 11))
        resultado.pack(pady=10)
        
        Ventana.Button(ventana, text="Agregar", bg="blue", fg="white", width=15, command=lambda: self.agregarCliente(self.entryNombreC, self.entryApellidoC, self.entryEmailC, self.entryHistorialC, resultado)).pack(pady=3)
        Ventana.Button(ventana, text="Consultar", bg="purple", fg="white", width=15, command=lambda: self.consultarClientes(resultado)).pack(pady=3)
        Ventana.Button(ventana, text="Actualizar", bg="orange", fg="black", width=15, command=lambda: self.actualizarCliente(self.entryIdC, self.entryNombreC, self.entryApellidoC, self.entryEmailC, self.entryHistorialC, resultado)).pack(pady=3)
        Ventana.Button(ventana, text="Eliminar", bg="red", fg="white", width=15, command=lambda: self.eliminarCliente(self.entryIdC, resultado)).pack(pady=3)

        Ventana.Button(ventana, text="Valor total de compras", bg="brown", fg="white", width=25, command=lambda: self.totalCompras(resultado)).pack(pady=3)
        Ventana.Button(ventana, text="Total por cliente", bg="yellow", fg="black", width=25, command=lambda: self.totalPorCliente(resultado)).pack(pady=3)

    # ********* FUNCIONES CLIENTES *********
    def agregarCliente(self, nombre, apellido, email, historial, label):
        try:
            self.cliente.agregarCliente(nombre.get(), apellido.get(), email.get(), float(historial.get()))
            label.config(text="Cliente agregado correctamente")
        except:
            label.config(text="Error al agregar cliente")
        finally:
            self.setNombreC("")
            self.setApellidoC("")
            self.setEmailC("")
            self.setHistorialC("")

    def consultarClientes(self, label):
        try:
            datos = self.cliente.consultarClientes()
            texto = "\n".join(str(fila) for fila in datos)
            label.config(text=texto)
        except:
            label.config(text="Error al consultar los clientes")

    def actualizarCliente(self, idc, nombre, apellido, email, historial, label):
        try:
            self.cliente.actualizarCliente(int(idc.get()), nombre.get(), apellido.get(), email.get(), float(historial.get()))
            label.config(text=f"Cliente {idc.get()} actualizado")
        except:
            label.config(text="Error al actualizar al cliente")
        finally:
            self.setIdC("")
            self.setNombreC("")
            self.setApellidoC("")
            self.setEmailC("")
            self.setHistorialC("")

    def eliminarCliente(self, idc, label):
        try:
            self.cliente.eliminarCliente(int(idc.get()))
            label.config(text=f"Cliente {idc.get()} eliminado")
        except:
            label.config(text="Error al eliminar al cliente")
        finally:
            self.setIdC("")

    def totalCompras(self, label):
        try:
            total = self.cliente.valorTotalCompras()
            label.config(text=f"Valor total de compras: {total}")
        except:
            label.config(text="Error al calcular el total")

    def totalPorCliente(self, label):
        try:
            datos = self.cliente.totalComprasPorCliente()
            texto = "\n".join(f"{d[0]} → {d[1]}" for d in datos)
            label.config(text=texto)
        except:
            label.config(text="Error al calcular el total por cliente")


# ****** Main ********
obj = interfaz()
aux = obj.ventana()
aux.mainloop()