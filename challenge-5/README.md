# Challenge 5: Helm Chart

## Objective

Create a Helm chart to deploy the Python HTTP server from Challenge 3 to Kubernetes.

## Background

The Challenge 3 server is a Python HTTP application that:
- Listens on **port 8080**
- Returns `200 OK` with "Everything works!" when the request includes header `Challenge: orcrist.org`
- Returns `404 Not Found` with "Wrong header!" otherwise

Assume the Docker image has been built from your Challenge 3 Dockerfile.

## Requirements

Complete the Helm chart in `server-chart/` with the following:

### 1. values.yaml
Define configurable values for:
- Container image (repository, tag, pull policy)
- Number of replicas
- Service configuration (type, port)
- Resource limits/requests (optional)

### 2. templates/deployment.yaml
Create a Kubernetes Deployment that:
- Deploys the container image
- Exposes container port 8080
- Uses values from values.yaml

### 3. templates/service.yaml
Create a Kubernetes Service that:
- Exposes the deployment
- Routes traffic to port 8080

### 4. (Optional) templates/_helpers.tpl
Add template helpers for consistent naming and labels.

## Deliverables

A working Helm chart that can be:
1. Validated with: `helm lint ./server-chart`
2. Rendered with: `helm template ./server-chart`
3. Installed with: `helm install server ./server-chart`

## Acceptance Criteria

- [X] `helm lint` passes without errors
```
$ helm lint server-chart/
==> Linting server-chart/
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

- [X] `helm template` renders valid Kubernetes manifests
```
$ helm template server-chart/
---
# Source: server-chart/templates/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: release-name-server-chart
  labels:
    app.kubernetes.io/name: server-chart
    app.kubernetes.io/instance: release-name
    app.kubernetes.io/version: "1.0.0"
    app.kubernetes.io/managed-by: Helm
spec:
  type: ClusterIP
  ports:
    - port: 8080
      targetPort: 8080
      protocol: TCP
  selector:
    app.kubernetes.io/name: server-chart
    app.kubernetes.io/instance: release-name
---
# Source: server-chart/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: release-name-server-chart
  labels:
    app.kubernetes.io/name: server-chart
    app.kubernetes.io/instance: release-name
    app.kubernetes.io/version: "1.0.0"
    app.kubernetes.io/managed-by: Helm
spec:
  replicas: 1
  selector:
    matchLabels:
      app.kubernetes.io/name: server-chart
      app.kubernetes.io/instance: release-name
  template:
    metadata:
      labels:
        app.kubernetes.io/name: server-chart
        app.kubernetes.io/instance: release-name
    spec:
      containers:
        - name: server
          image: "chal3:latest"
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 8080
```

- [X] Deployment targets container port 8080
```
# Source: server-chart/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
...
    spec:
      containers:
        - name: server
          image: "chal3:latest"
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 8080
```
- [X] Service correctly routes to the deployment
```
apiVersion: v1
kind: Service
spec:
  type: ClusterIP
  ports:
    - port: 8080
      targetPort: 8080
      protocol: TCP
  selector:
    app.kubernetes.io/name: server-chart
    app.kubernetes.io/instance: release-name
---
# Source: server-chart/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app.kubernetes.io/name: server-chart
      app.kubernetes.io/instance: release-name
  template:
    metadata:
      labels:
        app.kubernetes.io/name: server-chart
        app.kubernetes.io/instance: release-name
```
- [X] All hardcoded values are parameterized in values.yaml
Everything can be set via values.yaml.

### Extra sanity checks

To be 100% sure everything is working as expected, I ran Minikube and installed the chart there:

```
$ kubectl get nodes
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   11m   v1.32.0

$ helm install server ./server-chart/
NAME: server
LAST DEPLOYED: Sat Feb 14 16:14:21 2026
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

The Service and Deployment were configured properly and pod is running as expected:
```
$ kubectl get service
NAME                  TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
kubernetes            ClusterIP   10.96.0.1      <none>        443/TCP    12m
server-server-chart   ClusterIP   10.101.85.43   <none>        8080/TCP   10m
$ kubectl get deployments.apps
NAME                  READY   UP-TO-DATE   AVAILABLE   AGE
server-server-chart   1/1     1            1           10m
$ kubectl get pods
NAME                                   READY   STATUS    RESTARTS   AGE
server-server-chart-6b7fc9b979-m97j7   1/1     Running   0          10m
```

I didn't setup an Ingress, so the Service is not reachable from outside the cluster.
But running a test pod inside the cluster that makes a curl against the Service shows the expected output:

```
kubectl run curl-test --image=curlimages/curl --rm -it --restart=Never -- curl -s -H "Challenge: orcrist.org" http://server-server-chart:8080
Everything works!pod "curl-test" deleted
```
