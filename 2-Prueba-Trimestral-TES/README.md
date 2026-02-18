# API de Gestión de Incidencias - FastAPI & MySQL

Este proyecto es una API REST profesional desarrollada con **FastAPI** para la gestión de incidencias técnicas. Incluye persistencia de datos en una base de datos **MySQL** (mediante Docker) y seguridad basada en tokens **JWT (JSON Web Tokens)**.

---

## Características

- **CRUD de Incidencias**: Listado, consulta por ID y creación.
- **Base de Datos Relacional**: Integración con MySQL mediante el ORM SQLAlchemy.
- **Seguridad JWT**: Protección de endpoints sensibles (POST) mediante autenticación de usuario.
- **Contenedores**: Configurado para funcionar con entornos Docker.
- **Documentación Interactiva**: Autogenerada por FastAPI (Swagger UI).

---

## Tecnologías Utilizadas

- **Backend**: Python 3.10+ & FastAPI.
- **Base de Datos**: MySQL 8.0 (Docker).
- **ORM**: SQLAlchemy & PyMySQL.
- **Seguridad**: Passlib (Bcrypt) & Python-Jose (JWT).

---

## Requisitos Previos

1.  Tener instalado **Python**.
2.  Tener **Docker Desktop** funcionando.
3.  Servidor MySQL activo en el puerto `3306` (o el configurado en `db.py`).

---

## Instalación y Configuración

1. **Clonar el repositorio y entrar en la carpeta:**
   ```bash
   cd fastapi-incidencias
   ```
2. **Crear y activar el entorno virtual:**

```bash
python -m venv venv
# En Windows:
.\venv\Scripts\activate
```

3. **Instalar dependencias:**

```bash
pip install fastapi uvicorn sqlalchemy pymysql "python-jose[cryptography]" "passlib[bcrypt]" python-multipart
```

4. **Configurar la Base de Datos:**
   Ejecutar el siguiente script SQL en tu gestor de MySQL:

```SQL
CREATE DATABASE IF NOT EXISTS fastapi_incidentes;
USE fastapi_incidentes;
CREATE TABLE incidencias (
id INT AUTO_INCREMENT PRIMARY KEY,
titulo VARCHAR(150) NOT NULL,
descripcion TEXT NOT NULL,
prioridad VARCHAR(20) NOT NULL,
estado VARCHAR(20) NOT NULL
);
```

Ejecución
Para arrancar el servidor de desarrollo:

```bash
uvicorn main:app --reload
```

La API estará disponible en: http://localhost:8000
La documentación Swagger en: http://localhost:8000/docs

Credenciales de Prueba (JWT)
Para probar los endpoints protegidos (POST), utiliza las siguientes credenciales en el endpoint /login:

- Usuario: admin
- Password: Tanimaraes201619

**Estructura del Proyecto**
**main.py:** Punto de entrada y definición de rutas.
**db.py:** Configuración de la conexión a MySQL.
**models.py:** Definición de las tablas (SQLAlchemy).
**auth.py:** Rutas de autenticación y login.
**security.py:** Lógica de encriptado y generación de tokens.
**deps.py:** Dependencias de seguridad para proteger rutas.
