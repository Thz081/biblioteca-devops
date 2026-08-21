# Especificação de Requisitos - Microsserviços da Biblioteca

## 1. Microsserviço de Livros (`books-service`)
Responsável pela gestão do acervo bibliográfico.
- **Entidade Livro:** `id`, `titulo`, `autor`, `categoria`, `ano`, `disponivel` (boolean).
- **Endpoints:**
  - `POST /books`: Cadastrar novo livro.
  - `GET /books`: Listar todos os livros.
  - `GET /books/{id}`: Consultar livro específico.
  - `PUT /books/{id}`: Atualizar dados de um livro.
  - `DELETE /books/{id}`: Excluir um livro.

## 2. Microsserviço de Empréstimos (`loans-service`)
Responsável pelo controle de circulação de exemplares.
- **Entidade Empréstimo:** `id`, `book_id`, `usuario`, `data_emprestimo`, `data_devolucao`, `ativo` (boolean).
- **Endpoints:**
  - `POST /loans`: Registrar novo empréstimo.
  - `POST /loans/{id}/return`: Registrar devolução.
  - `GET /loans`: Consultar todos os empréstimos.
  - `GET /loans/active`: Verificar empréstimos ativos.
