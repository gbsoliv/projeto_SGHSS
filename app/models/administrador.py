# tabela do bd > ADM (SQLModel)

from sqlmodel import SQLModel, Field
from typing import Optional

class Administrador(SQLModel, table=True):
  id_admin: int = Field(primary_key=True, foreign_key="pessoa.id_pessoa") 
  setor: str
  nivel_acesso: str