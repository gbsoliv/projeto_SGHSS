# tabela do banco (SQLModel)

from typing import Optional
from datetime import date
from sqlmodel import SQLModel, Field


class Paciente(SQLModel, table=True):
    
    # PK e também FK para pessoa.id_pessoa
    id_paciente: int = Field(primary_key=True, foreign_key="pessoa.id_pessoa")

    data_nascimento: date
    convenio: bool