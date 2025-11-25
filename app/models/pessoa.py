# tabela do banco (SQLModel)

from typing import Optional
from sqlmodel import SQLModel, Field

class Pessoa(SQLModel, table=True):
    id_pessoa: Optional[int] = Field(default=None, primary_key=True)
    cpf: str
    nome: str
    sobrenome: str
    email: str
    senha: str
    perfil: str  # PACIENTE, PROFISSIONAL, ADMIN
