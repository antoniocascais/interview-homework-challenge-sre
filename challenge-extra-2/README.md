# Summary

The same resources that were created via `.yml` in the challenge extra 1 are now created via terraform.
I followed the approach of having a .tf file per Kubernetes resources, in order to improve readability and also long term repo maintenance.

The provider used was the official `hashicorp/kubernetes`.
I used the deployment/service/pod/namespace resources from that provider because it fits our use case very well.
I could have also used the resource `kubernetes_manifest`, but it is less readable and more difficult to validate.

## Validation

```
$ kubectl diff -f manifests/
$ echo $?
0
```

```
$ kubectl -n orcrist port-forward pods/nginx-deployment-6847d94d85-bb8jg 8080:80Forwarding from 127.0.0.1:8080 -> 80
Forwarding from [::1]:8080 -> 80
```

```
$ curl 0.0.0.0:8080
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

## Terraform commands
```
$ terraform validate
Success! The configuration is valid.
```

```
$ terraform init

Initializing the backend...

Initializing provider plugins...
- Reusing previous version of hashicorp/kubernetes from the dependency lock file
- Using previously-installed hashicorp/kubernetes v2.38.0

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```


```
$ terraform plan -out plan

Terraform used the selected providers to generate the following
execution plan. Resource actions are indicated with the following
symbols:
  + create

Terraform will perform the following actions:

...........

Plan: 11 to add, 0 to change, 0 to destroy.

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Saved the plan to: plan

To perform exactly these actions, run the following command to apply:
    terraform apply "plan"
```

```
$ terraform apply "plan"
kubernetes_namespace.namespaces["integration"]: Creating...
kubernetes_namespace.namespaces["tools"]: Creating...
kubernetes_namespace.namespaces["monitoring"]: Creating...
kubernetes_namespace.namespaces["orcrist"]: Creating...
kubernetes_namespace.namespaces["collector"]: Creating...
kubernetes_namespace.namespaces["collector"]: Creation complete after 0s [id=collector]
kubernetes_namespace.namespaces["integration"]: Creation complete after 0s [id=integration]
kubernetes_namespace.namespaces["orcrist"]: Creation complete after 0s [id=orcrist]
kubernetes_namespace.namespaces["monitoring"]: Creation complete after 0s [id=monitoring]
kubernetes_namespace.namespaces["tools"]: Creation complete after 0s [id=tools]
kubernetes_service.nginx: Creating...
kubernetes_service.nginx: Creation complete after 0s [id=orcrist/nginx-service]
kubernetes_pod.example_monitoring: Creating...
kubernetes_pod.nginx_tools: Creating...
kubernetes_pod.example_orcrist: Creating...
kubernetes_pod.example_integration: Creating...
kubernetes_deployment.nginx: Creating...
kubernetes_pod.example_integration: Creation complete after 3s [id=integration/pod-example-integration]
kubernetes_pod.example_monitoring: Creation complete after 6s [id=monitoring/pod-example-monitoring]
kubernetes_pod.nginx_tools: Creation complete after 6s [id=tools/pod-nginx-tools]
kubernetes_pod.example_orcrist: Still creating... [10s elapsed]
kubernetes_deployment.nginx: Still creating... [10s elapsed]
kubernetes_pod.example_orcrist: Creation complete after 12s [id=orcrist/pod-example-orcrist]
kubernetes_deployment.nginx: Creation complete after 15s [id=orcrist/nginx-deployment]

Apply complete! Resources: 11 added, 0 changed, 0 destroyed.
```
