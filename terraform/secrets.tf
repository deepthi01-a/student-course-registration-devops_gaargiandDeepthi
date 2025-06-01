resource "kubernetes_secret" "flask_secrets" {
  metadata {
    name      = "flask-secret"
    namespace = kubernetes_namespace.student_ns.metadata[0].name
  }

  data = {
    SECRET_KEY = base64encode("my_flask_secret")
    JWT_SECRET = base64encode("my_jwt_secret")
  }

  type = "Opaque"
}
