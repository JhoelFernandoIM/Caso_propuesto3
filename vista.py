# vista.py (Interfaz con Streamlit)
# ---------------------------------
import streamlit as st
import pandas as pd
import controlador

st.title("Gestión de Productos")

# Mostrar productos
datos = controlador.obtener_productos_controlador()
df = pd.DataFrame(datos)

st.subheader("Lista de Productos")
for _, row in df.iterrows():
    with st.container():
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        col1.write(row["id"])
        col2.write(row["nombre"])
        col3.write(row["categoria"])
        col4.write(row["precio"])
        col5.write(row["stock"])
        if col6.button("Eliminar", key=f"del_{row['id']}"):
            controlador.eliminar_producto_controlador(row["id"])
            st.success("Producto eliminado correctamente.")
            st.rerun()

# Formulario para agregar productos
st.subheader("Agregar Nuevo Producto")
nombre = st.text_input("Nombre del Producto")
categoria = st.text_input("Categoría")
precio = st.number_input("Precio", min_value=0.0, step=0.01)
stock = st.number_input("Stock", min_value=0, step=1)
if st.button("Agregar Producto"):
    try:
        controlador.agregar_producto_controlador(nombre, categoria, precio, stock)
        st.success("Producto agregado correctamente.")
        st.rerun()
    except Exception as e:
        st.error(f"Error: {e}")

# Formulario para editar productos
st.subheader("Actualizar Producto")
id_editar = st.number_input("ID del Producto a editar", min_value=1, step=1)
nuevo_nombre = st.text_input("Nuevo Nombre")
nueva_categoria = st.text_input("Nueva Categoría")
nuevo_precio = st.number_input("Nuevo Precio", min_value=0.0, step=0.01)
nuevo_stock = st.number_input("Nuevo Stock", min_value=0, step=1)
if st.button("Actualizar Producto"):
    try:
        controlador.actualizar_producto_controlador(id_editar, nuevo_nombre, nueva_categoria, nuevo_precio, nuevo_stock)
        st.success("Producto actualizado correctamente.")
        st.rerun()
    except Exception as e:
        st.error(f"Error: {e}")