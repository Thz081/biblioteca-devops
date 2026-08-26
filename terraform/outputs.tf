output "books_service_url" {
  description = "URL de acesso ao Swagger do microsservico de livros"
  value       = "http://localhost:8001/docs"
}

output "loans_service_url" {
  description = "URL de acesso ao Swagger do microsservico de emprestimos"
  value       = "http://localhost:8002/docs"
}
