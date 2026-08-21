terraform {
  required_version = ">= 1.0.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# Security Group para liberar SSH, App Livros (8001) e Empréstimos (8002)
resource "aws_security_group" "biblioteca_sg" {
  name        = "biblioteca_devops_sg"
  description = "Permite acesso SSH e portas dos microsservicos"

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Books Service"
    from_port   = 8001
    to_port     = 8001
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Loans Service"
    from_port   = 8002
    to_port     = 8002
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "biblioteca-sg"
  }
}

# Instancia EC2 para hospedar os microsservicos via Docker
resource "aws_instance " "biblioteca_server" {
  ami           = "ami-0c7217cdde317cfec" # Ubuntu 22.04 LTS (Exemplo validavel)
  instance_type = var.instance_type
  key_name      = var.key_name
  vpc_security_group_ids = [aws_security_group.biblioteca_sg.id]

  tags = {
    Name = "Biblioteca-DevOps-Server"
  }
}
