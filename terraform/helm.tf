resource "helm_release" "kube_prometheus_stack" {
  name       = "monitoring"
  namespace  = kubernetes_namespace.student_ns.metadata[0].name
  repository = "https://prometheus-community.github.io/helm-charts"
  chart      = "kube-prometheus-stack"
  version    = "56.6.0" # Adjust to latest version

  values = [
    file("${path.module}/../monitoring/prometheus-values.yaml")
  ]
}
