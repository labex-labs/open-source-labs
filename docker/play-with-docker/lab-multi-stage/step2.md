# The old way of doing things

Let's build the Docker image with all the Golang toolchain and see how big the image comes out as:

```bash
docker build -t alexellis2/href-counter:sdk . -f Dockerfile.build
```

Now check the size of the image:

```bash
docker images |grep href-counter
```

```
docker images |grep href-counter
href-counter        sdk                 131c782e8c35        30 second
s ago      692MB
```

The `docker history` command will show you that the layers we added during the build are only a small part of the resulting image (about 20MB +/-):

```bash
docker history alexellis2/href-counter:sdk |head -n 4
```

```
IMAGE               CREATED             CREATED BY
                   SIZE                COMMENT
f8b1953fb9c7        1 second ago        /bin/sh -c CGO_ENABLED=0 GOOS=linux go bui...   5.64MB
5d24895500e8        9 seconds ago       /bin/sh -c #(nop) COPY file:d3eec1f1fefbec...   1.71kB
d83dc0785057        9 seconds ago       /bin/sh -c go get -d -v golang.org/x/net/html   13.6MB
c6f59b210906        11 seconds ago      /bin/sh -c #(nop) WORKDIR /go/src/github.c...   0B
```

The image is quite large, but this Golang package can be built into a very small binary with no external dependencies, then added to an Alpine Linux base image.
