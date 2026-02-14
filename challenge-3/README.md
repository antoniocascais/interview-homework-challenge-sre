# Summary

The Dockerfile was created (with non-root user), built and run:
```
$ docker build -t chal3 .
[+] Building 0.6s (9/9) FINISHED                     docker:default
 => [internal] load build definition from Dockerfile           0.0s
 => => transferring dockerfile: 163B                           0.0s
 => [internal] load metadata for docker.io/library/python:3-s  0.6s
 => [internal] load .dockerignore                              0.0s
 => => transferring context: 2B                                0.0s
 => [internal] load build context                              0.0s
 => => transferring context: 31B                               0.0s
 => [1/4] FROM docker.io/library/python:3-slim@sha256:486b809  0.0s
 => CACHED [2/4] WORKDIR /app                                  0.0s
 => CACHED [3/4] COPY server.py .                              0.0s
 => CACHED [4/4] RUN useradd -r appuser                        0.0s
 => exporting to image                                         0.0s
 => => exporting layers                                        0.0s
 => => writing image sha256:beda844402f754e67f7cf5aacb5d28ded  0.0s
 => => naming to docker.io/library/chal3                       0.0s

$ docker run chal3
INFO:root:Listening on 8080...

INFO:root:Host: 172.17.0.2:8080
User-Agent: curl/8.17.0
Accept: */*
Challenge: orcrist.org


172.17.0.1 - - [14/Feb/2026 12:39:27] "GET / HTTP/1.1" 200 -
```

Here's the result of making a `GET` request to the server with the header `Challenge: orcrist.org`:
```
$ curl -H "Challenge: orcrist.org" 172.17.0.2:8080
Everything works!
```
