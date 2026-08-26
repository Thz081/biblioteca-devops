terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "3.0.1"
    }
  }
}

provider "docker" {
  host = "npipe:////./pipe/docker_engine"
}

# Construindo as imagens
resource "docker_image" "books_image" {
  name = "books-service:latest"
  build {
    context = "../app/books"
  }
}

resource "docker_image" "loans_image" {
  name = "loans-service:latest"
  build {
    context = "../app/loans"
  }
}

# Rede
resource "docker_network" "biblioteca_net" {
  name = "biblioteca-net-tf"
}

# Container Books (SÓ SOBE SE A VARIÁVEL FOR 'books' ou 'both')
resource "docker_container" "books_container" {
  count = var.service_to_deploy == "books" || var.service_to_deploy == "both" ? 1 : 0
  
  name  = "books-service"
  image = docker_image.books_image.image_id
  
  ports {
    internal = 8001
    external = 8001
  }
  
  networks_advanced {
    name = docker_network.biblioteca_net.name
  }
}

# Container Loans (SÓ SOBE SE A VARIÁVEL FOR 'loans' ou 'both')
resource "docker_container" "loans_container" {
  count = var.service_to_deploy == "loans" || var.service_to_deploy == "both" ? 1 : 0

  name  = "loans-service"
  image = docker_image.loans_image.image_id
  
  env = [
    # Isso precisa ser configurado com o IP do PC1 quando rodar no PC2
    "BOOKS_SERVICE_URL=http://books-service:8001" 
  ]
  
  ports {
    internal = 8002
    external = 8002
  }
  
  networks_advanced {
    name = docker_network.biblioteca_net.name
  }
}
