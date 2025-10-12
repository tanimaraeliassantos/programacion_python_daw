from producto import Producto, crear_producto, listar_productos, actualizar_productos, eliminar_producto
# List vacía para almacenar productos
productos = []

# Productos para iniciar lista
p1 = Producto("Portatil Acer Gaming Nitro V 15\"", 649.00, 8)
p2 = Producto("Portatil Acer Aspire Go 15 AG15", 479.00, 10)
p3 = Producto("Portatil Lenovo IdeaPad Slim 3", 349.00, 20)

productos.append(p1)
productos.append(p2)
productos.append(p3)

# Inicializar función para disponer de menu principal


def menu_principal(productos):
    ejecutando = True

    while ejecutando:
        print("*** Menu de gestión de productos *** ")
        print("1. Crear nuevo producto")
        print("2. Listar todos los productos")
        print("3. Actualizar datos producto")
        print("4. Eliminar producto")

        opcion = input("Elige que deseas hacer: (1-5)")

        if opcion == "1":
            crear_producto(productos)

        elif opcion == "2":
            listar_productos(productos)

        elif opcion == "3":
            actualizar_productos(productos)

        elif opcion == "4":
            eliminar_producto(productos)

        elif opcion == "5":
            print("Gestor de productos finalizado.")
            ejecutando = False
        else:
            print("Opcion no válida, inténtalo de nuevo.")


if __name__ == "__main__":
    menu_principal(productos)
