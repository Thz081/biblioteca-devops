terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "ubuntu" {
  name         = "ubuntu:22.04"
  keep_locally = true
}

resource "docker_container" "biblioteca_server" {
  image = docker_image.ubuntu.image_id
  name  = "biblioteca-server-demo"
  
  ports {
    internal = 8001
    external = 8001
  }
  ports {
    internal = 8002
    external = 8002
  }
  
  command = ["tail", "-f", "/dev/null"]
}

output "instance_ip" {
  value = "localhost"
}
