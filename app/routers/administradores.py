# endpoints da API

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.administrador import AdministradorCreate, AdministradorRead
from app.repositories.administradores_repo import (
    criar_administrador,
    buscar_administrador_por_id_pessoa,
    listar_administradores,
    buscar_administrador_por_id,
)
from app.repositories.pessoas_repo import buscar_pessoa_por_id

router = APIRouter(
    prefix="/admin",
    tags=["Administradores"],
)


@router.post(
    "/",
    response_model=AdministradorRead,
    status_code=status.HTTP_201_CREATED,
)
def criar_administrador_endpoint(
    dados: AdministradorCreate,
    session: Session = Depends(get_session),
):

    # Verifica se a Pessoa existe
    pessoa = buscar_pessoa_por_id(session, dados.id_pessoa)
    if not pessoa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pessoa não encontrada. Crie a Pessoa antes de torná-la Administrador.",
        )

    # Verifica se essa Pessoa já é Administrador
    admin_existente = buscar_administrador_por_id_pessoa(session, dados.id_pessoa)
    if admin_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Esta pessoa já está cadastrada como administrador.",
        )

    # Cria o Administrador
    novo_admin = criar_administrador(session, dados)
    return novo_admin


@router.get("/", response_model=List[AdministradorRead])
def listar_administradores_endpoint(
    session: Session = Depends(get_session),
):
    admins = listar_administradores(session)
    return admins


@router.get("/{id_admin}", response_model=AdministradorRead)
def buscar_administrador_endpoint(
    id_admin: int,
    session: Session = Depends(get_session),
):
    admin = buscar_administrador_por_id(session, id_admin)
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Administrador não encontrado.",
        )
    return admin