resource "kubernetes_pod" "example_orcrist" {
  metadata {
    name      = "pod-example-orcrist"
    namespace = kubernetes_namespace.namespaces["orcrist"].metadata[0].name
  }

  spec {
    container {
      name  = "pod"
      image = "alpine"
      args  = ["cat"]
      tty   = true
      stdin = true
    }
  }
}

resource "kubernetes_pod" "nginx_tools" {
  metadata {
    name      = "pod-nginx-tools"
    namespace = kubernetes_namespace.namespaces["tools"].metadata[0].name
  }

  spec {
    container {
      name  = "pod"
      image = "nginx"

      port {
        name           = "web"
        container_port = 80
        protocol       = "TCP"
      }
    }
  }
}

resource "kubernetes_pod" "example_integration" {
  metadata {
    name      = "pod-example-integration"
    namespace = kubernetes_namespace.namespaces["integration"].metadata[0].name
  }

  spec {
    container {
      name  = "pod"
      image = "alpine"
      args  = ["cat"]
      tty   = true
      stdin = true
    }
  }
}

resource "kubernetes_pod" "example_monitoring" {
  metadata {
    name      = "pod-example-monitoring"
    namespace = kubernetes_namespace.namespaces["monitoring"].metadata[0].name
  }

  spec {
    container {
      name  = "pod"
      image = "alpine"
      args  = ["cat"]
      tty   = true
      stdin = true
    }
  }
}
