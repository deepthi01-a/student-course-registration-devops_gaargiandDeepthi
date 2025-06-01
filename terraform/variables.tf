variable "flask_secret" {
  type        = string
  description = "Flask secret key"
  default     = "my_flask_secret"
}

variable "jwt_secret" {
  type        = string
  description = "JWT secret key"
  default     = "my_jwt_secret"
}
