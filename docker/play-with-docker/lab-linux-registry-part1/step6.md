# Running a Registry Container with External Storage

Remove the existing registry container by removing the container which holds the storage layer. Any images pushed will be deleted:

```bash
docker kill registry
docker rm registry
```

In this example, the new container will use a host-mounted Docker volume. When the registry server in the container writes image layer data, it appears to be writing to a local directory in the container but it will be writing to a directory on the host.

Create the registry:

```bash
mkdir registry-data
docker run -d -p 5000:5000 --name registry -v $(pwd)/registry-data:/var/lib/registry registry
```

Tag and push the container with the new IP address of the registry.

```bash
docker pull hello-world
docker tag hello-world 127.0.0.1:5000/hello-world
docker push 127.0.0.1:5000/hello-world
```

Repeating the previous `docker push` command uploads an image to the registry container, and the layers will be stored in the container's `/var/lib/registry` directory, which is actually mapped to the `$(pwd)/registry-data` directory on your machine. Storing data outside of the container means we can build a new version of the registry image and replace the old container with a new one using the same host mapping - so the new registry container has all the images stored by the previous container.

Using an insecure registry isn't practical in multi-user scenarios. Effectively there's no security so anyone can push and pull images if they know the registry hostname. The registry server supports authentication, but only over a secure SSL connection. We'll run a secure version of the registry server in a container next.