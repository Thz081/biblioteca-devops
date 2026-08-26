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

# 1. Construindo as imagens a partir do código fonte
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

# 2. Criando a rede isolada (Confidencialidade/Segurança)
resource "docker_network" "biblioteca_net" {
  name = "biblioteca-net-tf"
}

# 3. Subindo o Container Books de verdade
resource "docker_container" "books_container" {
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

# 4. Subindo o Container Loans de verdade
resource "docker_container" "loans_container" {
  name  = "loans-service"
  image = docker_image.loans_image.image_id
  
  env = [
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
