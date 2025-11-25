# endpoints da API

# app/routers/pessoas.py

from typing import List

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.pessoa import PessoaCreate, PessoaRead
from app.repositories.pessoas_repo import (
    criar_pessoa,
    listar_pessoas,
)

router = APIRouter(
    prefix="/pessoas",
    tags=["Pessoas"],
)


@router.post("/", response_model=PessoaRead, status_code=status.HTTP_201_CREATED)
def criar_pessoa_endpoint(
    dados: PessoaCreate,
    session: Session = Depends(get_session),
):
    """
    Cria uma nova Pessoa no banco de dados.
    """
    nova_pessoa = criar_pessoa(session, dados)
    return nova_pessoa


@router.get("/", response_model=List[PessoaRead])
def listar_pessoas_endpoint(
    session: Session = Depends(get_session),
):
    """
    Lista todas as Pessoas cadastradas.
    """
    pessoas = listar_pessoas(session)
    return pessoas
