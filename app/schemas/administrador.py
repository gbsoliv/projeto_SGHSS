# formato de entrada/saída da API para o AAdm 

from pydantic import BaseModel

class AdministradorCreate(BaseModel):
    id_pessoa: int
    setor: str
    nivel_acesso: str
  

class AdministradorRead(BaseModel):
    id_administrador: int
    id_pessoa: int
    setor: str
    nivel_acesso: str

    class Config:
        orm_mode = True