resource "kubernetes_namespace" "namespaces" {
  for_each = toset(["collector", "integration", "orcrist", "monitoring", "tools"])

  metadata {
    name = each.key
  }
}
