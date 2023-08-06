# Understanding Image Names

Typically we work with images from Docker Store, which is the default registry for Docker. Commands using just the image repository name work fine, like this:

```bash
docker pull hello-world
```

`hello-world` is the repository name, which we are using as a short form of the full image name. The full name is `docker.io/hello-world:latest`. That breaks down into three parts:

- `docker.io` - the hostname of the registry which stores the image;
- `hello-world` - the repository name, in this case in `{imageName}` format;
- `latest` - the image tag.

If a tag isn't specified, then the default `latest` is used. If a registry hostname isn't specified then the default `docker.io` for Docker Store is used. If you want to use images with any other registry, you need to explicitly specify the hostname - the default is always Docker Store.

With a local registry, the hostname and the custom port used by the registry is the full registry address, e.g. `127.0.0.1:5000`. In this sample we'll just be using `127.0.0.1:5000` as that's already been added to the daemon.
