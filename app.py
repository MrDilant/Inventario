# app.py
from servicios import *
from archivos import guardar_csv, cargar_csv

def validar_numero(mensaje, tipo=float):
    """Valida que la entrada sea numérica y no negativa."""
    while True:
        try:
            valor = tipo(input(mensaje))
            if valor < 0:
                print("[!] El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("[!] Entrada inválida. Ingrese un número.")

def menu_principal():
    inventario = []
    
    while True:
        print("\n=== SISTEMA DE GESTIÓN DE INVENTARIO ===")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Calcular estadísticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")
        
        opcion = input("\nSeleccione una opción (1-9): ")

        if opcion == "1":
            nom = input("Nombre: ")
            pre = validar_numero("Precio: ", float)
            can = validar_numero("Cantidad: ", int)
            agregar_producto(inventario, nom, pre, can)
            print("[OK] Producto agregado.")

        elif opcion == "2":
            mostrar_inventario(inventario)

        elif opcion == "3":
            nom = input("Nombre a buscar: ")
            p = buscar_producto(inventario, nom)
            if p: print(f"Encontrado: {p}")
            else: print("[!] Producto no hallado.")

        elif opcion == "4":
            nom = input("Nombre del producto a editar: ")
            pre = validar_numero("Nuevo precio (0 para omitir): ")
            can = validar_numero("Nueva cantidad (0 para omitir): ", int)
            if actualizar_producto(inventario, nom, pre or None, can or None):
                print("[OK] Producto actualizado.")
            else: print("[!] No se encontró el producto.")

        elif opcion == "5":
            nom = input("Nombre a eliminar: ")
            if eliminar_producto(inventario, nom):
                print("[OK] Producto eliminado.")
            else: print("[!] No se encontró.")

        elif opcion == "6":
            stats = calcular_estadisticas(inventario)
            if stats:
                print(f"\n--- ESTADÍSTICAS ---")
                print(f"Unidades Totales: {stats['unidades']}")
                print(f"Valor Total: ${stats['valor']:.2f}")
                print(f"Más caro: {stats['caro']['nombre']} (${stats['caro']['precio']})")
                print(f"Mayor stock: {stats['stock']['nombre']} ({stats['stock']['cantidad']} und)")
            else: print("[!] Sin datos.")

        elif opcion == "7":
            guardar_csv(inventario)

        elif opcion == "8":
            datos, err = cargar_csv()
            if datos is not None:
                print(f"Se encontraron {len(datos)} productos y {err} errores.")
                res = input("¿Sobrescribir inventario actual? (S/N): ").upper()
                if res == "S":
                    inventario = datos
                else:
                    # Fusión: Actualizar si existe, si no, agregar
                    for p_nuevo in datos:
                        p_viejo = buscar_producto(inventario, p_nuevo['nombre'])
                        if p_viejo:
                            p_viejo['cantidad'] += p_nuevo['cantidad']
                            p_viejo['precio'] = p_nuevo['precio']
                        else:
                            inventario.append(p_nuevo)
                print("[OK] Carga finalizada.")

        elif opcion == "9":
            print("Saliendo del sistema...")
            # Resumen final (Objetivo de la semana)
            # Este programa permite gestionar un inventario completo con persistencia en archivos,
            # aplicando validaciones, modularización y lógica de colecciones en Python.
            break
        else:
            print("[!] Opción no válida.")

if __name__ == "__main__":
    menu_principal()