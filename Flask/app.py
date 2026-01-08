from flask import Flask
from flask import jsonify
from flask import render_template

app = Flask(__name__)

productos = [
    {"id": 1, "nombre": "Monitor", "precio": 198.99}, {
        "id": 2, "nombre": "Teclado", "precio": 34.99}
]


@app.route("/web")
def web():
    return render_template("inicio.html")


@app.route("/api/productos")
def obtener_productos():
    return jsonify({"productos": productos})


@app.route("/api/productos/<int:id>")
def obtener_producto(id):
    producto = next((p for p in productos if p["id"] == id), None)
    if producto:
        return jsonify(producto)
    return jsonify({"error": "Producto no encontrado"}), 404


@app.route("/")
def inicio():
    return "Hola, esta es mi primera app Flask"


@app.route("/saludo")
def saludo():
    return "Hola a todos desde Flask!"


@app.route("/usuario/<nombre>")
def usuario(nombre):
    return f"Bienvenida, {nombre}"


@app.route("/suma/<int:a>/<int:b>")
def suma(a, b):
    return f"La suma es {a + b}"


if __name__ == "__main__":
    app.run(debug=True)
