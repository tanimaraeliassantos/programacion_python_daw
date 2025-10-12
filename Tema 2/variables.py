# Variables correctas
nombre = "Ana"
edad = 25
altura = 1.75
es_estudiante = True

# Variables incorrectas
# 1variable = 5
# mi-variable = 7
# class="Python"

print(nombre)
print(edad)
print(altura)
es_estudiante = True

# Asignación múltiple
x, y, z = 10, "Hola", True
print(x)
print(y)
print(z)

# Aritméticos
a, b = 10, 3
print(a + b)   # 13  (suma)
print(a - b)   # 7   (resta)
print(a * b)   # 30  (multiplicación)
print(a / b)   # 3.33 (división)
print(a // b)  # 3   (división entera)
print(a % b)   # 1   (módulo)
print(a ** b)  # 1000 (potencia)

# Comparación
a, b = 10, 5

print(a == b)   # False (igualdad)
print(a != b)   # True  (diferente)
print(a > b)    # True
print(a <= b)   # False

# Lógicos
x, y = True, False

print(x and y)  # False (ambos deben ser True)
print(x or y)   # True  (al menos uno True)
print(not x)

x //= 2     # división entera → 6
x **= 3     # potencia → 8

saludo = "Hola" + " " + "Python"
# Subcadena (slicing)
sub = saludo[0:4]                  # "Hola"
# Acceso por índice
letra = saludo[0]                  # "H"

texto = "hola soy adicta al pan"
print(texto.upper())    # " PYTHON ES GENIAL "
print(texto.lower())    # " python es genial "
print(texto.strip(4))    # "Python es genial"

# match-case (Python 3.10+)
estado = "error"

match estado:
    case "ok":
        print("Todo funciona correctamente")
    case "error":
        print("Se ha producido un error")
    case "pendiente":
        print("Operación en proceso")
    case _:
        print("Estado desconocido")

# NUNCA!!!!
while True:
    respuesta = input("¿Continuar? (s/n): ")
    if respuesta.lower() == "n":
        break

punto = (0, 5)

match punto:
    case (0, y):
        print(f"Eje Y en {y}")  # Eje Y en 5
