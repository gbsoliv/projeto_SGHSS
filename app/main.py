# ponto de entrada da aplicação FastAPI

from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.db.init_db import init_db
from app.routers import pessoas, pacientes

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Executa quando o servidor inicia
    init_db()
    yield


app = FastAPI(
    title="SGHSS API",
    lifespan=lifespan
)

# Inclui rotas
app.include_router(pessoas.router)
app.include_router(pacientes.router)


@app.get("/ping")
def ping():
    return {"message": "testando..."}
