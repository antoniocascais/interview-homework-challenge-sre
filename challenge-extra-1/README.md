# Summary

All yml files applied successfully on Minikube:

```
$ kubectl get nodes
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   20m   v1.32.0

$ kubectl apply -f manifests/
namespace/collector created
namespace/integration created
namespace/orcrist created
namespace/monitoring created
namespace/tools created
deployment.apps/nginx-deployment created
service/nginx-service created
pod/pod-example-orcrist created
pod/pod-nginx-tools created
pod/pod-example-integration created
pod/pod-example-monitoring created
```

## Validation according to main README.md

### Get all namespaces

```
$ kubectl get namespaces
NAME              STATUS   AGE
collector         Active   2m12s
default           Active   20m
integration       Active   2m12s
kube-node-lease   Active   20m
kube-public       Active   20m
kube-system       Active   20m
monitoring        Active   2m12s
orcrist           Active   2m12s
tools             Active   2m12s
```

### Get all pods from all namespaces.

```
$ kubectl get pods -A
NAMESPACE     NAME                               READY   STATUS    RESTARTS      AGE
integration   pod-example-integration            1/1     Running   0             2m36s
kube-system   coredns-668d6bf9bc-jjpwt           1/1     Running   0             21m
kube-system   etcd-minikube                      1/1     Running   0             21m
kube-system   kube-apiserver-minikube            1/1     Running   0             21m
kube-system   kube-controller-manager-minikube   1/1     Running   0             21m
kube-system   kube-proxy-sf5pd                   1/1     Running   0             21m
kube-system   kube-scheduler-minikube            1/1     Running   0             21m
kube-system   storage-provisioner                1/1     Running   1 (20m ago)   21m
monitoring    pod-example-monitoring             1/1     Running   0             2m36s
orcrist       nginx-deployment-96b9d695-4kv5g    1/1     Running   0             2m36s
orcrist       nginx-deployment-96b9d695-4rdcz    1/1     Running   0             2m36s
orcrist       nginx-deployment-96b9d695-j25kg    1/1     Running   0             2m36s
orcrist       pod-example-orcrist                1/1     Running   0             2m36s
tools         pod-nginx-tools                    1/1     Running   0             2m36s
```

### Get all resources from all namespaces.

```
$ kubectl get all -A
NAMESPACE     NAME                                   READY   STATUS    RESTARTS      AGE
integration   pod/pod-example-integration            1/1     Running   0             3m1s
kube-system   pod/coredns-668d6bf9bc-jjpwt           1/1     Running   0             21m
kube-system   pod/etcd-minikube                      1/1     Running   0             21m
kube-system   pod/kube-apiserver-minikube            1/1     Running   0             21m
kube-system   pod/kube-controller-manager-minikube   1/1     Running   0             21m
kube-system   pod/kube-proxy-sf5pd                   1/1     Running   0             21m
kube-system   pod/kube-scheduler-minikube            1/1     Running   0             21m
kube-system   pod/storage-provisioner                1/1     Running   1 (21m ago)   21m
monitoring    pod/pod-example-monitoring             1/1     Running   0             3m1s
orcrist       pod/nginx-deployment-96b9d695-4kv5g    1/1     Running   0             3m1s
orcrist       pod/nginx-deployment-96b9d695-4rdcz    1/1     Running   0             3m1s
orcrist       pod/nginx-deployment-96b9d695-j25kg    1/1     Running   0             3m1s
orcrist       pod/pod-example-orcrist                1/1     Running   0             3m1s
tools         pod/pod-nginx-tools                    1/1     Running   0             3m1s

NAMESPACE     NAME                    TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)                  AGE
default       service/kubernetes      ClusterIP   10.96.0.1      <none>        443/TCP                  21m
kube-system   service/kube-dns        ClusterIP   10.96.0.10     <none>        53/UDP,53/TCP,9153/TCP   21m
orcrist       service/nginx-service   ClusterIP   10.106.53.42   <none>        80/TCP                   3m1s

NAMESPACE     NAME                        DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR            AGE
kube-system   daemonset.apps/kube-proxy   1         1         1       1            1           kubernetes.io/os=linux   21m

NAMESPACE     NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
kube-system   deployment.apps/coredns            1/1     1            1           21m
orcrist       deployment.apps/nginx-deployment   3/3     3            3           3m1s

NAMESPACE     NAME                                        DESIRED   CURRENT   READY   AGE
kube-system   replicaset.apps/coredns-668d6bf9bc          1         1         1       21m
orcrist       replicaset.apps/nginx-deployment-96b9d695   3         3         3       3m1s
```

### Get all services from namespace `orcrist`.

```
$ kubectl get svc -n orcrist
NAME            TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
nginx-service   ClusterIP   10.106.53.42   <none>        80/TCP    3m22s
```

### Get all deployments from `tools`.

```
$ kubectl get deployment -n tools
No resources found in tools namespace.
```

### Get image from `nginx` deployment on `orcrist` namespace.

```
$ kubectl get deployment nginx-deployment -n orcrist -o jsonpath='{.spec.template.spec.containers[0].image}'
nginx:latest
```

### Create a `port-forward` to access `nginx` pod on `orcrist` namespace.

Because the README explicitly says "port forward to pod", I did port forward to one of the pods. Could have done port-forward to a deployment or service instead.

```
$ kubectl -n orcrist port-forward pods/nginx-deployment-96b9d695-4kv5g 8080:80
Forwarding from 127.0.0.1:8080 -> 80
Forwarding from [::1]:8080 -> 80
```
