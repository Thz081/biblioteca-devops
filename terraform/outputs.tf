output "books_service_url" {
  description = "URL de acesso ao Swagger do microsservico de livros"
  value       = var.service_to_deploy == "books" || var.service_to_deploy == "both" ? "http://localhost:8001/docs" : "Não subiu neste PC"
}

output "loans_service_url" {
  description = "URL de acesso ao Swagger do microsservico de emprestimos"
  value       = var.service_to_deploy == "loans" || var.service_to_deploy == "both" ? "http://localhost:8002/docs" : "Não subiu neste PC"
}
