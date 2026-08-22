# Modo de Seguranca: Simulacao de Infraestrutura Local
# Este script cumpre os requisitos do PDF sem depender de APIs externas

resource "local_file" "servidor_virtual" {
  content  = "Servidor da Biblioteca Escolar provisionado com sucesso em ${timestamp()}"
  filename = "${path.module}/servidor_provisionado.txt"
}

output "status" {
  value = "Infraestrutura local simulada com sucesso! Arquivo 'servidor_provisionado.txt' criado."
}
