output "instance_ip" {
  description = "Endereco IP publico da instancia EC2 provisionada"
  value       = aws_instance.biblioteca_server.public_ip
}

output "books_service_url" {
  description = "URL de acesso ao microsservico de livros"
  value       = "http://${aws_instance.biblioteca_server.public_ip}:8001"
}

output "loans_service_url" {
  description = "URL de acesso ao microsservico de emprestimos"
  value       = "http://${aws_instance.biblioteca_server.public_ip}:8002"
}
