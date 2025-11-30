# funções que acessam o banco de dados consultas

from typing import List, Optional
from app.models.consulta import Consulta
from sqlmodel import Session, select
from app.schemas.consulta import ConsultaCreate


# Cria uma nova consulta no bd
def criar_consulta(
    session: Session,
    dados: ConsultaCreate
) -> Consulta:
    nova_consulta = Consulta(
        id_paciente=dados.id_paciente,
        id_profissional=dados.id_profissional,
        data_hora=dados.data_hora,
        tipo=dados.tipo,
        link_teleconsulta=dados.link_teleconsulta,
    )
    session.add(nova_consulta)
    session.commit()
    session.refresh(nova_consulta)
    return nova_consulta


# Retorna todas as consultas cadastrada
def listar_consultas(session: Session) -> List[Consulta]:
    statement = select(Consulta)
    resultado = session.exec(statement)
    return list(resultado.all())


#Busca uma consulta pelo id_consulta 
def buscar_consulta_por_id(
    session: Session,
    id_consulta: int
) -> Optional[Consulta]:
    statement = select(Consulta).where(Consulta.id_consulta == id_consulta)
    resultado = session.exec(statement)
    return resultado.first()

# Altera o status de uma consulta (ex.: CANCELADA, REALIZADA)
def alterar_status_consulta(
    session: Session,
    id_consulta: int,
    novo_status: str,
) -> Optional[Consulta]:
    consulta = buscar_consulta_por_id(session, id_consulta)
    if not consulta:
        return None

    consulta.status = novo_status
    session.add(consulta)
    session.commit()
    session.refresh(consulta)

    return consulta


