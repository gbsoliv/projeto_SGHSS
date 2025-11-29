# funções que acessam o banco de dados relacionadas a administradores

from app.models.administrador import Administrador
from sqlmodel import Session, select

from app.models.administrador import Administrador
from app.schemas.administrador import AdministradorCreate

#Cria um Administrador no banco de dados a partir de uma Pessoa existente

def criar_administrador(
    session: Session,
    dados: AdministradorCreate
) -> Administrador:
    novo_admin = Administrador(
        id_admin=dados.id_pessoa,   # PK = FK para Pessoa
        setor=dados.setor,
        nivel_acesso=dados.nivel_acesso,
    )

    session.add(novo_admin)
    session.commit()
    session.refresh(novo_admin)

    return novo_admin

#retorna todos os administradores cadastrados
def listar_administradores(session: Session) -> list[Administrador]:
    statement = select(Administrador)
    resultado = session.exec(statement)
    return list(resultado.all())

#retorna um administrador pelo ID
def buscar_administrador_por_id(
    session: Session,
    id_admin: int
) -> Administrador | None:
    statement = select(Administrador).where(Administrador.id_admin == id_admin)
    resultado = session.exec(statement)
    return resultado.first()

#Busca um administrador a partir do id_pessoa
def buscar_administrador_por_id_pessoa(
    session: Session,
    id_pessoa: int
) -> Administrador | None:
    statement = select(Administrador).where(Administrador.id_admin == id_pessoa)
    resultado = session.exec(statement)
    return resultado.first()




