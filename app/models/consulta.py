# tabela do bd > Consulta (SQLModel)

from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

class Consulta(SQLModel, table=True):
  id_consulta: Optional[int] = Field(default=None, primary_key=True)

  id_paciente: int = Field(foreign_key="paciente.id_paciente")
  id_profissional: int = Field(foreign_key="profissionalsaude.id_profissional")
  data_hora: datetime
  tipo: str  # "PRESENCIAL" ou "ONLINE"
  status: str = Field(default="AGENDADA") # "AGENDADA", "CANCELADA", "REALIZADA"
  link_teleconsulta: Optional[str] = None
