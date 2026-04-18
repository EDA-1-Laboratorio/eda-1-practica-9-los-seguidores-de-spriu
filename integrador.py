def agregar_producto(inventario):
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    # Crear el diccionario del producto y agregarlo a la lista
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    print("¡Producto agregado con éxito!")

def mostrar_inventario(inventario):
    if not inventario:
        print("Inventario vacío.")
        return
    print(f"{'Nombre':<20} {'Precio':>10} {'Cantidad':>10}")
    print("-" * 42)
    # Recorrer el inventario e imprimir cada producto
    for p in inventario:
        print(f"{p['nombre']:<20} ${p['precio']:>9.2f} {p['cantidad']:>10}")

def buscar_producto(inventario, nombre):
    # Buscar y retornar el producto cuyo nombre coincida (ignorando mayúsculas/minúsculas)
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None

def actualizar_cantidad(inventario):
    nombre = input("Nombre del producto: ")
    producto = buscar_producto(inventario, nombre)
    if producto:
        nueva_cantidad = int(input("Nueva cantidad: "))
        # Actualizar la cantidad del producto
        producto["cantidad"] = nueva_cantidad
        print("¡Cantidad actualizada con éxito!")
    else:
        print("Producto no encontrado.")

def eliminar_producto(inventario):
    nombre = input("Nombre del producto a eliminar: ")
    # Buscar el producto y eliminarlo de la lista
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        print("¡Producto eliminado con éxito!")
    else:
        print("Producto no encontrado.")

def resumen(inventario):
    if not inventario:
        print("Inventario vacío.")
        return
    
    # Calcular e imprimir métricas
    total_distintos = len(inventario)
    
    # Sumamos el valor total multiplicando precio * cantidad de cada producto
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)
    
    # Encontramos el más caro y el más barato usando la función max() y min()
    mas_caro = max(inventario, key=lambda x: x["precio"])
    mas_barato = min(inventario, key=lambda x: x["precio"])
    
    print("\n--- RESUMEN DEL INVENTARIO ---")
    print(f"Total de productos distintos: {total_distintos}")
    print(f"Valor total del inventario: ${valor_total:.2f}")
    print(f"Producto más caro: {mas_caro['nombre']} (${mas_caro['precio']:.2f})")
    print(f"Producto más barato: {mas_barato['nombre']} (${mas_barato['precio']:.2f})")
    print("------------------------------")

def menu():
    inventario = []
    while True:
        print("\n=== GESTOR DE INVENTARIO ===")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Actualizar cantidad")
        print("5. Eliminar producto")
        print("6. Resumen")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            mostrar_inventario(inventario)
        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            producto = buscar_producto(inventario, nombre)
            if producto:
                # Formateamos un poco la salida para que se vea mejor que un simple diccionario
                print(f"Encontrado - Nombre: {producto['nombre']}, Precio: ${producto['precio']}, Cantidad: {producto['cantidad']}")
            else:
                print("No encontrado.")
        elif opcion == "4":
            actualizar_cantidad(inventario)
        elif opcion == "5":
            eliminar_producto(inventario)
        elif opcion == "6":
            resumen(inventario)
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()
