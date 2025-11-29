# formato de entrada/saída da API para consultsa médicas

from pydantic import BaseModel
from typing import Optional

from datetime import datetime

#inpouts p agendar uma consulta
class ConsultaCreate(BaseModel):
    id_paciente: int
    id_profissional_saude: int
    data_hora: datetime
    tipo_consulta: str # Ex: "presencial", "online"
    link_teleconsulta: Optional[str] = None

class ConsultaRead(BaseModel):
      id_consulta: int
      id_paciente: int
      id_profissional_saude: int
      data_hora: datetime
      tipo: str # Ex: "presencial", "online"
      link_teleconsulta: Optional[str] = None
      status: str  # Ex: "AGENDADA", "CANCELADA", "REALIZADA"

class Config:
    from_attributes = True