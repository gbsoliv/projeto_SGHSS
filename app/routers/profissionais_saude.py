# endpoints da API

from typing import List, Sequence

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.profissional_saude import (
    ProfissionalSaudeCreate,
    ProfissionalSaudeRead,
)
from app.repositories.profissionais_repo import (
    criar_profissional_saude,
    listar_profissionais_saude,
    buscar_profissional_por_id,
    buscar_profissional_por_id_pessoa,
)
from app.repositories.pessoas_repo import buscar_pessoa_por_id

router = APIRouter(
    prefix="/profissionais_saude",
    tags=["Profissionais de Saúde"],
)


@router.post(
    "/",
    response_model=ProfissionalSaudeRead,
    status_code=status.HTTP_201_CREATED,
)
def criar_profissional_saude_endpoint(
    dados: ProfissionalSaudeCreate,
    session: Session = Depends(get_session),
):

    # Verifica se a Pessoa existe
    pessoa = buscar_pessoa_por_id(session, dados.id_pessoa)
    if not pessoa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pessoa não encontrada. Crie a Pessoa antes de torná-la Profissional de Saúde.",
        )

    # Verifica se já não é profissional
    profissional_existente = buscar_profissional_por_id_pessoa(session, dados.id_pessoa)
    if profissional_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Esta pessoa já está cadastrada como profissional de saúde.",
        )

    # Cria o profissional
    novo_profissional = criar_profissional_saude(session, dados)
    return novo_profissional


@router.get("/", response_model=Sequence[ProfissionalSaudeRead])
def listar_profissionais_endpoint(
    session: Session = Depends(get_session),
):
    profissionais = listar_profissionais_saude(session)
    return profissionais


@router.get("/{id_profissional}", response_model=ProfissionalSaudeRead)
def buscar_profissional_saude_endpoint(
    id_profissional: int,
    session: Session = Depends(get_session),
):
    profissional = buscar_profissional_por_id(session, id_profissional)
    if not profissional:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profissional de saúde não encontrado.",
        )
    return profissional