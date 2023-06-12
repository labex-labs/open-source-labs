# The builder pattern

Type in `cat builder.sh` so you can see how the builder pattern uses two separate Dockerfiles. This will help us get the context for the next step where we will use a single Dockerfile.

```bash
./build.sh
```

```
#!/bin/sh
echo Building alexellis2/href-counter:build

docker build -t alexellis2/href-counter:build . -f Dockerfile.build
docker create --name extract alexellis2/href-counter:build
docker cp extract:/go/src/github.com/alexellis/href-counter/app ./app
docker rm -f extract

echo Building alexellis2/href-counter:latest
docker build -t alexellis2/href-counter:latest .
```

As you can see there are quite a few intermediate steps required to create an optimized image using the _Builder pattern_.

Let's see how big the Docker image came out as:

```bash
docker images |grep alexellis2/href-counter
```

This is much smaller than when we built our first image with the Golang SDK included.
