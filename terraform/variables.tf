variable "aws_region" {
  description = "Regiao da AWS para provisionamento"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "Tipo da instancia EC2"
  type        = string
  default     = "t2.micro"
}

variable "key_name" {
  description = "Nome da chave SSH para acesso ao servidor"
  type        = string
  default     = "biblioteca-key"
}
