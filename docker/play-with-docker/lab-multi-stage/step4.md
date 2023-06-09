# Multi-stage build example

While the builder pattern helps us achieve a small image, it does require extra leg-work for every piece of software we want to package in Docker.

Here is where multi-stage builds help us out. Instead of using a shell script to orchestrate two separate Dockerfiles, we can just use one and define stages throughout.

To use the Dockerfile.multi file in the Github repository to do a multi-stage build, then check the size of the resulting image against that of the image created by the Golang SDK base and the builder pattern.

```bash
docker build -t alexellis2/href-counter:multi . -f Dockerfile.multi
```

```
docker images |grep href-counter
alexellis2/href-counter   multi               44852229a1cc        2 minutes ago       10.3MB
alexellis2/href-counter   latest              bb997f819fbb        3 minutes ago       10.3MB
alexellis2/href-counter   build               298d3b970412        4 minutes ago       692MB
alexellis2/href-counter   sdk                 298d3b970412        4 minutes ago       692MB
alexellis2/href-counter   <none>              b0a73b688243        13 days ago         11.6MB
```

Here is an example of building "Hello World" in Go.

Create a new folder:

```bash
mkdir hello
cd hello
```

Create the app.go file:

```bash
echo 'package main

import "fmt"

func main() {
    fmt.Println("Hello world!")
}
' | tee app.go
```

Create a Dockerfile with the following contents:

```bash
echo '
FROM golang:1.7.3
COPY app.go .
RUN go build -o app app.go

FROM scratch
COPY --from=0 /go/app .
CMD ["./app"]
' | tee Dockerfile
```

Now build and run the Dockerfile:

```bash
docker build -t hello-world-lab .
docker run hello-world-lab
```

The resulting size of hello-world is very small:

```bash
docker images |grep hello-world-lab
```
