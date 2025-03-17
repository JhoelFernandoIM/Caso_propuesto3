# main.py (Punto de entrada principal)
# ------------------------------------
import streamlit as st
import vista

st.sidebar.title("Menú")
opcion = st.sidebar.radio("Seleccione una opción", ["Ver Productos", "Agregar Producto"])

if opcion == "Ver Productos":
    vista.mostrar_productos()
elif opcion == "Agregar Producto":
    vista.agregar_producto()
