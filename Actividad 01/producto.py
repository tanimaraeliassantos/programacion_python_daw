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
