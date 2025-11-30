# tabela do bd > paciente (SQLModel)

from typing import Optional
from datetime import date
from sqlmodel import SQLModel, Field


class Paciente(SQLModel, table=True):

    id_paciente: Optional[int] = Field(default=None, primary_key=True)

    data_nascimento: date
    convenio: bool