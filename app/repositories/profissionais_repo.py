# funções que acessam o banco de dados relacionadas a profissionais da saude

from typing import List, Optional
from sqlmodel import Session, select

from app.models.profissional_saude import ProfissionalSaude
from app.schemas.profissional_saude import ProfissionalSaudeCreate


# Cria um Profissional de Saúde no banco de dados a partir de uma Pessoa existente

def criar_profissional_saude(
    session: Session,
    dados: ProfissionalSaudeCreate
) -> ProfissionalSaude:
    novo_profissional = ProfissionalSaude(
        id_profissional=dados.id_pessoa,  # PK = FK para Pessoa
        crm=dados.crm,
        especialidade=dados.especialidade,
        unidade_saude=dados.unidade_saude,
        disponibilidade=dados.disponibilidade,
    )

    session.add(novo_profissional)
    session.commit()
    session.refresh(novo_profissional)

    return novo_profissional


# retorna todos os Profissionais de Saúde cadastrados
def listar_profissionais_saude(session: Session) -> List[ProfissionalSaude]:
  
    statement = select(ProfissionalSaude)
    resultado = session.exec(statement)
    return list(resultado.all())

# retorna um Profissional de Saúde pelo ID

def buscar_profissional_por_id(
    session: Session,
    id_profissional: int
) -> Optional[ProfissionalSaude]:
    statement = select(ProfissionalSaude).where(
        ProfissionalSaude.id_profissional == id_profissional
    )
    resultado = session.exec(statement)
    return resultado.first()

# Busca um Profissional de Saúde a partir do id_pessoa 
def buscar_profissional_por_id_pessoa(
    session: Session,
    id_pessoa: int
) -> Optional[ProfissionalSaude]:
    statement = select(ProfissionalSaude).where(
        ProfissionalSaude.id_profissional == id_pessoa
    )
    resultado = session.exec(statement)
    return resultado.first()