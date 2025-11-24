# formato de entrada/saída da API para o recurso Pessoa

from typing import Optional
from pydantic import BaseModel


# 1. Schema de ENTRADA (POST)
class PessoaCreate(BaseModel):
    cpf: str
    nome: str
    sobrenome: str
    email: str
    senha: str
    perfil: str  # PACIENTE, PROFISSIONAL, ADMIN


  # 2. Schema de SAÍDA (GET)
class PessoaRead(BaseModel):
    id_pessoa: int
    cpf: str
    nome: str
    sobrenome: str
    email: str
    perfil: str

    class Config:
        orm_mode = True


# 3. LOGIN - entrada
class PessoaLogin(BaseModel):
    email: str
    senha: str


# 4. LOGIN - saída
class LoginResponse(BaseModel):
    id_pessoa: int
    nome: str
    perfil: str


