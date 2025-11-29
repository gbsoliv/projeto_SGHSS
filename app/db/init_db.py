
from sqlmodel import SQLModel
from .session import engine

# IMPORTANDO OS MODELS PARA REGISTRAR AS TABELAS
from app.models.pessoa import Pessoa  
from app.models.paciente import Paciente 
from app.models.profissional_saude import ProfissionalSaude
from app.models.administrador import Administrador
from app.models.consulta import Consulta


#CRIANDO AS TABELAS
def init_db() -> None:
    SQLModel.metadata.create_all(bind=engine)
