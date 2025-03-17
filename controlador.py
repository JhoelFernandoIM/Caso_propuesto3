# controlador.py (Manejar la lógica de la aplicación)
# ----------------------------------------------------
import modelo

def obtener_productos_controlador():
    return modelo.obtener_productos()

def agregar_producto_controlador(nombre, categoria, precio, stock):
    modelo.agregar_producto(nombre, categoria, precio, stock)

def actualizar_producto_controlador(id, nombre, categoria, precio, stock):
    modelo.actualizar_producto(id, nombre, categoria, precio, stock)

def eliminar_producto_controlador(id):
    modelo.eliminar_producto(id)
