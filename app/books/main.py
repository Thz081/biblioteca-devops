from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import os

app = FastAPI(title="Microsserviço de Livros", version="1.0.0")

class Book(BaseModel):
    id: int
    titulo: str
    autor: str
    categoria: str
    ano: int
    disponivel: bool = True

class BookUpdate(BaseModel):
    titulo: Optional[str] = None
    autor: Optional[str] = None
    categoria: Optional[str] = None
    ano: Optional[int] = None
    disponivel: Optional[bool] = None

# In-memory storage for simplicity & robustness in container demo
fake_db_books = [
    {"id": 1, "titulo": "Clean Code", "autor": "Robert C. Martin", "categoria": "Engenharia de Software", "ano": 2008, "disponivel": True},
    {"id": 2, "titulo": "DevOps Handbook", "autor": "Gene Kim", "categoria": "DevOps", "ano": 2016, "disponivel": True}
]

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "books-service"}

@app.get("/books", response_model=List[Book])
def listar_livros():
    return fake_db_books

@app.get("/books/{book_id}", response_model=Book)
def consultar_livro(book_id: int):
    for book in fake_db_books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Livro não encontrado")

@app.post("/books", response_model=Book, status_code=201)
def cadastrar_livro(book: Book):
    for b in fake_db_books:
        if b["id"] == book.id:
            raise HTTPException(status_code=400, detail="ID de livro já cadastrado")
    fake_db_books.append(book.dict())
    return book

@app.put("/books/{book_id}", response_model=Book)
def atualizar_livro(book_id: int, book_update: BookUpdate):
    for idx, book in enumerate(fake_db_books):
        if book["id"] == book_id:
            updated_data = book.copy()
            if book_update.titulo is not None:
                updated_data["titulo"] = book_update.titulo
            if book_update.autor is not None:
                updated_data["autor"] = book_update.autor
            if book_update.categoria is not None:
                updated_data["categoria"] = book_update.categoria
            if book_update.ano is not None:
                updated_data["ano"] = book_update.ano
            if book_update.disponivel is not None:
                updated_data["disponivel"] = book_update.disponivel
            fake_db_books[idx] = updated_data
            return updated_data
    raise HTTPException(status_code=404, detail="Livro não encontrado")

@app.delete("/books/{book_id}", status_code=204)
def excluir_livro(book_id: int):
    for idx, book in enumerate(fake_db_books):
        if book["id"] == book_id:
            fake_db_books.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Livro não encontrado")
