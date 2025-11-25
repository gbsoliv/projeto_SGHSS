# funções que acessam o banco de dados relacionadas a paciente 

from typing import List, Optional

from sqlmodel import Session, select

from app.models.paciente import Paciente
from app.schemas.paciente import PacienteCreate

def criar_paciente(session: Session, dados: PacienteCreate) -> Paciente:
    novo_paciente = Paciente(
        id_paciente=dados.id_pessoa,              # PK = FK para Pessoa
        data_nascimento=dados.data_nascimento,
        convenio=dados.convenio,
    )

    session.add(novo_paciente)
    session.commit()
    session.refresh(novo_paciente)

    return novo_paciente


def listar_pacientes(session: Session) -> List[Paciente]:
    statement = select(Paciente)
    resultado = session.exec(statement)
    return list(resultado.all())


def buscar_paciente_por_id(session: Session, id_paciente: int) -> Optional[Paciente]:
    statement = select(Paciente).where(Paciente.id_paciente == id_paciente)
    resultado = session.exec(statement)
    return resultado.first()


def buscar_paciente_por_id_pessoa(session: Session, id_pessoa: int) -> Optional[Paciente]:
    statement = select(Paciente).where(Paciente.id_paciente == id_pessoa)
    resultado = session.exec(statement)
    return resultado.first()