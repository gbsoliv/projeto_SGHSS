# endpoints da API

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.pessoa import PessoaCreate, PessoaRead
from app.repositories.pessoas_repo import (
    criar_pessoa,
    listar_pessoas,
    buscar_pessoa_por_email,
)

router = APIRouter(
    prefix="/pessoas",
    tags=["Pessoas"],
)