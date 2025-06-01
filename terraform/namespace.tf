resource "kubernetes_namespace" "student_ns" {
  metadata {
    name = "student-app"
  }
}
