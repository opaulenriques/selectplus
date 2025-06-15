from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Vaga(Base):
    __tablename__ = "vagas"

    id = Column(Integer, primary_key=True, index=True)
    data_abertura = Column(Date)
    sla = Column(Integer)
    marca = Column(String)
    departamento = Column(String)
    solicitante = Column(String)
    cargo = Column(String)
    sigilosa = Column(Boolean)
    tipo_vaga = Column(String)
    recrutador = Column(String)
    status = Column(String)
    etapa = Column(String)
    fonte = Column(String)
    observacoes = Column(String)
