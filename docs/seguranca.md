# Documentação de Segurança e Práticas DevSecOps

## 1. Medidas de Segurança Aplicadas
Em conformidade com os requisitos de DevSecOps, o projeto adota as seguintes práticas de segurança:
- **Variáveis de Ambiente:** Credenciais e URLs de microsserviços não são hardcoded; utilizam variáveis injetadas via Docker Compose e ambiente de execução.
- **Princípio do Menor Privilégio:** Os containers rodam em imagens mínimas (`python:3.11-slim`) e expõem exclusivamente as portas estritamente necessárias (8001 para livros e 8002 para empréstimos).
- **Validação de Entrada:** Todas as requisições de entrada nas APIs são validadas de forma estrita utilizando Pydantic schemas, prevenindo injeções e payloads inválidos.
- **Gestão de Segredos e `.gitignore`:** Arquivos sensíveis e de configuração local (`.env`, chaves SSH privadas, diretórios `.terraform`) são ignorados pelo Git (`.gitignore`).

## 2. Tríade da Segurança da Informação
- **Confidencialidade:** Garantida pelo isolamento de rede em bridge do Docker Compose e restrição de acesso por Security Groups no Terraform, assegurando que apenas tráfexo autorizado alcance os microsserviços.
- **Integridade:** Assegurada por validações rígidas nos esquemas Pydantic e controle de versionamento estrito no Git, onde qualquer alteração no código requer rastreabilidade de commits.
- **Disponibilidade:** Promovida pelo uso de políticas de reinício automático (`restart: always`) nos containers Docker e pela automação completa via Terraform e Ansible, permitindo reconstrução rápida do ambiente em caso de falhas.
