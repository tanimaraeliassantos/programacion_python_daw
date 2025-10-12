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
