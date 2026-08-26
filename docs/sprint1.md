# Planejamento e Relatório da Sprint 1

**Objetivo da Sprint:** Desenvolver o MVP do Sistema de Biblioteca, estabelecendo a arquitetura de microsserviços com FastAPI, containerização com Docker e validação de comunicação distribuída.

## 🎯 Funcionalidades Selecionadas
As seguintes funcionalidades de prioridade ALTA do Backlog foram selecionadas para esta Sprint:
1. Cadastrar e listar livros (`books-service`).
2. Registrar e listar empréstimos (`loans-service`).

## 🛠️ Execução e Arquitetura
A equipe definiu a stack baseada em **Python (FastAPI)**, focando em alta performance e documentação automatizada (Swagger). O sistema foi dividido em dois microsserviços independentes.

### Teste de Ambiente Distribuído (Validação Prática)
Durante o fim de semana e segunda-feira finalizamos os ajustes para separar o projeto em duas máquinas físicas distintas, simulando um ambiente de produção real. O sistema foi validado em dois computadores na mesma rede local:

- **PC 1 (Books):** Rodou o `books-service` na porta 8001.
- **PC 2 (Loans):** Rodou o `loans-service` na porta 8002. A variável de ambiente `BOOKS_SERVICE_URL` foi configurada para apontar para o endereço IP do PC 1 (ex: `http://<IP-PC-1>:8001`).

**Resultado:** A integração HTTP REST funcionou perfeitamente entre as máquinas. O `loans-service` conseguiu consultar o `books-service` remotamente, validando a arquitetura de microsserviços desacoplados e atendendo ao requisito de sistemas distribuídos da disciplina.

## 🏁 Conclusão
A Sprint 1 foi concluída com sucesso. A base do projeto está sólida e pronta para receber as próximas etapas de automação de infraestrutura (Ansible/Terraform) e pipelines (CI/CD).
