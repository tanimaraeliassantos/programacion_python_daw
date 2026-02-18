from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from db import get_db
from models import Incidencia
from auth import router as auth_router
from deps import get_current_user

app = FastAPI(
    title="API de Incidencias",
    description="Login token endpoint protegido",
    version="3.0.0"
)


class IncidenciaBase(BaseModel):
    titulo: str = Field(min_length=1, max_length=150)
    descripcion: str
    prioridad: str
    estado: str


class IncidenciaResponse(IncidenciaBase):
    id: int

    class Config:
        from_attributes = True


app.include_router(auth_router)


@app.get("/")
def root():
    return {"ok": True, "mensaje": "API conectada a MySQL. Ve a /docs"}


@app.get("/privado")
def privado(usuario: str = Depends(get_current_user)):
    return {"mensaje": f"Hola {usuario}, estás autenticado"}


@app.get("/incidencias", response_model=list[IncidenciaResponse])
def listar_incidencias(db: Session = Depends(get_db)):
    return db.query(Incidencia).all()


@app.get("/incidencias/{incidencia_id}", response_model=IncidenciaResponse)
def obtener_incidencia(incidencia_id: int, db: Session = Depends(get_db)):
    incidencia = db.query(Incidencia).filter(
        Incidencia.id == incidencia_id).first()

    if not incidencia:
        raise HTTPException(status_code=404, detail="Incidencia no encontrada")

    return incidencia


@app.post("/incidencias", response_model=IncidenciaResponse, status_code=201)
def crear_incidencia(incidencia: IncidenciaBase, db: Session = Depends(get_db)):
    nueva = Incidencia(
        titulo=incidencia.titulo,
        descripcion=incidencia.descripcion,
        prioridad=incidencia.prioridad,
        estado=incidencia.estado
    )

    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return nueva


@app.get("/nombre")
def nombre(usuario: str = Depends(get_current_user)):
    return {"usuario": usuario}
