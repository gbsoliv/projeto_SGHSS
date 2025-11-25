# endpoints da API

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.paciente import PacienteCreate, PacienteRead
from app.repositories.pacientes_repo import (
    criar_paciente,
    listar_pacientes,
    buscar_paciente_por_id,
    buscar_paciente_por_id_pessoa,
)
from app.repositories.pessoas_repo import buscar_pessoa_por_id

router = APIRouter(
    prefix="/pacientes",
    tags=["Pacientes"],
)



"""
    Cria um Paciente a partir de uma Pessoa existente.

    1. Verifica se a Pessoa existe
    2. Verifica se a Pessoa já não é Paciente
    3. Cria o registro na tabela Paciente

    """

@router.post("/", response_model=PacienteRead, status_code=status.HTTP_201_CREATED)
def criar_paciente_endpoint(
    dados: PacienteCreate,
    session: Session = Depends(get_session),
):

    #  Verifica se a Pessoa existe
    pessoa = buscar_pessoa_por_id(session, dados.id_pessoa)
    if not pessoa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pessoa não encontrada. Crie a Pessoa antes de torná-la Paciente.",
        )
    
    #Verifica se essa Pessoa já é Paciente
    paciente_existente = buscar_paciente_por_id_pessoa(session, dados.id_pessoa)
    if paciente_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Esta pessoa já está cadastrada como paciente.",
        )

    # Cria o Paciente
    novo_paciente = criar_paciente(session, dados)
    return novo_paciente


@router.get("/", response_model=List[PacienteRead])
def listar_pacientes_endpoint(
    session: Session = Depends(get_session),
):
  
    # Lista todos os Pacientes cadastrados.
  
    pacientes = listar_pacientes(session)
    return pacientes


@router.get("/{id_paciente}", response_model=PacienteRead)
def buscar_paciente_endpoint(
    id_paciente: int,
    session: Session = Depends(get_session),
):

    # Busca um Paciente pelo id_paciente.
    
    paciente = buscar_paciente_por_id(session, id_paciente)
    if not paciente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente não encontrado.",
        )
    return paciente