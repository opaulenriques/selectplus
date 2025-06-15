from database import SessionLocal
from vaga_model import Vaga
from datetime import date

def criar_vaga(dados):
    db = SessionLocal()
    vaga = Vaga(**dados)
    db.add(vaga)
    db.commit()
    db.refresh(vaga)
    db.close()
    return vaga

def listar_vagas():
    db = SessionLocal()
    vagas = db.query(Vaga).all()
    db.close()
    return vagas
