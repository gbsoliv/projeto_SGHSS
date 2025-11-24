# ponto de entrada da aplicação FastAPI

from fastapi import FastAPI
from app.db.init_db import init_db

app = FastAPI(title="SGHSS API")

@app.on_event("startup")
def on_startup():
    init_db()

# endpoint de teste 
@app.get("/ping")
def ping():
    return {"message": "testando"}
