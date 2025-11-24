# tabela do banco (SQLModel)

from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

class Consulta(SQLModel, table=True):
  id_consulta: Optional[int] = Field(default=None, primary_key=True)
  data_hora: datetime
  tipo: str  # "PRESENCIAL" ou "ONLINE"
  status: str = "AGENDADA"  # AGENDADA, CANCELADA, REALIZADA


  # Relação com Paciente e Profissional de Saúde
id_paciente: int = Field(foreign_key="paciente.id_paciente")
id_profissional: int = Field(foreign_key="profissionalsaude.id_profissional")