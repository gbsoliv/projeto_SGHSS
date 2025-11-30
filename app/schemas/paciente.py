# formato de entrada/saída da API para pACIENTE   

from datetime import date
from pydantic import BaseModel

class PacienteCreate(BaseModel):
    id_pessoa: int
    data_nascimento: date
    convenio: bool

class PacienteRead(BaseModel):
    id_paciente: int
    data_nascimento: date
    convenio: bool

    class Config:
        from_attributes = True  