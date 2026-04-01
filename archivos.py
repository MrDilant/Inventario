# archivos.py
import csv

def guardar_csv(inventario, ruta="inventario.csv"):
    """Guarda la lista de diccionarios en un archivo CSV."""
    if not inventario:
        print("[!] No hay datos para guardar.")
        return False
    
    try:
        with open(ruta, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["nombre", "precio", "cantidad"])
            writer.writeheader()
            writer.writerows(inventario)
        print(f"[OK] Inventario guardado en: {ruta}")
    except Exception as e:
        print(f"[Error] No se pudo guardar: {e}")


def cargar_csv(ruta="inventario.csv"):
    """Carga datos validando tipos y estructura."""
    productos_cargados = []
    errores = 0
    try:
        with open(ruta, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            # Validar encabezados
            if not all(col in reader.fieldnames for col in ["nombre", "precio", "cantidad"]):
                raise ValueError("Encabezados CSV inválidos.")

            for fila in reader:
                try:
                    nombre = fila['nombre']
                    precio = float(fila['precio'])
                    cantidad = int(fila['cantidad'])
                    
                    if precio < 0 or cantidad < 0: raise ValueError
                    
                    productos_cargados.append({
                        "nombre": nombre, "precio": precio, "cantidad": cantidad
                    })
                except:
                    errores += 1
        return productos_cargados, errores
    except FileNotFoundError:
        print("[!] El archivo no existe.")
        return None, 0
    except Exception as e:
        print(f"[Error] Error al cargar: {e}")
        return None, 0