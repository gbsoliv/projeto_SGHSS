# endpoints da API

from typing import List, Sequence

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.consulta import ConsultaCreate, ConsultaRead
from app.repositories.consultas_repo import (
    criar_consulta,
    listar_consultas,
    buscar_consulta_por_id,
    alterar_status_consulta,
)
from app.repositories.pacientes_repo import buscar_paciente_por_id
from app.repositories.profissionais_repo import buscar_profissional_por_id

router = APIRouter(
    prefix="/consultas",
    tags=["Consultas"],
)


@router.post(
    "/",
    response_model=ConsultaRead,
    status_code=status.HTTP_201_CREATED,
)
def agendar_consulta_endpoint(
    dados: ConsultaCreate,
    session: Session = Depends(get_session),
):

    #  Verificar Paciente
    paciente = buscar_paciente_por_id(session, dados.id_paciente)
    if not paciente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente não encontrado.",
        )

    # Verificar Profissional
    profissional = buscar_profissional_por_id(session, dados.id_profissional)
    if not profissional:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profissional da saúde não encontrado.",
        )

    # Criar Consulta
    nova_consulta = criar_consulta(session, dados)
    return nova_consulta

#Lista todas as consultas cadastradas
@router.get("/", response_model=List[ConsultaRead])
def listar_consultas_endpoint(
    session: Session = Depends(get_session),
):
    consultas = listar_consultas(session)
    return consultas


# Altera o status da consulta para CANCELADA
@router.put("/{id_consulta}/cancelar", response_model=ConsultaRead)
def cancelar_consulta_endpoint(
    id_consulta: int,
    session: Session = Depends(get_session),
):
    consulta = alterar_status_consulta(session, id_consulta, "CANCELADA")
    if not consulta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Consulta não encontrada.",
        )
    return consulta

# Altera o status da consulta para REALIZADA
@router.put("/{id_consulta}/realizar", response_model=ConsultaRead)
def realizar_consulta_endpoint(
    id_consulta: int,
    session: Session = Depends(get_session),
):
    consulta = alterar_status_consulta(session, id_consulta, "REALIZADA")
    if not consulta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Consulta não encontrada.",
        )
    return consulta