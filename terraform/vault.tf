provider "helm" {
  kubernetes {
    config_path = "~/.kube/config"
  }
}

resource "helm_release" "vault" {
  name       = "vault"
  namespace  = kubernetes_namespace.student_ns.metadata[0].name
  repository = "https://helm.releases.hashicorp.com"
  chart      = "vault"
  version    = "0.27.0" # adjust to latest stable

  values = [
    <<EOF
server:
  dev:
    enabled: true
  dataStorage:
    enabled: false
EOF
  ]
}
