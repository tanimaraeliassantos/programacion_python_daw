from flask import Flask
from flask import jsonify, request
from datetime import datetime
from flask import render_template
from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.engine import URL

app = Flask(__name__)

DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="Tanimaraes201619",
    host="localhost",
    port=3307,
    database="tienda_virtual",
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)

metadata = MetaData()

productos_t = Table(
    "productos_producto",
    metadata,
    autoload_with=engine
)

categorias_t = Table(
    "productos_categoria",
    metadata,
    autoload_with=engine
)


@app.route("/")
def home():
    return "API Flask conectada a MySQL (Docker). Prueba /api/productos"


@app.route("/api/productos")
def listar_productos():
    stmt = select(
        productos_t.c.id,
        productos_t.c.nombre,
        productos_t.c.descripcion,
        productos_t.c.precio,
        productos_t.c.stock,
        productos_t.c.disponible,
        productos_t.c.fecha_creacion,
        productos_t.c.categoria_id,
    )

    with engine.connect() as conn:
        rows = conn.execute(stmt).mappings().all()

    return jsonify([dict(row) for row in rows])


@app.route("/api/categorias")
def listar_categorias():
    stmt = select(categorias_t)

    with engine.connect() as conn:
        rows = conn.execute(stmt).mappings().all()

    return jsonify([dict(row) for row in rows])


@app.route("/api/productos", methods=["POST"])
def crear_producto():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "No se ha enviado JSON"}), 400

    # Campos obligatorios según la tabla
    campos = ["nombre", "descripcion", "precio",
              "stock", "disponible", "categoria_id"]
    for campo in campos:
        if campo not in data:
            return jsonify({"error": f"Falta el campo {campo}"}), 400

    with engine.begin() as conn:
        result = conn.execute(
            productos_t.insert().values(
                nombre=data["nombre"],
                descripcion=data["descripcion"],
                precio=data["precio"],
                stock=data["stock"],
                disponible=1 if data["disponible"] else 0,
                fecha_creacion=datetime.now(),
                categoria_id=data["categoria_id"]
            )
        )

        nuevo_id = result.lastrowid

        producto = conn.execute(
            select(productos_t).where(productos_t.c.id == nuevo_id)
        ).mappings().first()

    return jsonify(dict(producto)), 201


@app.route("/api/productos/<int:pid>", methods=["PUT"])
def actualizar_producto(pid):
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "No se ha enviado JSON"}), 400

    # Campos permitidos (no tocamos id ni fecha_creacion)
    permitidos = ["nombre", "descripcion", "precio",
                  "stock", "disponible", "categoria_id"]
    cambios = {k: data[k] for k in permitidos if k in data}

    if "disponible" in cambios:
        cambios["disponible"] = 1 if cambios["disponible"] else 0

    if not cambios:
        return jsonify({"error": "No hay campos válidos para actualizar"}), 400

    with engine.begin() as conn:
        existe = conn.execute(
            select(productos_t.c.id).where(productos_t.c.id == pid)
        ).first()

        if not existe:
            return jsonify({"error": "Producto no encontrado"}), 404

        conn.execute(
            productos_t.update()
            .where(productos_t.c.id == pid)
            .values(**cambios)
        )

        producto = conn.execute(
            select(productos_t).where(productos_t.c.id == pid)
        ).mappings().first()

    return jsonify(dict(producto))


@app.route("/api/productos/<int:pid>", methods=["DELETE"])
def borrar_producto(pid):
    with engine.begin() as conn:
        existe = conn.execute(
            select(productos_t.c.id).where(productos_t.c.id == pid)
        ).first()

        if not existe:
            return jsonify({"error": "Producto no encontrado"}), 404

        conn.execute(productos_t.delete().where(productos_t.c.id == pid))

    return jsonify({"mensaje": "Producto eliminado"})


if __name__ == "__main__":
    app.run(debug=True)
