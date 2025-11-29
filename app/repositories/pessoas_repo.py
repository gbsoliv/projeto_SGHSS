# funções que acessam o banco de dados relacionadas a pessoas

from typing import List, Optional

from sqlmodel import Session, select

from app.models.pessoa import Pessoa
from app.schemas.pessoa import PessoaCreate


def criar_pessoa(session: Session, dados: PessoaCreate) -> Pessoa:

# Cria uma nova Pessoa no banco de dados.

    nova_pessoa = Pessoa(
        cpf=dados.cpf,
        nome=dados.nome,
        sobrenome=dados.sobrenome,
        email=dados.email,
        senha=dados.senha,
        perfil=dados.perfil,
    )

    session.add(nova_pessoa)
    session.commit()
    session.refresh(nova_pessoa)
    return nova_pessoa

# Retorna todas as Pessoas cadastradas.
    
def listar_pessoas(session: Session) -> List[Pessoa]:
    
    statement = select(Pessoa)
    resultado = session.exec(statement)
    return list(resultado.all())

# busca uma Pessoa pelo id_pessoa.
def buscar_pessoa_por_id(session: Session, id_pessoa: int) -> Optional[Pessoa]:
    statement = select(Pessoa).where(Pessoa.id_pessoa == id_pessoa)
    resultado = session.exec(statement)
    return resultado.first()
