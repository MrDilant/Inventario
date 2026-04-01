# servicios.py

def agregar_producto(inventario, nombre, precio, cantidad):
    """Agrega un nuevo producto al inventario."""
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)

    
def mostrar_inventario(inventario):
    """Recorre y muestra los productos."""
    if not inventario:
        print("\n[!] El inventario está vacío.")
        return
    print("\n--- INVENTARIO ACTUAL ---")
    for p in inventario:
        print(f"Producto: {p['nombre']:15} | Precio: ${p['precio']:8.2f} | Cantidad: {p['cantidad']:5}")


def buscar_producto(inventario, nombre):
    """Busca un producto por nombre (ignora mayúsculas/minúsculas)."""
    for p in inventario:
        if p['nombre'].lower() == nombre.lower():
            return p
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """Actualiza precio o cantidad de un producto existente."""
    p = buscar_producto(inventario, nombre)
    if p:
        if nuevo_precio is not None: p['precio'] = nuevo_precio
        if nueva_cantidad is not None: p['cantidad'] = nueva_cantidad
        return True
    return False


def eliminar_producto(inventario, nombre):
    """Elimina un producto de la lista."""
    p = buscar_producto(inventario, nombre)
    if p:
        inventario.remove(p)
        return True
    return False


def calcular_estadisticas(inventario):
    """Calcula métricas usando lambdas y funciones integradas."""
    if not inventario:
        return None

    # Uso de lambda para subtotal como pide el ejercicio
    subtotal_fn = lambda p: p["precio"] * p["cantidad"]
    
    unidades_totales = sum(p['cantidad'] for p in inventario)
    valor_total = sum(subtotal_fn(p) for p in inventario)
    
    producto_mas_caro = max(inventario, key=lambda x: x['precio'])
    producto_mayor_stock = max(inventario, key=lambda x: x['cantidad'])

    return {
        "unidades": unidades_totales,
        "valor": valor_total,
        "caro": producto_mas_caro,
        "stock": producto_mayor_stock
    }