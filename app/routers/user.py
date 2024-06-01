from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"],
)

# Recuperar Usuario pelo ID
@router.get("/{usuario_id}", response_model=schemas.UsuarioOut)
def read_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario not found")
    return db_usuario

# Recuperar todos os Usuarios
@router.get("/", response_model=list[schemas.UsuarioOut])
def read_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(models.Usuario).all()
    return usuarios