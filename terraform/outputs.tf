output "namespace_name" {
  value = kubernetes_namespace.student_ns.metadata[0].name
}
