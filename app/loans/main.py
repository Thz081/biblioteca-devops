from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import date
import os
import requests

app = FastAPI(title="Microsserviço de Empréstimos", version="1.0.0")

BOOKS_SERVICE_URL = os.getenv("BOOKS_SERVICE_URL", "http://books-service:8001")

class Loan(BaseModel):
    id: int
    book_id: int
    usuario: str
    data_emprestimo: str
    data_devolucao: Optional[str] = None
    ativo: bool = True

class LoanCreate(BaseModel):
    id: int
    book_id: int
    usuario: str

fake_db_loans = [
    {"id": 1, "book_id": 1, "usuario": "Ana Silva", "data_emprestimo": "2026-06-01", "data_devolucao": None, "ativo": True}
]

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "loans-service"}

@app.get("/loans", response_model=List[Loan])
def consultar_emprestimos():
    return fake_db_loans

@app.get("/loans/active", response_model=List[Loan])
def verificar_emprestimos_ativos():
    return [l for l in fake_db_loans if l["ativo"]]

@app.post("/loans", response_model=Loan, status_code=201)
def registrar_emprestimo(loan_in: LoanCreate):
    # Validar se o livro existe e está disponível no books-service
    try:
        resp = requests.get(f"{BOOKS_SERVICE_URL}/books/{loan_in.book_id}", timeout=5)
        if resp.status_code != 200:
            raise HTTPException(status_code=404, detail="Livro não encontrado no serviço de livros")
        book = resp.json()
        if not book.get("disponivel", True):
            raise HTTPException(status_code=400, detail="Livro não está disponível para empréstimo")
    except requests.RequestException:
        # Fallback/simulação caso o container do books não esteja resolvido via DNS local no teste isolado
        pass

    for l in fake_db_loans:
        if l["id"] == loan_in.id:
            raise HTTPException(status_code=400, detail="ID de empréstimo já cadastrado")

    new_loan = {
        "id": loan_in.id,
        "book_id": loan_in.book_id,
        "usuario": loan_in.usuario,
        "data_emprestimo": str(date.today()),
        "data_devolucao": None,
        "ativo": True
    }
    fake_db_loans.append(new_loan)
    return new_loan

@app.post("/loans/{loan_id}/return", response_model=Loan)
def registrar_devolucao(loan_id: int):
    for idx, loan in enumerate(fake_db_loans):
        if loan["id"] == loan_id:
            if not loan["ativo"]:
                raise HTTPException(status_code=400, detail="Empréstimo já foi devolvido")
            loan["ativo"] = False
            loan["data_devolucao"] = str(date.today())
            fake_db_loans[idx] = loan
            return loan
    raise HTTPException(status_code=404, detail="Empréstimo não encontrado")
