# tabela do banco (SQLModel)

from typing import Optional
from sqlmodel import SQLModel, Field

class ProfissionalSaude(SQLModel, table=True):
    id_profissional: Optional[int] = Field(default=None, primary_key=True)
    especialidade: str
    crm: str
    disponibilidade: bool  # True = disponível, False = indisponível
    unidade_saude: str 