class Persona:
    id = 1

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.id = Persona.id
        Persona.id = Persona.id + 1

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"
