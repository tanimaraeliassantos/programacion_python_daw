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

# -------------------------------------------------------
# Función para crear producto con input del usuario
# -------------------------------------------------------


def crear_producto(productos):
    # Solicita el nombre del producto
    nombre = input("Introduce nombre del producto: ")
    # Validación para nombre
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    try:
        # Solicita y valida el precio como float
        precio = float(
            input("Introduce precio del producto:(ejemplo 199.99) "))
        if precio <= 0:
            print("El precio debe ser un número positivo")
            return
    except ValueError:
        # Captura error si el formato del precio es incorrecto
        print("Formato de precio inválido.")
        return

    try:
        # Solicita y valida la cantidad como int
        cantidad = int(input("Introduce la cantidad de productos en stock: "))
        if cantidad < 0:
            print("La cantidad debe ser un número positivo")
            return
    except ValueError:
        # Captura error si el formato de la cantidad es incorrecto
        print("Formato de cantidad en inventario inválido.")
        return

    # Crea el nuevo objeto Producto
    nuevo_producto = Producto(nombre, precio, cantidad)
    # Agrega el nuevo producto a la lista
    productos.append(nuevo_producto)

    print(f"Producto nuevo añadido al inventario.")
    print(nuevo_producto)


def listar_productos(productos):
    print("Sigue el listado de los productos de la tienda: ")

    for producto in productos:
        # Imprime cada producto
        print(producto)

# -------------------------------------------------------
# Función para actualizar producto con input del usuario
# -------------------------------------------------------


def actualizar_productos(productos):
    try:
        # Solicita el ID a actualizar y valida la entrada
        id_actualizar = int(input("Introduce el ID a actualizar: "))
    except ValueError:
        print("ID inválido.")
        return

    producto_encontrado_actualizado = False

    for producto in productos:
        if producto.id == id_actualizar and not producto_encontrado_actualizado:

            # Cambiar nombre del producto
            nuevo_nombre = input(
                f"Nuevo nombre: (dejalo en blanco para no cambiar nada)")
            if nuevo_nombre:
                producto.nombre = nuevo_nombre

            # Cambiar cantidad en inventario
            nueva_cantidad = input(
                f"Nueva cantidad: (dejalo en blanco para no cambiar nada)")
            if nueva_cantidad:
                try:
                    nueva_cantidad = int(nueva_cantidad)

                    if nueva_cantidad >= 0:
                        producto.cantidad = nueva_cantidad
                        producto_encontrado_actualizado = True
                    else:
                        print("La cantidad deve ser un número positivo o cero.")
                except ValueError:
                    print("La cantidad debe ser un número.")

            # Cambiar precio del producto
            nuevo_precio = input(
                f"Nuevo precio: (dejalo en blanco para no cambiar nada)")
            if nuevo_precio:
                try:
                    nuevo_precio = float(nuevo_precio)

                    if nuevo_precio >= 0:
                        producto.precio = nuevo_precio
                        producto_encontrado_actualizado = True
                    else:
                        print("El precio debe ser un número positivo o cero.")
                except ValueError:
                    print("El precio debe ser un número.")

    if not producto_encontrado_actualizado:
        print("Producto no encontrado o no actualizado.")

# -------------------------------------------------------
# Función para eliminar producto con input del usuario
# -------------------------------------------------------


def eliminar_producto(productos):
    try:
        # Solicita el ID a eliminar y valida la entrada
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
