# tabela do banco (SQLModel)

from typing import Optional
from sqlmodel import SQLModel, Field

class ProfissionalSaude(SQLModel, table=True):
    id_profissional: int = Field(primary_key=True, foreign_key="pessoa.id_pessoa")
    especialidade: str
    crm: str
    disponibilidade: bool  # True = disponível, False = indisponível
    unidade_saude: str 