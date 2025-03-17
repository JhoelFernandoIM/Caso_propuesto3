# vista.py (Interfaz con Streamlit)
# ---------------------------------
import streamlit as st
import controlador

def mostrar_productos():
    st.title("Gestión de Productos")
    productos = controlador.obtener_productos_controlador()
    
    for i, producto in enumerate(productos, start=1):
        with st.expander(f"{i}. {producto['nombre']}"):
            st.write(f"**ID:** {i}")
            nombre = st.text_input("Nombre", producto["nombre"], key=f"nombre_{i}")
            categoria = st.text_input("Categoría", producto["categoria"], key=f"categoria_{i}")
            precio = st.number_input("Precio", value=producto["precio"], key=f"precio_{i}")
            stock = st.number_input("Stock", value=producto["stock"], step=1, key=f"stock_{i}")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Actualizar", key=f"actualizar_{i}"):
                    controlador.actualizar_producto_controlador(producto["id"], nombre, categoria, precio, stock)
                    st.success("Producto actualizado correctamente.")
                    st.rerun()
            with col2:
                if st.button("Eliminar", key=f"eliminar_{i}"):
                    controlador.eliminar_producto_controlador(producto["id"])
                    st.warning("Producto eliminado.")
                    st.rerun()

def agregar_producto():
    st.subheader("Agregar Nuevo Producto")
    nombre = st.text_input("Nombre")
    categoria = st.text_input("Categoría")
    precio = st.number_input("Precio", min_value=0.0, format="%.2f")
    stock = st.number_input("Stock", min_value=0, step=1)
    if st.button("Agregar Producto"):
        try:
            controlador.agregar_producto_controlador(nombre, categoria, precio, stock)
            st.success("Producto agregado correctamente.")
            st.rerun()
        except ValueError as ve:
            st.error(ve)
        except Exception as e:
            st.error(e)