class Producto:
    id = 1

    def __init__(self, nombre, precio, cantidad):
        #Atributos de instancia
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

        #Autoincremento
        self.id = Producto.id
        Producto.id = Producto.id + 1
    
    
    

