# formato de entrada/saída da API para a entidade ProfissionalSaude

from pydantic import BaseModel
class ProfissionalSaudeCreate(BaseModel):
    id_pessoa: int
    especialidade: str
    crm: str
    unidade_saude: str
    disponibilidade: bool

class ProfissionalSaudeRead(BaseModel):
    id_profissional: int
    especialidade: str
    crm: str
    unidade_saude: str
    disponibilidade: bool

    class Config:
        from_attributes = True