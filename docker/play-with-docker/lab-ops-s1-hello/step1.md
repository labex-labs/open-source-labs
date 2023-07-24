# Running your first container

It's time to get your hands dirty! As with all things technical, a "hello world" app is good place to start. Type or click the code below to run your first Docker container:

```bash
docker container run hello-world
```

That's it: your first container. The _hello-world_ container output tells you a bit about what just happened. Essentially, the Docker engine running in your terminal tried to find an **image** named hello-world. Since you just got started there are no images stored locally (`Unable to find image...`) so Docker engine goes to its default **Docker registry**, which is [Docker Hub](https://hub.docker.com), to look for an image named "hello-world". It finds the image there, pulls it down, and then runs it in a container. And hello-world's only function is to output the text you see in your terminal, after which the container exits.

![Hello world explainer](/images/ops-basics-hello-world.svg)

If you are familiar with VMs, you may be thinking this is pretty much just like running a virtual machine, except with a central repository of VM images. And in this simple example, that is basically true. But as you go through these exercises you will start to see important ways that Docker and containers differ from VMs. For now, the simple explanation is this:

- The VM is a _hardware_ abstraction: it takes physical CPUs and RAM from a host, and divides and shares it across several smaller virtual machines. There is an OS and application running inside the VM, but the virtualization software usually has no real knowledge of that.
- A container is an _application_ abstraction: the focus is really on the OS and the application, and not so much the hardware abstraction.
  Many customers actually use both VMs and containers today in their environments and, in fact, may run containers inside of VMs.
