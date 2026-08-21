# Sistema da Biblioteca Escolar — Microsserviços, DevOps & Gerência de Configuração

Repositório oficial da solução desenvolvida para a **Atividade Integradora**, adotando a **Opção B (Dois Microsserviços)** com arquitetura desacoplada, containerização via Docker, provisionamento automatizado com Terraform, gerência de configuração com Ansible e práticas rigorosas de DevSecOps.

---

## 1. Arquitetura da Solução (Opção B)

O sistema foi arquitetado em dois microsserviços independentes desenvolvidos em Python com FastAPI, comunicando-se via HTTP RESTful em uma rede virtual bridge do Docker Compose:

1. **Microsserviço de Livros (`books-service` - Porta 8001):**
   - Responsável pelo gerenciamento completo do acervo bibliográfico (cadastro, consulta, alteração, exclusão e listagem de livros).
   - Armazenamento isolado e endpoints validados via Pydantic.

2. **Microsserviço de Empréstimos (`loans-service` - Porta 8002):**
   - Responsável pelo controle de circulação e empréstimos de exemplares (registro de empréstimo, registro de devolução, consulta de histórico e verificação de empréstimos ativos).
   - Integra-se diretamente com o `books-service` para validação de disponibilidade de estoque.

---

## 2. Estrutura do Repositório

```text
biblioteca-devops/
├── app/
│   ├── books/
│   │   ├── Dockerfile
│   │   ├── main.py
│   │   └── requirements.txt
│   └── loans/
│       ├── Dockerfile
│       ├── main.py
│       └── requirements.txt
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
├── ansible/
│   ├── inventory.ini
│   └── instalar-biblioteca.yml
├── docker-compose.yml
├── docs/
│   ├── requisitos.md
│   └── seguranca.md
├── .gitignore
└── README.md
```

---

## 3. Instruções de Execução e Reprodução

Para reproduzir integralmente o ambiente e colocar o sistema em funcionamento, siga os comandos abaixo organizados por etapas de DevOps:

### Passo 1: Provisionamento de Infraestrutura (Terraform)
Navegue até o diretório do Terraform, inicialize e aplique o provisionamento dos recursos na nuvem:
```bash
cd terraform
terraform init
terraform plan
terraform apply -auto-approve
```

### Passo 2: Configuração do Servidor e Deploy (Ansible)
Após a obtenção do IP público da instância provisionada, atualize o arquivo `ansible/inventory.ini` com o IP correto e execute o playbook de gerência de configuração:
```bash
cd ../ansible
ansible-playbook -i inventory.ini instalar-biblioteca.yml
```

### Passo 3: Execução Local / Teste com Docker Compose
Para testar e executar a stack completa localmente:
```bash
cd ..
docker compose up -d --build
```

### Passo 4: Destruição do Ambiente (Teste de Reprodução)
Para validar a reprodutibilidade e destruir os recursos criados:
```bash
cd terraform
terraform destroy -auto-approve
```

---

## 4. Práticas de Segurança e DevSecOps

A solução implementa medidas de segurança robustas alinhadas aos pilares da segurança da informação:
- **Confidencialidade:** Isolamento de rede por Docker Bridge e Security Groups restritos no Terraform.
- **Integridade:** Validação estrita de esquemas de dados com Pydantic e versionamento com rastreabilidade de commits.
- **Disponibilidade:** Políticas de reinício automático de containers (`restart: always`) e automação idempotente com Ansible.

---

## 5. Histórico de Contribuições (Papéis da Equipe)

O desenvolvimento seguiu uma abordagem incremental com commits realizados por todos os papéis da equipe:
- **Product Owner (PO):** Definição do escopo e backlog da Opção B.
- **Analista de Requisitos:** Especificação detalhada dos microsserviços.
- **Scrum Master:** Organização da estrutura e planejamento da entrega.
- **Desenvolvedor:** Implementação dos microsserviços em FastAPI e Dockerfiles.
- **DevOps / DevSecOps:** Automação com Terraform, Ansible, Docker Compose e políticas de segurança.
