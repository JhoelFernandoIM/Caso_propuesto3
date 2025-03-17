# modelo.py (Definir funciones CRUD con Supabase)
# -----------------------------------------------
from supabase import create_client, Client

SUPABASE_URL = "https://bmfyqluttbhuiookplic.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJtZnlxbHV0dGJodWlvb2twbGljIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE3NDU2MTYsImV4cCI6MjA1NzMyMTYxNn0.QH-LObkiMjRWYSaf7uZOyk__mPoWr0ipWWNL2xobzSY"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def obtener_productos():
    response = supabase.table("productos").select("*").execute()
    return response.data if response.data else []

def agregar_producto(nombre, categoria, precio, stock):
    if not nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")
    
    try:
        precio = float(precio)
        stock = int(stock)
        
        response = supabase.table("productos").insert({
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "stock": stock
        }).execute()
        
        return "Producto agregado correctamente."

    except ValueError:
        raise ValueError("El precio debe ser un número decimal y el stock un número entero.")
    
    except Exception as e:
        if "duplicate key value" in str(e) or "unique constraint" in str(e).lower():
            raise ValueError("Error: Ya existe un producto con este nombre.")
        else:
            raise Exception(f"Error al agregar producto: {e}")

def actualizar_producto(id, nombre, categoria, precio, stock):
    if not nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")
    try:
        precio = float(precio)
        stock = int(stock)
        supabase.table("productos").update({"nombre": nombre, "categoria": categoria, "precio": precio, "stock": stock}).eq("id", id).execute()
    except ValueError:
        raise ValueError("El precio debe ser un número decimal y el stock un número entero.")
    except Exception as e:
        raise Exception(f"Error al actualizar producto: {e}")

def eliminar_producto(id):
    try:
        supabase.table("productos").delete().eq("id", id).execute()
    except Exception as e:
        raise Exception(f"Error al eliminar producto: {e}")