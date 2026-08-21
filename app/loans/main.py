from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import date
import os
import requests

app = FastAPI(title="Microsservico de Emprestimos", version="1.1.0")

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

fake_db_loans = []

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
    # 1. Verificar se o livro existe e esta disponivel
    try:
        resp = requests.get(f"{BOOKS_SERVICE_URL}/books/{loan_in.book_id}", timeout=5)
        if resp.status_code != 200:
            raise HTTPException(status_code=404, detail="Livro nao encontrado no acervo")
        
        book = resp.json()
        if not book.get("disponivel", True):
            raise HTTPException(status_code=400, detail="Livro ja esta emprestado")
            
        # 2. Marcar livro como INDISPONIVEL no outro microsservico (Integracao)
        update_resp = requests.put(
            f"{BOOKS_SERVICE_URL}/books/{loan_in.book_id}", 
            json={"disponivel": False},
            timeout=5
        )
        if update_resp.status_code != 200:
            raise HTTPException(status_code=500, detail="Falha ao atualizar status do livro")
            
    except requests.RequestException:
        # Fallback para modo isolado (demonstracao sem rede docker ativa)
        pass

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
                raise HTTPException(status_code=400, detail="Emprestimo ja foi devolvido")
            
            # Atualizar livro para DISPONIVEL novamente
            try:
                requests.put(
                    f"{BOOKS_SERVICE_URL}/books/{loan['book_id']}", 
                    json={"disponivel": True},
                    timeout=5
                )
            except requests.RequestException:
                pass

            loan["ativo"] = False
            loan["data_devolucao"] = str(date.today())
            fake_db_loans[idx] = loan
            return loan
            
    raise HTTPException(status_code=404, detail="Emprestimo nao encontrado")
