# Quadro Kanban - Sprint 1

Este quadro reflete o status das tarefas durante a Sprint 1, onde o foco foi estabelecer a base arquitetural e as funcionalidades principais do MVP (Microsserviços de Livros e Empréstimos).

## 📋 Backlog da Sprint (To Do)
- [ ] Configuração do pipeline CI/CD básico
- [ ] Refatoração das rotas de devolução de livros

## 💻 Em Desenvolvimento (In Progress)
- [ ] Implementação de testes unitários para o `loans-service`
- [ ] Documentação da infraestrutura com Terraform

## 🔍 Em Testes (Testing)
- [ ] Comunicação entre microsserviços na rede local (PC 1 e PC 2) - *Validando latência*

## ✅ Concluído (Done)
- [x] Criação do microsserviço `books-service` (FastAPI)
- [x] Criação do microsserviço `loans-service` (FastAPI)
- [x] Dockerização dos microsserviços (Dockerfile e docker-compose)
- [x] Teste de ambiente distribuído em dois computadores separados
- [x] Configuração da comunicação HTTP entre `loans-service` e `books-service`
