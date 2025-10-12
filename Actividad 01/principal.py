from ejemplo import Persona

if __name__ == "__main__":
    print("Hola!")
    nombre = input("Nombre: ")
    edad = input("Edad: ")

    nueva = Persona(nombre, edad)
    print(Persona.id)
    nueva2 = Persona(nombre, edad)
    print(nueva2.nombre)

    """
    Para 
    comentarios
    en
    bloque
    
    """
    nombres = ["Ana", "Maria", "Paula"]
    for nombre in nombres:
        print("Hola", nombre)

    p1 = Persona("Ana", 25)
    p2 = Persona("Luis", 30)
    p3 = Persona("Marta", 45)

    personas = []
    personas.append(p1)
    personas.append(p2)
    personas.append(p3)
    