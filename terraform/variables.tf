variable "service_to_deploy" {
  description = "Define qual microsserviço este PC vai rodar. Opções: 'books', 'loans' ou 'both'"
  type        = string
  default     = "both"
}
