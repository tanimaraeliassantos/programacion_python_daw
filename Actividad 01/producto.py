class Producto:
    id = 1

    def __init__(self, nombre, precio, cantidad):
        # Atributos de instancia
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

        # Autoincremento
        self.id = Producto.id
        Producto.id = Producto.id + 1

    # Información producto en String
    def __str__(self):
        return f"ID:{self.id}, Nombre: {self.nombre}, Precio: {self.precio:.2f}, Stock: {self.cantidad}"

# Función para crear producto con input del usuario


def crear_producto(productos):
    nombre = input("Introduce nombre del producto: ")
    precio = float(
        input("Introduce precio del producto:(ejemplo 199.99) "))
    cantidad = int(input("Introduce la cantidad de productos en stock: "))

    # Crear producto y añadir a la lista
    nuevo_producto = Producto(nombre, precio, cantidad)
    productos.append(nuevo_producto)

    # Confirmar inclusión en la lista e imprimir producto nuevo
    print(f"Producto nuevo añadido al inventario.")
    print(nuevo_producto)


def listar_productos(productos):
    print("Sigue el listado de los productos de la tienda: ")

    for producto in productos:
        print(producto)


def actualizar_productos(productos):
    id_actualizar = int(input("Introduce el ID a actualizar: "))

    producto_encontrado_actualizado = False

    for producto in productos:
        if producto.id == id_actualizar and not producto_encontrado_actualizado:

            # Cambiar nombre del producto
            nuevo_nombre = input(
                f"Nuevo nombre: (dejalo en blanco para no cambiar nada)")
            if nuevo_nombre:
                producto.nombre = nuevo_nombre

            # Cambiar cantidad en inventario
            nueva_cantidad = int(
                input(f"Nueva cantidad: (dejalo en blanco para no cambiar nada)"))
            if nueva_cantidad:
                producto.cantidad = nueva_cantidad
                producto_encontrado_actualizado = True

            # Cambiar precio del producto
            nuevo_precio = float(
                input(f"Nuevo precio: (dejalo en blanco para no cambiar nada)"))
            if nuevo_precio:
                producto.precio = nuevo_precio
                producto_encontrado_actualizado = True

    if not producto_encontrado_actualizado:
        print("Producto no encontrado")


def eliminar_producto(productos):
    try:
        id_eliminar = int(input("Introduce el ID del producto a eliminar: "))
    except ValueError:
        print("ID inválido.")
        return

    producto_eliminado = False

    for producto in productos:
        if producto.id == id_eliminar and not producto_eliminado:
            productos.remove(producto)
            print(f"Producto con ID {id_eliminar} eliminado.")
            producto_eliminado = True

    if not producto_eliminado:
        print(f"Producto con ID {id_eliminar} no eliminado.")
